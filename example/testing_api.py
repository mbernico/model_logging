# TODO Replace with Mock in the future when you trust yourself

from flask import Flask, request, flash, jsonify

app = Flask(__name__)


def unpack_payload(content):
    a = content['a']
    b = content['b']
    return a, b


def adder(a,b):
    return a + b


@app.route('/v666/predict/', methods=['POST'])
def predict():
    content = request.json
    a, b = unpack_payload(content)
    answer = adder(a,b)
    return jsonify({"answer":answer})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)