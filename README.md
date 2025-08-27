# PaperInsight

**Status:** Work in Progress

PaperInsight is an AI-powered tool designed to summarize research papers and extract important keywords. The goal is to help researchers, students, and professionals quickly understand the core ideas of any scientific document.

---

## Planned Features

- Upload PDF research papers.
- Extract and clean text from PDFs.
- Summarize content using HuggingFace Transformers models.
- Extract keywords using KeyBERT.
- View summaries and keywords in a clean Streamlit interface.
- Download summaries as text files.

---

## Project Structure

PaperInsight/
├── app/ # Core Python code
│ ├── pdf_utils.py # PDF extraction functions
│ ├── text_cleaning.py # Text preprocessing functions
│ ├── summarizer.py # Summarization + Keyword extraction
│ └── streamlit_app.py # Main Streamlit app
├── data/ # Sample PDFs for testing
├── notebooks/ # Optional notebooks for experiments
├── models/ # Optional: store pretrained models
├── requirements.txt # Python dependencies
├── README.md # Project description
└── .gitignore # Ignored files/folders


License

This project is currently under development. License will be added once the project is complete.
