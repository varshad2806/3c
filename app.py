
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Application!"

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello, World!",
        "status": "success"
    })

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    return jsonify({
        "message": "Data received successfully",
        "data": data
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
