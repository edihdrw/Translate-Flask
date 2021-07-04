from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        try:
            teks_kalimat = request.form["kalimat"].lower()
            dest_bahasa = request.form["dest"]
            src_bahasa = request.form["src"]
            teks_translate = translator.translate(
                teks_kalimat, src=src_bahasa, dest=dest_bahasa)
            text = teks_translate.text
        except:
            text = "Kata yang di masukan kosong"
        return render_template('index.html', translation_result=text)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
