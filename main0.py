from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("YOUR_MONGODB_ATLAS_CONNECTION_STRING")
db = client["your_database_name"]
users_collection = db["users"]

@app.route("/register", methods=["POST"])
def register():
    # Extract user data from the request
    user_data = request.get_json()

    # Insert user data into the MongoDB collection
    users_collection.insert_one(user_data)

    return jsonify({"message": "User registered successfully"})

@app.route("/login", methods=["POST"])
def login():
    # Extract user login data from the request
    login_data = request.get_json()
    
    # Check if a user with the provided email exists in the database
    existing_user = users_collection.find_one({"email": login_data["email"]})
    
    # Check if the provided password matches the stored password (you should hash passwords for security)
    if existing_user and existing_user["password"] == login_data["password"]:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Login failed"})


if __name__ == "__main__":
    app.run()


