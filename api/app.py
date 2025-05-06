from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB (use container name as hostname)
client = MongoClient(os.getenv("MONGO_URI", "mongodb://db-container:27017"))
db = client.taskdb
tasks = db.tasks

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [{"id": str(task["_id"]), "title": task["title"], "description": task["description"], "status": task["status"]}
                 for task in tasks.find()]
    return jsonify(task_list)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = {
        "title": data["title"],
        "description": data.get("description", ""),
        "status": data.get("status", "pending")
    }
    result = tasks.insert_one(task)
    return jsonify({"id": str(result.inserted_id)}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
