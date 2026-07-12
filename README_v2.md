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


