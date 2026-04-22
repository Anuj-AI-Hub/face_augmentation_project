from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Face Augmentation Working 🚀"

# Vercel handler (IMPORTANT)
def handler(request, response):
    return app