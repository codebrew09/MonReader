# Flask Application Documentation

# Overview

The Image-to-Audio system is developed using the Flask web framework. Flask serves as the backend of the application, providing a lightweight web server that handles user requests, processes uploaded images, performs Optical Character Recognition (OCR), converts the extracted text into speech, and returns the generated audio file to the user.

The application follows a modular design where each component performs a specific task:

- Flask manages HTTP requests and responses.
- OCR extracts text from uploaded images.
- Text-to-Speech converts the extracted text into audio.
- HTML templates provide the user interface.


---

# Application Structure

```
Project/
│
├── app.py
├── ocr.py
├── tts.py
├── test_ocr.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
│
├── templates/
│
├── uploads/
│
└── outputs/
```

## File Description

| File / Folder | Description |
|---------------|-------------|
| app.py | Main Flask application |
| ocr.py | Performs Optical Character Recognition (OCR) |
| tts.py | Converts extracted text into speech |
| templates/ | HTML pages displayed to users |
| uploads/ | Stores uploaded image files |
| outputs/ | Stores generated audio files |

---

# Flask Application Workflow

The application processes user requests through the following sequence:

```
User
   |
   v
Browser
   |
   v
Flask (app.py)
   |
   +---------------------------+
   |                           |
   v                           v
OCR Module (ocr.py)      HTML Templates
   |
   v
Extracted Text
   |
   v
Text-to-Speech Module (tts.py)
   |
   v
Generated Audio File
   |
   v
Flask Response
   |
   v
Browser
```

---

# Application Process

## Step 1: User Opens the Website

The user accesses the Flask application through a web browser.

Example:

```
http://localhost:5000
```

or

```
http://<EC2-Public-IP>:5000
```

Flask loads the main HTML page stored in the `templates` directory.

---

## Step 2: Upload an Image

The user selects an image containing text.

The image is submitted to the Flask server using an HTTP POST request.

Flask temporarily stores the uploaded file inside the `uploads` directory.

---

## Step 3: Optical Character Recognition (OCR)

After receiving the uploaded image, Flask calls the OCR module (`ocr.py`).

The OCR process extracts readable text from the image.

Output example:

```
Artificial Intelligence is transforming modern technology.
```

---

## Step 4: Text-to-Speech Conversion

The extracted text is sent to the Text-to-Speech module (`tts.py`).

The module generates an audio file representing the extracted text.

The generated audio is saved inside the `outputs` directory.

---

## Step 5: Return Result

Flask prepares the response and sends the generated audio back to the browser.

The user can then play or download the generated speech.

---

# Flask Components

## app.py

Responsibilities:

- Starts the Flask application
- Handles routes
- Accepts uploaded images
- Calls the OCR module
- Calls the Text-to-Speech module
- Returns the generated result to the user

---

## ocr.py

Responsibilities:

- Reads uploaded images
- Detects text within the image
- Returns extracted text to Flask

---

## tts.py

Responsibilities:

- Receives extracted text
- Generates speech audio
- Saves audio to the outputs folder
- Returns the audio file location

---

## templates/

Contains HTML pages used by Flask to build the web interface.

These templates display:

- Upload page
- Processing status
- Generated audio output

---

## uploads/

Stores images uploaded by users before OCR processing.

---

## outputs/

Stores generated audio files after Text-to-Speech conversion.

---

# Flask Request Lifecycle

```
User Uploads Image
          |
          v
Flask Receives Request
          |
          v
Save Image
          |
          v
OCR Processing
          |
          v
Extract Text
          |
          v
Text-to-Speech Processing
          |
          v
Generate Audio File
          |
          v
Return Response to User
```

---

# Running the Flask Application

Run the application using:

```bash
python app.py
```

Flask starts a local development server.

Example output:

```
Running on http://127.0.0.1:5000
```

The application can then be accessed through a web browser.

---

# Advantages of Using Flask

- Lightweight and easy to develop
- Simple routing mechanism
- Easily integrates with OCR and Text-to-Speech libraries
- Supports HTML templates through Jinja2
- Compatible with Docker for containerized deployment
- Easily deployable on cloud platforms such as AWS EC2

---

# Summary

Flask serves as the central controller of the Image-to-Audio application. It receives user requests, coordinates communication between the OCR and Text-to-Speech modules, manages uploaded and generated files, and returns the final audio output through a web interface. This modular architecture improves maintainability, simplifies future enhancements, and supports deployment in both local and cloud environments.
