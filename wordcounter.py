from flask import Flask, render_template, request, Blueprint

wordcounter_app = Blueprint("wordcounter",__name__)

def count_words_characters_lines(text):
    words = text.split()
    characters = len(text)
    lines = text.splitlines()
    return len(words), characters, len(lines)

@wordcounter_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form.get("input_text")
        word_count, character_count, line_count = count_words_characters_lines(input_text)
        return render_template("wordcounter.html", word_count=word_count, character_count=character_count, line_count=line_count, input_text=input_text)

    return render_template("wordcounter.html", word_count=None, character_count=None, line_count=None, input_text=None)
