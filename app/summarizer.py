# summarizer.py
from transformers import pipeline
import math

# Load the BART summarization pipeline once
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)  # CPU

def chunk_text(text, max_chars=1000):
    """
    Split the text into smaller chunks for safe summarization.
    max_chars: number of characters per chunk (adjustable)
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        # Ensure we don't cut mid-word
        if end < len(text):
            end = text.rfind(" ", start, end)
            if end == -1:  # fallback if no space found
                end = start + max_chars
        chunks.append(text[start:end].strip())
        start = end
    return chunks

def summarize_text(text, chunk_size=1000, max_length=150, min_length=40):
    """
    Summarize the text in chunks and combine the results.
    """
    if not text.strip():
        return "No text to summarize."

    chunks = chunk_text(text, max_chars=chunk_size)
    summaries = []

    for i, chunk in enumerate(chunks, 1):
        try:
            summary = summarizer_pipeline(chunk, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        except Exception as e:
            summaries.append(f"[Error summarizing chunk {i}: {e}]")

    # Combine all chunk summaries into final summary
    final_summary = " ".join(summaries)
    return final_summary
