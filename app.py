import os
from flask import Flask, render_template, request
from wordcounter import wordcounter_app
from weatherapp import weatherapp_app
from currencyconverter import currencyconverter_app
from languagetranslator import languagetranslator_app
from imageconverter import imageconverter_app
from pdftoword import pdftoword_app
from imagetotext import imagetotext_app
from urlshortener import urlshortener_app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(wordcounter_app, url_prefix="/wordcounter")
app.register_blueprint(weatherapp_app, url_prefix="/weatherapp")
app.register_blueprint(currencyconverter_app, url_prefix="/currencyconverter")
app.register_blueprint(languagetranslator_app, url_prefix="/languagetranslator")  
app.register_blueprint(imageconverter_app, url_prefix="/imageconverter")
app.register_blueprint(pdftoword_app, url_prefix="/pdftoword")
app.register_blueprint(imagetotext_app, url_prefix="/imagetotext")
app.register_blueprint(urlshortener_app, url_prefix="/urlshortener")


if __name__ == '__main__':
    try:
        os.makedirs('uploads', exist_ok=True)
        os.makedirs('outputs', exist_ok=True)
        app.run(port=8004)
    except Exception as e:
        print(f"An error occurred: {e}")

