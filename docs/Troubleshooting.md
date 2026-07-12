# Troubleshooting

During development and deployment, several common issues were encountered.

---

## Docker Container Exits Immediately

**Cause**

Application startup failed.

**Solution**

- Review container logs using:

```bash
docker logs <container_id>
```

- Verify the Dockerfile and startup command.

---

## Browser Shows "Refused to Connect"

**Possible Causes**

- Flask is not listening on `0.0.0.0`
- Port 5000 is not exposed
- Docker container is not running
- AWS Security Group does not allow inbound traffic on port 5000

---

## CPU Warning

```
Neither CUDA nor MPS are available.
```

This message indicates that GPU acceleration is unavailable.

The application automatically falls back to CPU inference, which is expected on most EC2 instances.

---

## EC2 Becomes Unresponsive

Large AI models require significant memory.

Possible solutions:

- Use a larger EC2 instance.
- Configure swap space.
- Monitor memory usage during inference.
