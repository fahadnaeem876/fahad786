from flask import Flask, render_template, request, Blueprint
import easyocr
from PIL import Image

imagetotext_app = Blueprint("imagetotext", __name__)

def image_to_text(image_path):
    reader = easyocr.Reader(['en'])  # Language code for English
    result = reader.readtext(image_path)
    
    # Extract text from EasyOCR results
    extracted_text = ' '.join([entry[1] for entry in result])
    
    return extracted_text, result

def add_spacing_to_text(text):
    words = text.split()
    spaced_text = ' '.join(words)
    return spaced_text

def identify_text_format(ocr_results):
    # Implement your logic to analyze OCR results and identify text format
    # For example, you can check for specific patterns or characteristics in the results
    # and provide information about the text format
    # This is just a placeholder, and you need to customize it based on your requirements.
    format_info = "Text format: [Add your format analysis logic here]"
    return format_info

@imagetotext_app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file from the form
        uploaded_file = request.files['file']

        if uploaded_file:
            # Save the uploaded image to a temporary file
            temp_image_path = "imagetotextuploadimages/temp_image.jpg"
            uploaded_file.save(temp_image_path)

            # Perform OCR on the image using EasyOCR
            text, ocr_results = image_to_text(temp_image_path)

            # Identify the text format
            format_info = identify_text_format(ocr_results)

            # Add spacing to the extracted text
            spaced_text = add_spacing_to_text(text)

            # Display the extracted text and format information
            return render_template('imagetotext.html', text=spaced_text, format_info=format_info)

    # Render the main page if no file is uploaded or on initial load
    return render_template('imagetotext.html')
