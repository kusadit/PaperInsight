import streamlit as st
import fitz
from transformers import pipeline, AutoTokenizer
import torch
from io import BytesIO

# ---- Summarization Pipeline ----
@st.cache_resource
def load_summarizer():
    model_name = "sshleifer/distilbart-cnn-12-6"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    summarizer = pipeline("summarization", model=model_name, tokenizer=tokenizer, device=-1)
    return summarizer, tokenizer

summarizer, tokenizer = load_summarizer()

# ---- PDF Text Extraction ----
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# ---- Chunking Function ----
def chunk_text(text, tokenizer, max_tokens=300):
    tokens = tokenizer.encode(text, truncation=False)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i+max_tokens]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)
    return chunks

# ---- Summarize Text with Progress ----
def summarize_text(text):
    chunks = chunk_text(text, tokenizer, max_tokens=300)
    summary_text = ""
    
    progress_bar = st.progress(0)
    
    for i, chunk in enumerate(chunks, 1):
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        summary_text += summary + " "
        progress_bar.progress(i / len(chunks))
    
    progress_bar.empty()
    return summary_text

# ---- Streamlit UI ----
st.title("PaperInsight ")
st.write("Upload your PDF and get a summarized version ")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    
    with st.spinner("Extracting text from PDF..."):
        original_text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("Original Text Preview")
    st.text(original_text[:1000] + "...")
    
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(original_text)
        
        st.subheader("Summary")
        st.write(summary)
        
        summary_bytes = summary.encode("utf-8")
        st.download_button(
            label="Download Summary as TXT",
            data=summary_bytes,
            file_name="summary.txt",
            mime="text/plain"
        )
