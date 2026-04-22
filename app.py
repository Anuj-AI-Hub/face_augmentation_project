from flask import Flask, render_template, request
from PIL import Image
import os
from augment import generate_augmentations_from_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "static/output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    images = []

    if request.method == "POST":
        file = request.files["image"]
        num_images = int(request.form["num_images"])

        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            img = Image.open(path).convert("RGB")

            # clear old output
            for f in os.listdir(OUTPUT_FOLDER):
                os.remove(os.path.join(OUTPUT_FOLDER, f))

            paths = generate_augmentations_from_image(img, OUTPUT_FOLDER, num_images)

            images = [f"/{p}" for p in paths]

    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True) 