# 📖 MonReader
## Image-to-Text Generation using Vision-Language Models
---

# 📌 Project Overview

MonReader is an end-to-end image-to-text generation application that uses a Vision-Language Model (VLM) to generate natural language descriptions from uploaded images.

The project demonstrates the complete lifecycle of developing and deploying a machine learning application:

- Model experimentation and evaluation
- Vision-Language Model integration
- Flask web application development
- Docker containerization
- Cloud deployment using AWS EC2


Unlike a traditional machine learning notebook project, this repository focuses on transforming a trained model into an accessible web application deployed in a cloud environment.


---

# 🎯 Project Objectives

The objectives of this project are:

- Explore deep learning approaches for image understanding
- Implement and evaluate multiple computer vision architectures
- Develop a Flask-based machine learning application
- Integrate a Vision-Language Model for image caption generation
- Containerize the application using Docker
- Deploy the application on AWS EC2
- Understand practical challenges involved in ML application deployment


---

# ✨ Key Features

## Image Upload

Users can upload images through a web interface.


## Image Understanding

The application analyzes uploaded images using a Vision-Language Model.


## Text Generation

The model generates natural language descriptions based on image content.


## Deployment Ready

The application can run through:

- Local Flask environment
- Docker container
- AWS EC2 deployment


---

# 🏗️ System Architecture
```
     User
             |
             ↓
      Flask Web Application
             |
             ↓
    Vision-Language Model
             |
             ↓
    Generated Description
```


Deployment architecture:

```
     Developer Machine
             |
             ↓
     Flask Application
             |
             ↓
       Docker Image
             |
             ↓
      Docker Container
             |
             ↓
      AWS EC2 Instance
             |
             ↓
    Public Web Application
```


---

# 🔄 End-to-End Process Flow


The project was developed following this workflow:

```
Step 1: Model Development (ResNet, EfficientNet, MobileNet, and Custom CNN)
             |
             ↓
Step 2: Vision-Language Model Integration
             |
             ↓
Step 3: Flask Web Application Development
             |
             ↓
Step 4: Local Application Testing
             |
             ↓
Step 5: Docker Containerization
             |
             ↓
Step 6: Local Docker Deplyoment
             |
             ↓
Step 7: AWS EC2 Deployment
             |
             ↓
Step 8: Public Application Access
```


---

# 🛠️ Technology Stack


| Category | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Deep Learning Framework | PyTorch |
| Computer Vision | CNN, ResNet, EfficientNet, MobileNet |
| Vision-Language Model | BLIP |
| Containerization | Docker |
| Cloud Platform | AWS EC2 |
| Operating System | Ubuntu Linux |
| Version Control | GitHub |


---

# 📂 Repository Structure
```
MonReader/

│
├── app.py
│
├── models/
│
├── templates/
│
├── static/
│
├── notebooks/
│
├── requirements.txt
│
├── Dockerfile
│
├── docs/
│
│ ├── 01_Model_Development.md
│ │
│ ├── 02_Flask_Application.md
│ │
│ ├── 03_Docker_Implementation.md
│ │
│ ├── 04_AWS_Deployment.md
│ │
│ ├── 05_Troubleshooting.md
│ │
│ └── 06_Lessons_Learned.md
│
├── assets/
│
└── README.md
```


---

# 📚 Detailed Documentation


For detailed implementation steps, please refer to:


## Model Development

Explanation of:

- CNN baseline model
- ResNet
- EfficientNet
- MobileNet
- Vision-Language Model integration


➡️ See:

`docs/01_Model_Development.md`



---

## Flask Application

Details about:

- Flask structure
- Application workflow
- Image upload process
- Local execution


➡️ See:

`docs/02_Flask_Application.md`



---

## Docker Implementation

Details about:

- Docker concepts
- Dockerfile
- Building images
- Running containers
- Local Docker deployment


➡️ See:

`docs/03_Docker_Implementation.md`



---

## AWS Deployment

Details about:

- EC2 setup
- Docker deployment
- Security Groups
- Public access configuration


➡️ See:

`docs/04_AWS_Deployment.md`



---

## Troubleshooting

Common problems encountered during development and deployment.


➡️ See:

`docs/05_Troubleshooting.md`



---

# 🚀 Future Improvements

Potential improvements include:

- GPU-based AWS deployment
- HTTPS configuration
- CI/CD pipeline
- Model optimization
- Container orchestration using Kubernetes
- Automated testing


---

# 👨‍💻 Author

Codebrew09

GitHub:
https://github.com/codebrew09


