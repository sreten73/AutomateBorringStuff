import csv
import PyPDF2
import re
import requests


# Grab the Google Drive Link from .csv File

data = open('find_the_link.csv', encoding = 'utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_str = ''
for row_num, data in enumerate(data_lines):
    link_str += data[row_num]
print(link_str)

# Download pdf file from given link
find_number_pdf = requests.get(link_str)
with open('Find_Phone_Number.pdf','wb') as f:
    f.write(find_number_pdf.content)

# Method One to search for phone number in pdf file

# Open PDF file
pdf_file = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Make pattern for phone number
phone_number_pattern = re.compile('\d{3}.*\d{3}.*\d{4}')

# Search pattern in the text from the all pages
for page_num in range(len(pdf_reader.pages)):
    # One page
    page = pdf_reader.pages[page_num]
    # Take text from one page
    text = page.extract_text()
    # Search pattern in the text
    matches = phone_number_pattern.findall(text)
    for match in matches:
        phone_number = match
        print(match)

print(f'Trazeni broj telefona je {phone_number}')

# Method Two to find phone number in the pdf file

# pattern
pattern = r'\d{3}.\d{3}.\d{4}'
# Search pattern in the text from the all pages
for n in range(len(pdf_reader.pages)):
    # One page
    page = pdf_reader.pages[n]
    # Text from one page
    page_text = page.extract_text()
    # Search pattern in the text from one page
    match = re.search(pattern,page_text)
    if match:
        phone_number1 = match.group()
        print(match.group())

print(f'Trazeni broj po drugom metodu je isti, telefonski broj je {phone_number1}')