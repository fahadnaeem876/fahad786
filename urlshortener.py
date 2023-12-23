from flask import Blueprint, render_template, request
import requests

urlshortener_app = Blueprint("urlshortener", __name__)

class URLShortener:
    def __init__(self):
        self.endpoint = "http://tinyurl.com/api-create.php"

    def shorten_url(self, long_url):
        try:
            response = requests.get(f"{self.endpoint}?url={long_url}")
            if response.status_code == 200:
                short_url = response.text
                return short_url
            else:
                return None
        except Exception as e:
            return None

@urlshortener_app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    warning = None
    error = None

    if request.method == 'POST':
        long_url = request.form.get('long_url')
        if long_url:
            shortener = URLShortener()
            short_url = shortener.shorten_url(long_url)
            if short_url:
                return render_template('urlshortener.html', short_url=short_url)
            else:
                error = 'An error occurred while shortening the URL.'
        else:
            warning = 'Please enter a URL.'

    return render_template('urlshortener.html', short_url=short_url, warning=warning, error=error)
