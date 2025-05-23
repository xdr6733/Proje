import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "Uygulama Render’da çalışıyor!"}), 200

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Merhaba, bu herkese açık bir API!"})

if __name__ == '__main__':
    # Lokal geliştirme için (Render zaten gunicorn’dan dinleyecek)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
