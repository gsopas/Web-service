from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes — allows your frontend to reach it

@app.route('/')
def home():
    return jsonify({"message": "Flask server running successfully"})

# Example API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"data": "Hello from Flask!"})

if __name__ == '__main__':
    # important for Render / Replit / any host — use PORT env variable if present
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
