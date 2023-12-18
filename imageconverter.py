from flask import Flask, render_template, request, send_file, Blueprint
from reportlab.pdfgen import canvas
from PIL import Image
from io import BytesIO

imageconverter_app = Blueprint("imageconverter",__name__)

def image_to_pdf(img):
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=img.size)
    pdf.drawInlineImage(img, 0, 0, width=img.width, height=img.height)
    pdf.save()
    return pdf_buffer.getvalue()

@imageconverter_app.route('/')
def index():
    return render_template('imageconverter.html')

@imageconverter_app.route('/', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        image = Image.open(file)
        pdf_content = image_to_pdf(image)
        
        file_name = file.filename.split(".")[0]
        pdf_filename = f"{file_name}.pdf"

        return send_file(BytesIO(pdf_content),
                         download_name=pdf_filename,
                         mimetype='application/pdf')


