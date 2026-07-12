# Docker Implementation Procedure

## Overview

Docker was used to containerize the Flask-based Image-to-Audio application. The purpose of using Docker is to package the application, dependencies, and required environment into a portable container that can run consistently on different systems, including AWS EC2.

The Docker workflow consists of:

1. Preparing the application files
2. Creating a Dockerfile
3. Building a Docker image
4. Running the Docker container
5. Testing and managing the container


---

# 1. Project Structure Preparation

The project directory was organized as follows:

```
Project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── templates/
├── static/
└── models/
```

## File Description

| File | Description |
|------|-------------|
| app.py | Main Flask application |
| requirements.txt | Python package dependencies |
| Dockerfile | Instructions to build the Docker image |
| .dockerignore | Files excluded during image creation |
| templates/ | HTML templates |
| static/ | CSS, JavaScript, and images |
| models/ | Machine learning model files |


---

# 2. Create requirements.txt

The `requirements.txt` file contains all Python dependencies required by the application.

Example:

```txt
Flask
torch
transformers
Pillow
opencv-python
numpy
```

Docker uses this file to automatically install all required libraries during image creation.


---

# 3. Create Dockerfile

The Dockerfile defines how the application environment is created.

Example:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```


## Dockerfile Explanation

### Base Image

```dockerfile
FROM python:3.10-slim
```

Uses a lightweight Python 3.10 image as the base environment.


### Working Directory

```dockerfile
WORKDIR /app
```

Creates and sets `/app` as the working directory inside the container.


### Copy Dependencies

```dockerfile
COPY requirements.txt .
```

Copies the dependency list into the container.


### Install Dependencies

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Installs all required Python packages.


### Copy Application Files

```dockerfile
COPY . .
```

Copies the entire project into the container.


### Expose Application Port

```dockerfile
EXPOSE 5000
```

Defines port 5000 for Flask application access.


### Start Application

```dockerfile
CMD ["python", "app.py"]
```

Runs the Flask application when the container starts.


---

# 4. Create .dockerignore File

The `.dockerignore` file prevents unnecessary files from being copied into the Docker image.

Example:

```
.git
__pycache__
*.pyc
.env
```

Benefits:

- Reduces Docker image size
- Improves build speed
- Prevents unnecessary files from being included


---

# 5. Build Docker Image

Navigate to the project directory:

```bash
cd Project
```

Build the Docker image:

```bash
docker build -t image-to-audio .
```

Explanation:

- `docker build` creates a Docker image
- `-t image-to-audio` assigns the image name
- `.` uses the current directory as the build location


Verify the image:

```bash
docker images
```


Expected output:

```
REPOSITORY        TAG       IMAGE ID
image-to-audio    latest    xxxxxxxxx
```


---

# 6. Run Docker Container

Start the container:

```bash
docker run -d -p 5000:5000 --name image_to_audio image-to-audio
```


Explanation:

| Parameter | Purpose |
|-----------|---------|
| -d | Runs container in background mode |
| -p 5000:5000 | Maps host port to container port |
| --name | Assigns container name |
| image-to-audio | Docker image to run |


---

# 7. Verify Container Status

Check running containers:

```bash
docker ps
```

Example output:

```
CONTAINER ID   IMAGE             PORTS
xxxxxxxx       image-to-audio    0.0.0.0:5000->5000/tcp
```


To view all containers:

```bash
docker ps -a
```


---

# 8. Access the Application

The Flask application can be accessed through:

```
http://<server-ip>:5000
```

For local testing:

```
http://localhost:5000
```


---

# 9. Monitor Application Logs

To check application output and errors:

```bash
docker logs image_to_audio
```

Example:

```
Running on http://0.0.0.0:5000
```

Logs are useful for troubleshooting application startup failures.


---

# 10. Docker Container Management Commands

## Stop Container

```bash
docker stop image_to_audio
```


## Start Existing Container

```bash
docker start image_to_audio
```


## Restart Container

```bash
docker restart image_to_audio
```


## Remove Container

```bash
docker rm image_to_audio
```


## Remove Docker Image

```bash
docker rmi image-to-audio
```


---

# 11. Docker Deployment Workflow

```
Application Source Code
          |
          |
          v
Create Dockerfile
          |
          |
          v
Build Docker Image
          |
          |
          v
Run Docker Container
          |
          |
          v
Flask Application Running
          |
          |
          v
Access Through Browser
```


---

# 12. Summary

Docker provides a consistent deployment environment by packaging the Flask application, Python runtime, libraries, and configurations into a single container.

The final deployment process:

1. Prepare application files
2. Define dependencies
3. Create Dockerfile
4. Build Docker image
5. Run Docker container
6. Verify application availability
7. Monitor logs and manage containers

Docker allows the Image-to-Audio application to be easily deployed locally or on cloud platforms such as AWS EC2.
