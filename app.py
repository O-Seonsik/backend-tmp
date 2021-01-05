from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    description = "안녕하세요 반갑습니다."
    date = "2021/01/6 02:17:32"
    author = "오선식"
    return jsonify(description=description, date=date, author=author)


if __name__ == '__main__':
    app.run()
