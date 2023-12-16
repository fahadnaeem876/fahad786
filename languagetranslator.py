from flask import Flask, render_template, request, Blueprint
from googletrans import Translator

languagetranslator_app = Blueprint("languagetranslator", __name__)

# Language names and codes
language_names = {
    "English": "english",
    "Spanish": "Spanish",
    "French": "French",
    "Hindi": "Hindi",
    "German": "German",
    "Japanese": "Japanese",
    "Urdu": "Urdu",
    "Arabic": "Arabic"
}

@languagetranslator_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        from_lang = request.form.get("from_lang")
        to_lang = request.form.get("to_lang")

        translator = Translator()
        try:
            translation = translator.translate(user_input, src=from_lang, dest=to_lang)
            translated_text = translation.text if translation else "Translation failed. Please try again."
        except Exception as e:
            print(f"Translation error: {e}")
            translated_text = "An error occurred during translation."

        return render_template(
            "languagetranslator.html",
            translated_text=translated_text,
            user_input=user_input,
            from_lang=from_lang,
            to_lang=to_lang,
            language_names=language_names
        )

    return render_template(
        "languagetranslator.html",
        translated_text=None,
        user_input=None,
        from_lang=None,
        to_lang=None,
        language_names=language_names
    )

    app = Flask(__name__)
    app.register_blueprint(languagetranslator_app, url_prefix="/languagetranslator")
    app.run(debug=True)
