from fastapi import FastAPI, Form

app = FastAPI()

# MongoDB Atlas connection information
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI
app=FastAPI()
uri = "mongodb+srv://username:password@cluster1.otlcmjt.mongodb.net/"
client = MongoClient(uri)

# Define the database and collection
db = client['reactpy02']
collection = db['reactpy_assignment']

@app.post('/submit')
async def submit_form(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    # Create a user document
    user_data = {
        'username': username,
        'email': email,
        'password': password
    }

    # Insert the user data into the MongoDB collection
    result = collection.insert_one(user_data)

    if result.acknowledged:
        return {"message": "User data submitted successfully"}
    else:
        return {"message": "Failed to submit user data"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
