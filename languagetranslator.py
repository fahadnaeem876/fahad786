from flask import Flask, render_template, request, Blueprint
from googletrans import Translator

languagetranslator_app = Blueprint("languagetranslator",__name__)

@languagetranslator_app.route('/', methods=['GET', 'POST'])
def translate_text():
    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        target_language = request.form['target_language']

        translator = Translator()

        try:
            detected_language = translator.detect(text_to_translate).lang
            translated_text = translator.translate(text_to_translate, dest=target_language).text

            return render_template('languagetranslator.html', 
                                   original_text=text_to_translate, 
                                   detected_language=detected_language,
                                   target_language=target_language,
                                   translated_text=translated_text)
        except Exception as e:
            error_message = f"Error: {e}"
            return render_template('languagetranslator.html', error_message=error_message)

    return render_template('languagetranslator.html')
