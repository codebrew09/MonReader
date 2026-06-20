from flask import Flask, render_template, request, send_from_directory
import os

from ocr import extract_text
from tts import text_to_audio

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # 1. Get uploaded file
    image = request.files["image"]

    # 2. Save file safely
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # 3. OCR (EasyOCR)
    text = extract_text(image_path)

    # 4. TTS
    audio_path = text_to_audio(text)

    # 5. Fix path for browser
    audio_file = "/" + audio_path.replace("\\", "/")

    return render_template(
        "result.html",
        extracted_text=text,
        audio_file=audio_file
    )


# Serve audio files
@app.route("/outputs/<filename>")
def serve_audio(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)