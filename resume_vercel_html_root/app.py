
# api/index.py
from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__, template_folder='templates', static_folder='static')

# ---- load your data ----
with open(os.path.join(os.path.dirname(__file__), '..', 'resume.json'), 'r', encoding='utf-8') as f:
    RESUME = json.load(f)

@app.get("/")
def root():
    return render_template("index.html", r=RESUME, photo_data="YOUR_DATA_URI_HERE")

@app.get("/api/resume")
def get_resume():
    return jsonify(RESUME)
