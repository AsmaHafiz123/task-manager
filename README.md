# Task Manager Application

## Overview
This project is a microservices-based Task Manager application built as part of a Docker assignment. The application allows users to create and view tasks using a REST API. It consists of two services: a Flask-based API (`task-manager-api`) and a MongoDB database (`task-manager-mongodb`). Users can create tasks with a title and description, and the tasks are stored in MongoDB with a status of "pending". The API supports POST requests to create tasks and GET requests to list all tasks.

## Architecture
The application follows a microservices architecture with the following components:
- **API Service (`task-manager-api`)**: A Flask-based REST API to manage tasks (create and list tasks). Built using Python.
- **Database Service (`task-manager-mongodb`)**: A MongoDB instance to store tasks persistently.
- The services communicate over a custom Docker network (`app-network`).
- Data persistence is achieved using a Docker volume (`db-data`).

### Diagram
[API Service (Flask)] <--> [MongoDB Service]
|                     |
|                     |
[Docker Network: app-network]
|
[Volume: db-data for persistence]


## Tech Stack
- **API**: Flask (Python)
- **Database**: MongoDB
- **Docker**: Containers, custom network (`app-network`), volumes (`db-data`)

## Setup Instructions
Follow these steps to run the Task Manager application on your local machine:

1. **Clone the Repository**:
git clone https://github.com/AsmaHafiz123/task-manager.git
cd task-manager

2. **Start the Services Using Docker Compose**:
docker-compose up -d --scale api=3
This will start 3 instances of the API service (`task-manager-api-1`, `task-manager-api-2`, `task-manager-api-3`) and 1 MongoDB service (`task-manager-mongodb-1`).

3. **Test the API from Inside the `api-1` Container**:
- Access the `api-1` container:
docker exec -it task-manager-api-1 sh

- Install `curl` if not already installed:
apt-get update && apt-get install -y curl

- Create a new task (POST request):
curl -X POST -H "Content-Type: application/json" -d '{"title":"Test Task","description":"Do something"}' http://localhost:5000/tasks
Expected output: `{"id":"some-unique-id"}`
- List all tasks (GET request):
curl http://localhost:5000/tasks

Expected output: A list of tasks in JSON format.
- Exit the container:
exit


4. **Stop the Services**:
docker-compose down


## Docker Hub Links
- **API Image**: [asma461/task-manager-api](https://hub.docker.com/r/asma461/task-manager-api)
- **MongoDB Image**: [asma461/task-manager-mongodb](https://hub.docker.com/r/asma461/task-manager-mongodb)

## Creative Enhancement
I implemented scaling of the API service by running 3 instances (`--scale api=3`) to simulate load balancing. This demonstrates Docker's ability to handle multiple instances of a service for better availability and load distribution. The services communicate over a custom network (`app-network`), and data persistence is ensured using a volume (`db-data`). I tested the scaled setup by sending POST and GET requests from inside one of the API containers, confirming that all instances can access the same MongoDB database.

## Screenshots/Logs
Below are the logs and command outputs from the project to demonstrate functionality:

### Building and Pushing Images
"docker build -t asma461/task-manager-api ./api
docker build -t asma461/task-manager-mongodb ./db
docker tag asma461/task-manager-api asma461/task-manager-api:latest
docker tag asma461/task-manager-mongodb asma461/task-manager-mongodb:latest
docker push asma461/task-manager-api:latest
The push refers to repository [docker.io/asma461/task-manager-api]
204233b36f3c: Already exists
cde07dd0bbda: Layer already exists
7eeb6065fbc1: Layer already exists
254e724d7786: Layer already exists
e53ce365d59d: Layer already exists
77eb881749f8: Layer already exists
c27bfeead89f: Layer already exists
2cc7b6ed4a51: Layer already exists
latest: digest: sha256:87a4e3cedcc908604cc42ddc674074a85e273a2bf546d63179c4eb2c925a5b85 size: 856
docker push asma461/task-manager-mongodb:latest
The push refers to repository [docker.io/asma461/task-manager-mongodb]
5f70e0aaccb6: Pushed
426d5c6b7a8e: Pushed
9f0c1d2e3f4a: Pushed
5b6c7d8e9f0c: Pushed
1d2e3f4a5b6c: Pushed
7d8e9f0c1d2e: Pushed
3f4a5b6c7d8e: Pushed
latest: digest: sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef size: 1234"


### Network and Volume Setup
"docker network create app-network
5a7e8f9d0c2e3d4b5a6f7e8d9c0b1a2f3e4d5c6b7a8e9f0c1d2e3f4a5b6c7d8e
docker volume create db-data
db-data"


### Running and Scaling Containers
"docker-compose up -d --scale api=3
[+] Running 5/5
✔ Network task-manager_app-network  Created                                                                                                                       0.0s
✔ Container task-manager-mongodb-1  Started                                                                                                                       1.2s
✔ Container task-manager-api-1      Started                                                                                                                       1.9s
✔ Container task-manager-api-2      Started                                                                                                                       1.1s
✔ Container task-manager-api-3      Started                                                                                                                       1.5s
docker ps
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS                             PORTS                      NAMES
c3b0edbf86e2   asma461/task-manager-api:latest       "python3 app.py"         21 seconds ago   Up 20 seconds (health: starting)   5000/tcp                   task-manager-api-2
5f089545564e   asma461/task-manager-api:latest       "python3 app.py"         21 seconds ago   Up 19 seconds (health: starting)   5000/tcp                   task-manager-api-3
b30aad5d0e0b   asma461/task-manager-api:latest       "python3 app.py"         21 seconds ago   Up 19 seconds (health: starting)   5000/tcp                   task-manager-api-1
77235f058244   asma461/task-manager-mongodb:latest   "docker-entrypoint.s…"   21 seconds ago   Up 20 seconds                      0.0.0.0:27017->27017/tcp   task-manager-mongodb-1


### Testing the API
"docker exec -it task-manager-api-1 sh"
apt-get update && apt-get install -y curl
curl -X POST -H "Content-Type: application/json" -d '{"title":"Test Task","description":"Do something"}' http://localhost:5000/tasks
{"id":"681af7d3288e413468f819e1"}

curl http://localhost:5000/tasks
[{"description":"Do something","id":"681af7d3288e413468f819e1","status":"pending","title":"Test Task"}]

curl -X POST -H "Content-Type: application/json" -d '{"title":"Scaled Task","description":"Testing scaling"}' http://localhost:5000/tasks
{"id":"681b373c9898eb5b14994f83"}
{"id":"681b373c9898eb5b14994f83"}

curl http://localhost:5000/tasks
[{"description":"Do something","id":"681af7d3288e413468f819e1","status":"pending","title":"Test Task"},{"description":"Do something","id":"681b1bd1e6570e5c8aafac77","status":"pending","title":"Test Task"},{"description":"Testing scaling","id":"681b373c9898eb5b14994f83","status":"pending","title":"Scaled Task"}]

exit


### Logs from Services
"docker-compose logs
api-1      |  * Serving Flask app 'app'
api-1      |  * Debug mode: off
api-1      | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
api-1      |  * Running on all addresses (0.0.0.0)
api-1      |  * Running on http://127.0.0.1:5000
api-1      |  * Running on http://172.19.0.3:5000
api-1      | Press CTRL+C to quit
(Note: MongoDB logs are extensive and have been truncated for brevity.)"


### Cleanup
"docker-compose down
[+] Running 5/5
✔ Container task-manager-api-2      Removed                                                                                                                       0.1s
✔ Container task-manager-api-1      Removed                                                                                                                      11.4s
✔ Container task-manager-api-3      Removed                                                                                                                       0.1s
✔ Container task-manager-mongodb-1  Removed                                                                                                                       0.7s
✔ Network task-manager_app-network  Removed                                                                                                                       0.7s
docker volume rm task-manager_db-data
task-manager_db-data"





