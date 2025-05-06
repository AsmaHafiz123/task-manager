# Task Manager Microservices Application

## Description
A simple task management application allowing users to create, read, update, and delete tasks via a REST API. The application uses a Flask-based API and a MongoDB database, both containerized with Docker. Services communicate over a custom Docker network, and MongoDB data persists using a Docker volume.

## Use Case
Users can manage tasks (e.g., title, description, status) through HTTP requests (e.g., via `curl` or Postman). Ideal for personal or team task tracking.

## Architecture
- **Flask API**: Handles CRUD operations, connects to MongoDB.
- **MongoDB**: Stores task data.
- **Docker Network**: `app-network` for service communication.
- **Docker Volume**: `db-data` for MongoDB persistence.



## Tech Stack
- Flask (Python) for the API.
- MongoDB for the database.
- Docker for containerization.

## Docker Usage
- Containers: One for Flask, one for MongoDB.
- Network: Custom `app-network` for communication.
- Volume: Persistent storage for MongoDB.
- Multi-stage build: Optimize Flask image size.
- Healthcheck: Ensure Flask API is responsive.
 
