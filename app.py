from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # herkese açık hale getirir

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Merhaba, bu herkese açık bir API!"})

if __name__ == '__main__':
    app.run()
