from flask import Flask, request, render_template

app = Flask(__name__)

lyrics_db = {
    "workers": "I keep my workers compensated so they don't strike",
    "dreams": "Yesterday is history, tomorrow's a mystery"
}

@app.route('/', methods=['GET', 'POST'])
def home():
    quote = ""
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        quote = lyrics_db.get(keyword.lower(), "No quote found for this keyword.")
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)