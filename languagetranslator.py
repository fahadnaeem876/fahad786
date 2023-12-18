from flask import Flask, render_template, request, Blueprint
from googletrans import Translator, LANGUAGES

languagetranslator_app = Blueprint("languagetranslator", __name__)

@languagetranslator_app.route('/', methods=['GET', 'POST'])
def translate_text():
    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        target_language = request.form['target_language']

        translator = Translator()

        try:
            # Detect the language
            detected_language = translator.detect(text_to_translate)
            detected_language_code = detected_language.lang if detected_language else None

            # Translate the text
            translated_text = translator.translate(text_to_translate, dest=target_language).text

            return render_template('languagetranslator.html',
                                   original_text=text_to_translate,
                                   detected_language=LANGUAGES.get(detected_language_code, "Unknown"),
                                   target_language=LANGUAGES.get(target_language, "Unknown"),
                                   translated_text=translated_text)
        except Exception as e:
            error_message = f"Error: {e}"
            return render_template('languagetranslator.html', error_message=error_message)

    return render_template('languagetranslator.html')
