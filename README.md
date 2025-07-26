# Minimal Reproducible Example for Railway DNS Issue

## Context for This Repository

This repository was created to isolate and demonstrate a persistent deployment issue on the Railway platform.

**The Issue:**

My main production application is experiencing a critical outbound DNS failure (`[Errno -3] Lookup timed out`) when making network calls from within its Python (Gunicorn/eventlet) runtime.

Railway support has confirmed that basic DNS resolution **succeeds** from the container's interactive shell (using the `dig` command). However, this minimal Flask application proves that the exact same DNS lookup **consistently fails** when initiated by a standard Python process (`socket.gethostbyname`).

You can see a live demonstration of this failure on my deployment of this exact repository here:
**flask-gunicorn-app-production.up.railway.app**

This repository exists to provide a clear, reproducible example of this discrepancy.

**Seeking Help:**

If you have any insights into what could cause this difference between the shell environment and the Python runtime environment on Railway, your advice would be greatly appreciated. Please feel free to open an issue or reach out.

## Project Structure

```
.
├── test_app.py        # Minimal Flask application demonstrating the DNS issue
├── requirements.txt   # Project dependencies
└── runtime.txt        # Specifies Python 3.11.9 for Railway deployment
```

## Reproduction Steps

1. Deploy this repository to Railway
2. Access the deployed application
3. Observe the DNS resolution failure in the application logs
4. (Optional) SSH into the container and verify `dig` works from the shell
