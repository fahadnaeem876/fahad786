from flask import Flask, render_template, request , Blueprint
import easyocr
from PIL import Image

imagetotext_app = Blueprint("imagetotext",__name__)

def image_to_text(image_path):
    reader = easyocr.Reader(['en'])  # Language code for English
    result = reader.readtext(image_path)
    text = ' '.join([entry[1] for entry in result])
    return text

@imagetotext_app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file from the form
        uploaded_file = request.files['file']

        if uploaded_file:
            # Save the uploaded image to a temporary file
            temp_image_path = "imagetotextuploadimages/temp_image.jpg"
            uploaded_file.save(temp_image_path)

            # Perform OCR on the image
            text = image_to_text(temp_image_path)

            # Display the extracted text
            return render_template('imagetotext.html', text=text)

    # Render the main page if no file is uploaded or on initial load
    return render_template('imagetotext.html')

