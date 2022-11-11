from flask import Flask, render_template, request, redirect, url_for
from googlesearch import search

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['text']
        with open('word.txt', 'w', encoding='utf-8') as f:
            f.write(word)
        return redirect(url_for('plagiarism')+"#hasil")
    return render_template("index.html")

@app.route('/plagiarism', methods=['GET', 'POST'])
def plagiarism():
    link_output = []
    hasil_plagiarism = []
    hasil_link = []
    hasil_persen = 0
    inputan_mentah = ""
    if request.method == 'POST':
        inputan_mentah += request.form['text']
    else:
        f = open("word.txt", "r")
        inputan_mentah += f.read()
    inputan = inputan_mentah.replace("\n", " ").split(". ")
    for i in range(len(inputan)):
        query = '"' + inputan[i].strip().replace(".", "").replace('"', "'") + '"'
        for j in range(len(list(search(query, tld="com", num=10, stop=10, pause=2)))):
            if i != j:
                continue
            hasil_plagiarism.append(inputan[i])
            hasil_link.append(list(search(query, tld="com", num=10, stop=10, pause=2))[j])
    count = len(inputan)
    count_hasil = len(hasil_link)
    hasil_persen += (count_hasil / count) * 100
    for i in range(len(hasil_link)):
        link_output.append(hasil_link[i])
    return render_template("index.html", hasil_persen=hasil_persen, data=inputan, hasil_plagiarism=hasil_plagiarism, link_output=link_output, hasil_link=hasil_link)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
