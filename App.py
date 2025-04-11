from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form['nama']
    email = request.form['email']
    return f"Terima kasih, {nama}! Email Anda ({email}) telah terdaftar."

if __name__ == '__main__':
    app.run(debug=True)