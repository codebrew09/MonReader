# AWS EC2 Deployment

## Overview

After validating the application locally and in Docker, the next step was deploying the container to an AWS EC2 instance.

This allows the application to be accessed from any web browser using the instance's public IP address.

---

## Deployment Workflow

```
Local Machine
      │
      ▼
Docker Image
      │
      ▼
AWS EC2 Instance
      │
      ▼
Docker Container
      │
      ▼
Public Web Application
```

---

## Deployment Steps

1. Launch an Ubuntu EC2 instance.
2. Configure the Security Group to allow HTTP traffic on port 5000.
3. Install Docker on the instance.
4. Transfer or load the Docker image.
5. Run the Docker container.
6. Access the application through the EC2 public IP.

Example:

```
http://<EC2_PUBLIC_IP>:5000
```

---

## AWS Services Used

- Amazon EC2
- Security Groups
- Public IP Address

---

## Key Learning Outcomes

- Provisioning cloud infrastructure
- Deploying Docker containers
- Configuring network access
- Hosting AI applications in the cloud
