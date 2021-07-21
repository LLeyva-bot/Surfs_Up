#Import dependencies.
from flask import Flask
#Create a new Flask app instance.
app = Flask(__name__)
#Define the root or starting point. 
@app.route('/')
#route function
def hello_world():
    return 'Hello world'



