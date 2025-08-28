# PaperInsight

PaperInsight is a web application that extracts and summarizes text from PDF research papers. It leverages **Python**, **Streamlit**, and **HuggingFace Transformers** to provide concise summaries from large documents.

## Features
- Upload PDFs and extract text.
- Breaks documents into manageable chunks for summarization.
- Generates clear and concise summaries using advanced NLP models.
- Handles large research papers efficiently.

## Project Structure
- `app/` – Contains the main Streamlit application (`app.py`) and supporting scripts.  
- `data/` – Folder to store sample PDFs or datasets.  
- `models/` – Pretrained models or model checkpoints for summarization.  
- `notebooks/` – Jupyter notebooks for experimentation or testing.  
- `.gitignore` – Git ignore rules for Python, virtual environments, and IDE-specific files.  
- `requirements.txt` – List of dependencies for the project.  
- `LICENSE` – License information for the project.  
- `README.md` – Project overview and instructions.

```
  PaperInsight
│
├── app
│   ├── pdf_utils.py
│   ├── streamlit_app.py
│   ├── summarizer.py
│   └── text_cleaning.py
│
├── data
│
├── models
├── notebooks
├── .gitignore
├── LICENSE
└── README.md
└──requirements.txt
 ```

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd PaperInsight
   ```
2. Create and activate a virtual environment:
  ```bash
  python -m venv venv
  venv\Scripts\activate   # Windows
  source venv/bin/activate  # macOS/Linux
  ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the Streamlit app:
```bash
streamlit run app/app.py
```
Then open the provided URL in your browser, upload a PDF, and get the summarized text.


