# 🐳 Flask + Redis + Nginx | Dockerized Visit Counter

This is a simple web app designed to showcase container orchestration using **Docker** and **Docker Compose**. It consists of three services:

- **Nginx** – Load balancer and reverse proxy
- **Flask** – Backend application for handling requests
- **Redis** – Stores and tracks visit counts

All services run in their own Docker containers and communicate over a Docker network.

## 🧪 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mustafa914/Containers-challenge.git
cd Containers-challenge
```

### 2. Run the project

```bash
docker compose up --build
```

This command will:

- Build the Flask app image  
- Pull official Redis and Nginx images  
- Start all three containers and connect them via a Docker network

### 3. Open in your browser

Visit 👉 [http://localhost:8080](http://localhost:8080)

You should see a message like:

```
Hello! You've visited this page 3 times.
```

## 🌐 How It Works

When you visit `http://localhost:8080` in your browser:

1. The request goes to the **Nginx** container (acting as a reverse proxy).
2. Nginx forwards the request to the **Flask** app container.
3. The Flask app increments a counter stored in the **Redis** container.
4. The current visit count is returned to the user through Nginx.

All services are connected through a Docker network managed by **Docker Compose**.