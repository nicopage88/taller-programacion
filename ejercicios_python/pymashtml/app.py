from flask import Flask, request, send_file, send_from_directory
import qrcode
from io import BytesIO
import os

app = Flask(__name__)

# Servir el HTML sin necesidad de carpeta templates
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), "index.html")

@app.route('/generar', methods=['POST'])
def generar_qr():
    texto = request.form['texto']
    qr = qrcode.make(texto)
    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
