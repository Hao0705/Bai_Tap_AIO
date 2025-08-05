import docx
from docx import Document

def extract_unique_words_from_docx(file_path):

    text = Document(file_path)

    words = ''
    for word in text.paragraphs:
        words += word.text + ''

    words.sp