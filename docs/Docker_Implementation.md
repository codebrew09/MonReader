# Docker Implementation Procedure

## Overview

Docker was used to containerize the Flask-based Image-to-Audio application. The purpose of Docker is to package the application code, Python environment, dependencies, and configurations into a portable container.

By using Docker, the application can run consistently across different environments, including local machines and AWS EC2.

The Docker implementation process consists of:

1. Preparing the application files
2. Creating a Dockerfile
3. Creating a Docker image
4. Running the Docker container
5. Testing and managing the container


---

# 1. Project Structure Preparation

The project directory contains the required application files:

```
Project/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## File Description

| File | Description |
|------|-------------|
| app.py | Main Flask application |
| requirements.txt | Python package dependencies required by the application |
| Dockerfile | Instructions used to create the Docker image |
| .dockerignore | Files excluded during Docker image creation |


---

# 2. Create requirements.txt

The `requirements.txt` file contains all Python libraries required by the Flask application.

Example:

```txt
Flask
torch
transformers
Pillow
opencv-python
numpy
```

During the Docker build process, these dependencies are automatically installed inside the container environment.


---

# 3. Create Dockerfile

The Dockerfile defines the environment and instructions required to run the application.

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

### 1. Base Image

```dockerfile
FROM python:3.10-slim
```

Uses a lightweight Python 3.10 environment as the base image.


### 2. Working Directory

```dockerfile
WORKDIR /app
```

Creates `/app` as the working directory inside the Docker container.


### 3. Copy Dependency File

```dockerfile
COPY requirements.txt .
```

Copies the Python dependency list into the container.


### 4. Install Dependencies

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Installs all required Python packages inside the container.


### 5. Copy Application Files

```dockerfile
COPY . .
```

Copies the application source code into the Docker container.


### 6. Expose Application Port

```dockerfile
EXPOSE 5000
```

Defines port 5000, which is the default Flask application port used by the application.


### 7. Start Application

```dockerfile
CMD ["python", "app.py"]
```

Automatically starts the Flask application when the container runs.


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
- Improves build performance
- Prevents unnecessary files from entering the container


---

# 5. Build Docker Image

Navigate to the project directory:

```bash
cd <project-directory>
```

Build the Docker image:

```bash
docker build -t image-to-audio .
```


Explanation:

| Command | Purpose |
|---------|---------|
| docker build | Creates a Docker image |
| -t image-to-audio | Assigns a name to the image |
| . | Uses the current directory as the build context |


Verify the Docker image:

```bash
docker images
```


Example output:

```
REPOSITORY        TAG       IMAGE ID
image-to-audio    latest    xxxxxxxxx
```


---

# 6. Run Docker Container

Start the Docker container:

```bash
docker run -d -p 5000:5000 --name image_to_audio image-to-audio
```


Explanation:

| Parameter | Purpose |
|-----------|---------|
| -d | Runs container in background mode |
| -p 5000:5000 | Maps host port 5000 to container port 5000 |
| --name image_to_audio | Assigns container name |
| image-to-audio | Specifies the Docker image to run |


---

# 7. Verify Running Container

Check active containers:

```bash
docker ps
```


Example output:

```
CONTAINER ID   IMAGE             PORTS
xxxxxxxx       image-to-audio    0.0.0.0:5000->5000/tcp
```


To display all containers:

```bash
docker ps -a
```


---

# 8. Access the Application

The Flask application can be accessed through:

```
http://<public-ip>:5000
```

Example for AWS EC2:

```
http://<EC2-public-IP>:5000
```


The EC2 Security Group must allow inbound TCP traffic on port 5000.


---

# 9. Check Application Logs

View container logs:

```bash
docker logs image_to_audio
```


Logs are used to troubleshoot issues such as:

- Application startup failure
- Missing dependencies
- Runtime errors
- Model loading errors


---

# 10. Docker Container Management Commands


## Stop Container

```bash
docker stop image_to_audio
```


## Start Container

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
Create Docker Container
          |
          |
          v
Run Flask Application
          |
          |
          v
Access Application Through Browser
```


---

# 12. Summary

The Docker implementation successfully converted the Flask Image-to-Audio application into a portable container.

The complete workflow:

1. Prepare application files
2. Define Python dependencies
3. Create Dockerfile
4. Build Docker image
5. Run Docker container
6. Verify application operation
7. Deploy and access through browser

Docker simplifies deployment by ensuring the same application environment can be reproduced locally and on AWS EC2.
