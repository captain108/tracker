import sys
import os
from flask import Flask, render_template
import json

# Ensure parent directory (with utils/) is in Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.tracking_utils import load_data  # Now works on Render

app = Flask(__name__)

@app.route("/")
def index():
    try:
        data = load_data()
        return render_template("index.html", tracked=data)
    except Exception as e:
        return f"<h1>Error loading data</h1><p>{e}</p>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render-compatible port
