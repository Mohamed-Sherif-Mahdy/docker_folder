from newspaper import Article
import re
import string
from nltk.tokenize import word_tokenize
url1='https://www.hplovecraft.com/writings/texts/fiction/bws.aspx'
article1 = Article(url1)
article1.download()
article1.parse()
url2='https://www.gutenberg.org/files/1342/1342-h/1342-h.htm'
article2 = Article(url2)
article2.download()
article2.parse()
def clean_text(text):
    text= ''.join([word for word in text if word not in string.punctuation])
    text= text.lower()
    text=re.sub("\s\s+", " ", text)
    return text
remove="The Project Gutenberg eBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere in the United States and most other parts of the world at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org . If you are not located in the United States, you will have to check the laws of the country where you are located before using this eBook. Title: Pride and Prejudice Author: Jane Austen Release Date: June, 1998 [eBook #1342] [Most recently updated: February 10, 2021] Language: English Character set encoding: UTF-8 Produced by: Anonymous Volunteers and David Widger *** START OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE *** THERE IS AN ILLUSTRATED EDITION OF THIS TITLE WHICH MAY VIEWED AT EBOOK [# 42671 ] Pride and Prejudice By Jane Austen Contents ten Contents"
start=len(remove)
article2.text=article2.text[start:]
article2.text= clean_text(article2.text)
article1.text= clean_text(article1.text)
document_1_words = article1.text.split()
document_2_words = article2.text.split()
common = set(document_1_words).intersection( set(document_2_words) )
print(common)
