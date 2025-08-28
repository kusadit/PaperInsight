import re

def clean_text(text):
    """
    Cleans the extracted PDF text.
    Removes extra spaces, newlines, and special characters.
    """
    text = re.sub(r'\s+', ' ', text)        # replace multiple whitespace with single space
    text = re.sub(r'\[[0-9]*\]', '', text)  # remove references like [1], [2]
    text = text.strip()
    return text
