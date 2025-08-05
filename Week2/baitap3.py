from docx import Document
import re

def extract_unique_words_from_docx(file_path):

    doc = Document(file_path)

    text = ''
    for para in doc.paragraphs:
        text += para.text + ' '
    text = text.lower()

    words = re.split(r'[,\.\s]+', text)
    words = [word for word in words if word]

    return words

def count_word_frequencies(words):
    my_dict = {}

    for value in words:

        if value in my_dict:
            my_dict[value] += 1
        else:
            my_dict[value] = 1

    return my_dict
file_path = "C:/AIO/Bai_tap/Week2/text.docx"
words = extract_unique_words_from_docx(file_path)

my_dict = count_word_frequencies(words)
print(my_dict)
