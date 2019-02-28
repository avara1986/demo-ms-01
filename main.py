from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/healthcheck")
def healthcheck():
    return "OK"

@app.route("/test")
def hello_with_stuffs():
    return jsonify(requests.get("https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe").json())

@app.route("/")
def hello():
    return "My Awesome Feature! Force hook"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080,debug=False)
