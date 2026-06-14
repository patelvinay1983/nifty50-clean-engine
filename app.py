from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "NIFTY50 CLEAN ENGINE RUNNING"

@app.route("/api/status")
def status():
    return jsonify({
        "engine": "NIFTY50 CLEAN ENGINE",
        "status": "RUNNING",
        "version": "1.0"
    })

@app.route("/api/signal")
def signal():
    return jsonify({
        "pcr": 0,
        "signal": "NO TRADE",
        "confidence": 0,
        "support": 0,
        "resistance": 0,
        "signal_reason": "INITIAL CLEAN BUILD"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
