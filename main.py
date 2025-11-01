from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running ✅"

@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "friend")
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/sum", methods=["POST"])
def do_sum():
    data = request.get_json() or {}
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"result": a + b})

if __name__ == "__main__":
    # Replit συνήθως ακούει στο 0.0.0.0 και port 8000
    app.run(host="0.0.0.0", port=8000)