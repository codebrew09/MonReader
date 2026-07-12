# Flask Application

## Overview

Flask was used to build the web interface for MonReader.

The application allows users to upload an image, processes the image using the Vision-Language Model, and displays the generated caption.

---

## Application Workflow

```
User Uploads Image
        │
        ▼
Flask Receives Request
        │
        ▼
Image Processing
        │
        ▼
BLIP Model Inference
        │
        ▼
Generated Caption
        │
        ▼
Display Result
```

---

## Local Deployment

Clone the repository:

```bash
git clone https://github.com/codebrew09/MonReader.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

## Features

- Image upload interface
- Model inference
- Caption generation
- Simple and responsive UI
