from flask import Flask
from printColors import *
import json
import os
import logging
import buttonControl
import jsCode
import textBox

def createPage(text, size=20):
    title = text
    input_box = textBox.createTextInputConnection()
    button = buttonControl.createButtonConnection("Click Here", size)
    script = jsCode.createRedirectScript()
    
    return title + input_box + button + script

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s|%(funcName)s|%(levelname)s|%(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()          # Also log to the console
    ]
)

try:
    with open("config.json") as config:
        permissions_list = json.load(config)
        permissions_set = set(permissions_list)
except FileNotFoundError:
    logging.critical("Error: Config file missing")

app = Flask(__name__)
@app.route("/")
def homePage():
    try:
        logging.info("The user has reached the home page")
        text_title = printBlue("If you want to connect, you need enter your name.")
        return createPage(text_title)
    except Exception as e:
        logging.critical(f"Error: {e}")

@app.route("/login/<name>")
def connect(name):
    try:
        logging.info(f"The user has accessed the lpgin with name {name}")
        if name in [perm.lower() for perm in permissions_set]:
            logging.info(f"Name {name} exists in list, access granted.")
            response = printGreen(f"{name.capitalize()} Welcome to my system!")
        else:
            logging.warning(f"Name {name} does not exists in list, access denied.")
            response = printRed("Access Denied")
        return createPage(response)
    except Exception as e:
        logging.critical(f"Error: {e}")

@app.route("/addNema")
def pageAddNema():
    try:
        response= "If you want to register, you need to add /(your name) in the URL"
        response_example = "Example: http://localhost/addNema/david" 
        logging.info("The user has reached the page 'addNema'")
        return printBlue(response,30)+printBlue(response_example,20)
    except Exception as e:
        logging.critical(f"Error: {e}")

@app.route("/addNema/<name>")
def addNema(name):
    try:
        logging.info("The user tried to connect")
        if name in [perm.lower() for perm in permissions_set]:
            logging.warning(f"The username {name.capitalize()} already exists!")
            response = printRed(f"The username {name.capitalize()} already exists!")
        else:
            permissions_set.add(name.lower())
            with open("config.json", "w") as json_file:
                json.dump(list(permissions_set), json_file, indent=4)
            logging.info(f"The name has been successfully added")
            response = printGreen("The name has been successfully added")
        return response
    except Exception as e:
        logging.critical(f"Error: {e}")



if __name__ == "__main__":
    app.run(host=os.environ.get("HOST_IP"), port=80)
