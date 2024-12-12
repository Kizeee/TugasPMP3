# main.py

from flask import Flask, render_template

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk halaman tentang
@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

# Route untuk halaman kontak
@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

# Route untuk halaman profil
@app.route('/profil')
def profil():
    return render_template('profil.html')

if __name__ == '__main__':
    app.run(debug=True)