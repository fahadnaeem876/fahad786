from flask import render_template, request, Blueprint
from googletrans import Translator, LANGUAGES
import langid

languagetranslator_app = Blueprint("languagetranslator", __name__)
translator = Translator()

@languagetranslator_app.route('/', methods=['GET', 'POST'])
def translate_text():
    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        target_language = request.form['target_language']

        try:
            # Detect the language using langid
            detected_language, confidence = langid.classify(text_to_translate)
            detected_language_code = detected_language if confidence > 0.5 else None

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
