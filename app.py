from flask import Flask, render_template, request
from wordcounter import wordcounter_app
from weatherapp import weatherapp_app
from currencyconverter import currencyconverter_app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(wordcounter_app, url_prefix="/wordcounter")
app.register_blueprint(weatherapp_app, url_prefix="/weatherapp")
app.register_blueprint(currencyconverter_app, url_prefix="/currencyconverter")

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
