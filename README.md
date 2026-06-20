# **MonReader**

## **Project Overview**
MonReader is a deep learning project that combines image classification, optical character recognition (OCR), and text-to-speech (TTS) technologies.


The project is divided into two major components:
1. Deep Learning Image Classification using CNN architectures.
2. OCR-to-Speech Web Application deployed using Flask.

---

## **Business Problem**
The goal is to build intelligent systems capable of understanding image content and converting textual information into accessible audio output.


This project explores:
- Image classification using convolutional neural networks.
- Text extraction from images.
- Speech generation from extracted text.

---

## **Part 1: Deep Learning Image Classification**
## Objective:
Develop and compare multiple CNN architectures for image classification.


### Models Evaluated:
- Custom CNN
A custom-built convolutional neural network designed as a baseline model.

- ResNet
Residual learning architecture that helps train deeper neural networks effectively.

- MobileNet
Lightweight architecture optimized for computational efficiency.

- EfficientNet
State-of-the-art architecture balancing model depth, width, and resolution.

### Workflow:
```
Image Upload
      │
      ▼
OCR Extraction
      │
      ▼
Text Cleaning
      │
      ▼
Text-to-Speech
      │
      ▼
Audio Generation
      │
      ▼
  Playback
```

### Evaluation Metrics:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Results:
| Model         | Accuracy |
|---------------|----------|
| CNN           | XX%      |
| ResNet        | XX%      |
| MobileNet     | XX%      |
| EfficientNet  | XX%      |

---

## **Part 2: OCR-to-Speech Flask Application**

### Objective:
Convert text embedded in images into spoken audio.

### Technologies:
#### OCR
- Qwen Vision Model


### Text-to-Speech
- Sesame CSM

### Web Framework
- Flask

### Application Workflow:
```
Image Upload
      │
      ▼
OCR Extraction
      │
      ▼
Text Cleaning
      │
      ▼
Text-to-Speech
      │
      ▼
Audio Generation
      │
      ▼
Playback

Application Architecture
app.py
   │
   ├── ocr.py
   │
   └── tts.py
```

### Running Locally:
1. Clone Repository
```
git clone https://github.com/codebrew09/MonReader.git
```

2. Install Dependencies
```
pip install -r flask_app/requirements.txt
```

3. Start Flask Server
```
cd flask_app
python app.py
```

4. Open Browser
```
http://127.0.0.1:5000
```

---

Future Improvements
- Multi-language OCR
- PDF support
- Faster inference
- Cloud deployment
- User authentication
