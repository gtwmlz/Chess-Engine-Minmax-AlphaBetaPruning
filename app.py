from flask import Flask, request, jsonify, send_from_directory
from engine import find_best_move
import os

app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.route("/health", methods=["GET"])
def health():
    return "OK", 200


@app.route("/best-move", methods=["POST"])
def best_move():
    payload = request.get_json() or {}
    fen = payload.get("fen")
    depth = int(payload.get("depth", 3))
    if not fen:
        return jsonify({"error": "Missing 'fen' in JSON payload"}), 400

    result = find_best_move(fen, depth)
    return jsonify(result)


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
