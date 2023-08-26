from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()

# Configure ReactPy
component(app)

# Set up CORS
origins = ["http://localhost", "http://localhost:3000"]  # Update with your frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@component
# ...

# ...

def MyCrud():
    ## Creating state
    alltodo = use_state([])
    name, set_name = use_state("")
    password, set_password = use_state("")
    gender, set_gender = use_state("male")  # Default value
    email, set_email = use_state("")  # New state variable for email
    phone, set_phone = use_state("")  # New state variable for phone number
    country, set_country = use_state("USA")  # Default country value

    def mysubmit(event):
        newtodo = {
            "name": name,
            "password": password,
            "gender": gender,
            "email": email,
            "phone": phone,
            "country": country,
        }

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        # Clear input fields after submission
        set_name("")
        set_password("")
        set_email("")
        set_phone("")
        login(newtodo)  # function call to login function using the submitted data

    # looping data from alltodo to show on the web
    list = [
        html.li(
            {},
            "Name: ", html.span(i["name"]),
            "Password: ", html.span(i["password"]),
            "Gender: ", html.span(i["gender"]),
            "Email: ", html.span(i["email"]),
            "Phone: ", html.span(i["phone"]),
            "Country: ", html.span(i["country"]),
        )
        for i in alltodo.value
    ]
    

    return html.div(
         {
          "style": {
            "padding": "10px",
            "background-image": "url('https://reactpy.neocities.org/photo/wallpaperflare.com_wallpaper.jpg/')",
            "width": "1000px",
            "height": "600px",
            "justify-content": "right",
            "margin-right": "0px",
            "margin-left": "10px",
            "margin-top": "20px",
            "margin-bottom": "20px",
        }
    },
        ## creating form for submission
        html.form(
            {"on_submit": mysubmit},
            html.h1("WELCOME TO FREE PARADISE"),
            html.h2("CHOOSE YOUR PARADISE RESORT"),
            html.h3("Give us your data"),
            # Name input field
            html.input(
                {
                    "type": "text",
                    "placeholder": "Name",
                    "on_change": lambda event: set_name(event["target"]["value"]),
                    "value": name,
                }
            ),
            # Password input field
            html.input(
                {
                    "type": "password",
                    "placeholder": "Password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                    "value": password,
                }
            ),   
            # Gender radio buttons
            html.label(
                {},
                "Gender:",
                html.input(
                    {
                        "type": "radio",
                        "name": "gender",
                        "value": "male",
                        "checked": gender == "male",
                        "on_change": lambda event: set_gender("male"),
                    },
                ),
                "Male",
            ),
            html.label(
                {},
                html.input(
                    {
                        "type": "radio",
                        "name": "gender",
                        "value": "female",
                        "checked": gender == "female",
                        "on_change": lambda event: set_gender("female"),
                    },
                ),
                "Female",
            ),
            # Email input field
            html.input(
                {
                    "type": "email",
                    "placeholder": "Email",
                    "on_change": lambda event: set_email(event["target"]["value"]),
                    "value": email,
                }
            ),
            # Phone number input field
            html.input(
                {
                    "type": "tel",
                    "placeholder": "Phone Number",
                    "on_change": lambda event: set_phone(event["target"]["value"]),
                    "value": phone,
                }
            ),
            # Country selection
            html.select(
                {
                    "on_change": lambda event: set_country(event["target"]["value"]),
                    "value": country,
                },
                html.option({"value": "Srilanka"}, "Srilanka"),
                html.option({"value": "USA"}, "USA"),
                html.option({"value": "Canada"}, "Canada"),
                html.option({"value": "UK"}, "UK"),
                html.option({"value": "Other"}, "Other"),
            ),
            # Creating submit button on form
            html.button(
                {
                    "type": "submit",
                    "on_click": event(lambda event: mysubmit(event), prevent_default=True),
                },
                "Submit",
            ),
        ),
        # Display the list of submitted data
        html.ul(list),
    )


# ...


    
app = FastAPI()

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI
app=FastAPI()
uri = uri = "mongodb+srv://nibm:nibm@cluster1.otlcmjt.mongodb.net/"

client = MongoClient(uri)

# Defining the database name
db = client['reactpy2']

# Defining the collection name
collection = db['react02']

# Checking the connection
try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB")
except Exception as e:
    print()


def login(login_data: dict):
    username = login_data["name"]
    password = login_data["password"]

    # Create a document to insert into the collection
    document = {"name": username, "password": password, "email": login_data["email"]}  # Include email in the document
    
    # Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id
    print(post_id)

    return {"message": "Login successful"}

configure(app, MyCrud)
