from flask import Flask, render_template, request ,Blueprint
from googletrans import Translator

languagetranslator_app = Blueprint("languagetranslator",__name__)

# Language names and codes
language_names = {
    "English": "English",
    "Spanish": "Spanish",
    "French": "French",
    "Hindi": "Hindi",
    "German": "German",
    "Japanese": "Japanese",
    "Urdu": "urdu",
    "Arabic": "Arabic"
}

@languagetranslator_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        from_lang = request.form.get("from_lang")
        to_lang = request.form.get("to_lang")

        translator = Translator()
        translated_text = translator.translate(user_input, src=from_lang, dest=to_lang).text

        return render_template("languagetranslator.html", translated_text=translated_text, user_input=user_input, from_lang=from_lang, to_lang=to_lang, language_names=language_names)

    return render_template("languagetranslator.html", translated_text=None, user_input=None, from_lang=None, to_lang=None, language_names=language_names)


