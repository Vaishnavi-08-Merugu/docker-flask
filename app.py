from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Hello from Flask in Docker!")

if __name__ == "__main__":
    # bind to 0.0.0.0 so Docker port mapping works
    app.run(host="0.0.0.0", port=5000)
