from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    description = "안녕하세요 반갑습니다."
    date = "2021/01/6 02:17:32"
    author = "오선식"
    return jsonify(description=description, date=date, author=author)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
