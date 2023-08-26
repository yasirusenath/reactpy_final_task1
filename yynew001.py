from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = FastAPI()
app= Flask(__name__)

origins = ["http://0.0.0.0", "http://0.0.0.0:8080"]  # Update with your frontend URL

# Set up CORS

CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],

app = FastAPI()
#call mongodb 
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI
app=FastAPI()
uri = uri = "mongodb+srv://nibm:nibm@cluster1.otlcmjt.mongodb.net/"

client = MongoClient(uri)


db = client['reactpy2']


collection = db['react02']

# Checking  connection
try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB")
except Exception as e:
    print()
@app.route('/')
def index():
    return render_template('xx.html')

@app.route('/submit', methods=['POST'])
def submit():
    data1 = request.form.get('Login')
    data2 = request.form.get('Registration')

    # Create a document to insert into MongoDB
    document = {
        'field_from_form1': data1,
        'field_from_form2': data2
    }

    # Insert the document into MongoDB
    collection.insert_one(document)

    return redirect(url_for('index'))

if __name__ == '_main_':
    app.run(debug=True)
