# AWS EC2 Deployment

## Overview

After validating the application locally and inside a Docker container, the final step was deploying the application to Amazon Web Services (AWS) using an Ubuntu EC2 instance.

The objective was to host the application in the cloud and make it accessible from any browser using the EC2 instance's public IP address.

---

# Deployment Architecture

```
Developer Machine
        │
        ▼
Docker Image
        │
        ▼
AWS EC2 (Ubuntu)
        │
        ▼
Docker Container
        │
        ▼
Flask Application
        │
        ▼
Public Browser
```

---

# Prerequisites

Before deployment, ensure you have:

- AWS Account
- Ubuntu EC2 Instance
- SSH Key Pair (.pem)
- Docker Image exported from your local machine

---

# Step 1 – Launch an EC2 Instance

Create an Ubuntu EC2 instance.

Recommended configuration:

- Ubuntu Server 22.04 LTS
- t3.small or higher (recommended for ML applications)
- Allow inbound traffic:
  - SSH (22)
  - Custom TCP (5000)

---

# Step 2 – Connect to the EC2 Instance

From your local machine:

```bash
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>
```

Example:

```bash
ssh -i monreader.pem ubuntu@54.xxx.xxx.xxx
```

---

# Step 3 – Update Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

---

# Step 4 – Install Docker

Install Docker:

```bash
sudo apt install docker.io -y
```

Verify installation:

```bash
docker --version
```

Expected output:

```
Docker version xx.xx.x
```

---

# Step 5 – Enable Docker

Start Docker:

```bash
sudo systemctl start docker
```

Enable Docker on boot:

```bash
sudo systemctl enable docker
```

Verify Docker is running:

```bash
sudo systemctl status docker
```

---

# Step 6 – Allow Current User to Run Docker

Instead of using `sudo` every time:

```bash
sudo usermod -aG docker ubuntu
```

Apply the changes:

```bash
newgrp docker
```

Verify:

```bash
docker ps
```

---

# Step 7 – Transfer the Docker Image

Export the Docker image on your local machine:

```bash
docker save monreader > monreader.tar
```

Copy the image to EC2:

```bash
scp -i your-key.pem monreader.tar ubuntu@<EC2_PUBLIC_IP>:~
```

Example:

```bash
scp -i monreader.pem monreader.tar ubuntu@54.xxx.xxx.xxx:~
```

---

# Step 8 – Load the Docker Image

Inside EC2:

```bash
docker load < monreader.tar
```

Verify:

```bash
docker images
```

Example output:

```
REPOSITORY    TAG       IMAGE ID
monreader     latest    xxxxxxxxx
```

---

# Step 9 – Run the Docker Container

Run the application:

```bash
docker run -d \
-p 5000:5000 \
--name monreader \
monreader
```

Verify:

```bash
docker ps
```

Expected:

```
CONTAINER ID

STATUS

PORTS

0.0.0.0:5000->5000/tcp
```

---

# Step 10 – View Container Logs

If the application does not start correctly:

```bash
docker logs monreader
```

or

```bash
docker logs <container_id>
```

---

# Step 11 – Access the Application

Open a browser:

```
http://<EC2_PUBLIC_IP>:5000
```

The Flask application should now be accessible.

---

# Useful Docker Commands

View running containers:

```bash
docker ps
```

View all containers:

```bash
docker ps -a
```

View images:

```bash
docker images
```

Stop container:

```bash
docker stop monreader
```

Start container:

```bash
docker start monreader
```

Restart container:

```bash
docker restart monreader
```

Remove container:

```bash
docker rm monreader
```

Remove image:

```bash
docker rmi monreader
```

---

# Common Troubleshooting

## Browser shows "Refused to Connect"

Check:

```bash
docker ps
```

Check logs:

```bash
docker logs monreader
```

Verify Security Group:

- Port 5000
- TCP
- Source: 0.0.0.0/0

---

## Flask Only Listening on localhost

Ensure Flask starts with:

```python
app.run(host="0.0.0.0", port=5000)
```

---

## Container Stops Immediately

Inspect logs:

```bash
docker logs monreader
```

Most startup issues can be identified from the container logs.

---

## Check Docker Service

```bash
sudo systemctl status docker
```

Restart Docker if necessary:

```bash
sudo systemctl restart docker
```

---

# Learning Outcomes

Through this deployment process, the following skills were developed:

- Launching and managing AWS EC2 instances
- Connecting securely via SSH
- Installing and configuring Docker on Ubuntu
- Deploying Docker images to a cloud environment
- Running containerized Flask applications
- Configuring network access through Security Groups
- Troubleshooting cloud-based deployments
