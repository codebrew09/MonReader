# MonReader: Image-to-Text Generation using Vision-Language Models

## Project Overview

MonReader is an end-to-end image-to-text generation application that uses a Vision-Language Model (VLM) to generate natural language descriptions from uploaded images.

The project demonstrates the complete lifecycle of developing and deploying a machine learning application:

1. Building and evaluating deep learning models
2. Integrating a Vision-Language Model into a web application
3. Developing a Flask-based user interface
4. Containerizing the application using Docker
5. Deploying the Docker container to AWS EC2
6. Making the application accessible through a public web endpoint

Unlike a traditional machine learning notebook project, this repository focuses on taking a trained model from experimentation all the way to a cloud-hosted application.

---

# Project Objectives

The main objectives of this project are:

- Develop an image understanding application using deep learning techniques.
- Explore different computer vision architectures including:
  - Custom CNN
  - ResNet
  - EfficientNet
  - MobileNet
- Implement a Flask web application for user interaction.
- Integrate a Vision-Language Model for image caption generation.
- Containerize the application using Docker.
- Deploy the application on AWS EC2.
- Understand the challenges involved in deploying machine learning applications in real-world environments.

---

# Key Features

## Image Upload Interface

Users can upload an image through a simple web interface.

The application processes the uploaded image and generates a natural language description.

---

## Vision-Language Model Integration

The application uses a pre-trained Vision-Language Model to understand image content and generate human-like descriptions.

The inference pipeline:
```
Image Upload
      │
      ▼
Image Preprocessing
      │
      ▼
Vision Encoder
      │
      ▼
Language Decoder
      │
      ▼
Generated Description
```

---

## Flask Web Application

A lightweight Flask application provides:

- User interface
- Image upload functionality
- Model inference endpoint
- Generated caption display

---

## Docker Deployment

The application is containerized to ensure consistent execution across different environments.

Docker provides:

- Dependency isolation
- Reproducible environments
- Easy deployment
- Simplified application management

Deployment flow:
```
Application Code
      │
      ▼
  Dockerfile
      │
      ▼
 Docker Image
      │
      ▼
Docker Container
      │
      ▼
Running Flask Application
      │
      ▼
Vision-Language Model
```


---

# Overall Project Architecture

The complete system architecture is shown below:

```
     User
      │
      ▼
Web Application
      │
      ▼
Image Processing Pipeline
      │
      ▼
Vision-Language Model (BLIP)
      │
      ▼
Generated Text Output
```


Deployment architecture:
```
Development Machine
      │
      ▼
Flask Application
      │
      ▼
Docker Build
      │
      ▼
Docker Image
      │
      ▼
Docker Container
      │
      ▼
AWS EC2 Instance
      │
      ▼
Public Web Application
```

---

# Project Development Workflow

The project followed the following development lifecycle:

Step 1: Model Development
Step 2: Model Evaluation
Step 3: Flask Application Development
Step 4: Local Application Testing
Step 5: Docker Containerization
Step 6: Local Docker Testing
Step 7: AWS EC2 Deployment
Step 8: Public Application Access


---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Deep Learning Framework | PyTorch |
| Computer Vision | CNN, ResNet, EfficientNet, MobileNet |
| Vision-Language Model | BLIP |
| Frontend | HTML, CSS |
| Containerization | Docker |
| Cloud Platform | AWS EC2 |
| Operating System | Ubuntu Linux |
| Version Control | Git & GitHub |

---

# Repository Structure

The repository is organized as follows:
```
MonReader/

│
├── app.py
│ └── Flask application entry point
│
├── model/
│ └── Machine learning model files
│
├── templates/
│ └── HTML templates for web interface
│
├── static/
│ └── CSS, JavaScript, and frontend assets
│
├── uploads/
│ └── Temporary uploaded images
│
├── requirements.txt
│ └── Python dependencies
│
├── Dockerfile
│ └── Docker image configuration
│
├── .dockerignore
│ └── Files excluded from Docker build
│
├── notebooks/
│ └── Model development and experimentation
│
├── assets/
│ └── Documentation images and screenshots
│
└── README.md
└── Project documentation
```

---

# Project Highlights

This project demonstrates knowledge across multiple areas:

## Machine Learning

- Computer vision model development
- Transfer learning
- Vision-language inference
- Model integration

## Software Development

- Flask API development
- Web application structure
- Frontend integration

## DevOps / MLOps

- Docker image creation
- Container management
- Cloud deployment
- Infrastructure troubleshooting

## Cloud Computing

- AWS EC2 provisioning
- Security Group configuration
- Public application hosting

---
