from flask import Flask, render_template, request, send_file, Blueprint
import os
from PyPDF2 import PdfReader
from docx import Document

pdftoword_app = Blueprint("pdftoword", __name__)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_word(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

def pdf_to_word(pdf_path, output_path):
    text = pdf_to_text(pdf_path)
    text_to_word(text, output_path)

@pdftoword_app.route('/')
def index():
    return render_template('pdftoword.html')

@pdftoword_app.route('/', methods=['POST'])
def upload_file():
    upload_folder = 'uploads'
    output_folder = 'outputs'

    # Ensure 'uploads' directory exists
    os.makedirs(upload_folder, exist_ok=True)

    if 'file' not in request.files:
        return render_template('pdftoword.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('pdftoword.html', error='No selected file')

    if file and allowed_file(file.filename):
        filename = file.filename
        pdf_path = os.path.join(upload_folder, filename)
        word_output_path = os.path.join(output_folder, 'output.docx')

        file.save(pdf_path)
        pdf_to_word(pdf_path, word_output_path)

        # Send the Word file in the response with the original filename
        return send_file(word_output_path, as_attachment=True, download_name=filename.replace('.pdf', '.docx'))

    return render_template('pdftoword.html', error='Invalid file type')


 

