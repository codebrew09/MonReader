# Docker Implementation

## Why Docker?

Docker packages the application and its dependencies into a portable container, ensuring consistent behavior across different environments.

Benefits include:

- Environment consistency
- Simplified deployment
- Dependency isolation
- Easy application distribution

---

## Docker Workflow

```
Application
      │
      ▼
Dockerfile
      │
      ▼
Docker Image
      │
      ▼
Docker Container
```

---

## Build the Docker Image

```bash
docker build -t monreader .
```

---

## Run the Container

```bash
docker run -p 5000:5000 monreader
```

The application can then be accessed at:

```
http://localhost:5000
```

---

## Useful Docker Commands

```bash
docker images
docker ps
docker logs <container_id>
docker stop <container_id>
docker rm <container_id>
```

---

## Key Learning Outcomes

- Building Docker images
- Running containers
- Managing Docker resources
- Preparing applications for cloud deployment
