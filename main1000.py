from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


# Define alltodo as a shared state outside of the component
alltodo = ([])

# Define a function to insert data into MongoDB
def insert_data_to_mongodb(data):
    try:
        # Insert the data into the MongoDB collection
        collection.insert_one(data)
        print("Data inserted into MongoDB successfully!")
    except DuplicateKeyError as e:
        # Handle duplicate key error (if needed)
        print("Duplicate key error:", str(e))
    except Exception as e:
        # Handle other exceptions or errors here
        print("Error inserting data into MongoDB:", str(e))

@component
def MyCrud():
    # Creating state
    first_name, set_first_name = use_state("")
    Last_name, set_Last_name = use_state("")
    Username, set_Username = use_state("")
    Email, set_Email = use_state("")
    password, set_password = use_state("")
    newtodo = {}

    def mysubmit():
        newtodo["first_name"] = first_name
        newtodo["Last_name"] = Last_name
        newtodo["Username"] = Username
        newtodo["Email"] = Email
        newtodo["password"] = password
               
        # Call the function to insert data into MongoDB
        insert_data_to_mongodb(newtodo)
    alltodo.append(newtodo)
        # Push this to alltodo
        
        # You can also add error handling and validation
    list = []
    return html.div(
        {"style":
             {"padding": "50px", "display": "flex",
              "background_image": "url(https://reactpy.neocities.org/photo/wallpaperflare.com_wallpaper.jpg)",
              "background-size": "cover",
              "margin": "0px",
              "min-height": "700px",
              "min-width": "700px"}
         },
        ## creating form for submission
        html.form(
            # Heading
            {"on_submit": mysubmit},
            html.b(html.h1(
                {"style": {"font-family": "Arial", "font-size": "26px", "color": "LightCyan"}}
                , "ReactPy & Mongodb", )),
            html.br(),

            html.b(html.h2(
                {"style": {"font-family": "Arial", "font-size": "20px", "color": "LightCyan"}}
                , 'Sign-Up')),

            html.label(
                {"style": {"font-family": "Arial", "font-size": "14px", "color": "#e6fffa"}}
                , "First name"),
            html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "First name",
                    "value": first_name,
                    "on_change": lambda event: set_first_name(event["target"]["value"]),
                }
            ),
            html.br(),

            html.label(
                {"style": {"font-family": "Arial", "font-size": "14px", "color": "#e6fffa"}}
                , "Last name"),
            html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Last name",
                    "value": Last_name,
                    "on_change": lambda event: set_Last_name(event["target"]["value"]),
                }
            ),

            html.br(),
            html.p(""),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "14px", "color": "#e6fffa"}}
                , "Username"),
            html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Username",
                    "value": Username,
                    "on_change": lambda event: set_Username(event["target"]["value"]),
                }
            ),

            html.br(),
            html.p(""),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "14px", "color": "#e6fffa"}}
                , "Gmail"),
            html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Email",
                    "value": Email,
                    "on_change": lambda event: set_Email(event["target"]["value"]),
                }
            ),

            html.br(),
            html.p(""),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "14px", "color": "#e6fffa"}}
                , "Password"),
            html.br(),
            html.input(
                {
                    "type": "password",
                    "placeholder": "Password",
                    "value": password,
                    "on_change": lambda event: set_password(event["target"]["value"]),
                }
            ),

            html.br(),
            html.p(""),
            # creating submit button on form
            html.button(
                {
                    "type": "submit",
                },
                "Create an Account",
            ),
            # add a button
            html.button(
                {
                    "type": "reset",
                    "on_click": lambda event: set_first_name("") and set_Last_name("") and set_Username("") and set_Email("") and set_password(""),
                },
                "Reset",
            ),
        ),
        html.ul(list),
        html.img(
            {
                "src": "https://reactpy.neocities.org/photo/wallpaperflare.com_wallpaper.jpg",
                "class_name": "img-fluid",
                "style": {"width": "1000px", "height": "600px",
                          "justify_content": "right", "margin_right": "0px",
                          "margin_left": "10px", "margin_top": "20px", "margin_bottom": "20px"},
                "alt": "picture",
            }),
    )
app = FastAPI()
from pymongo import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://yasiru11:yasiru11@cluster1.otlcmjt.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri)
DB = client["reactpy69"]
collection = DB["practice1"]
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Configure ReactPy with FastAPI
configure(app, MyCrud)





