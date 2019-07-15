#importing Flask class from flask.py file
from flask import Flask



#creating an instance of the Flask class, in order to run this application
#name parameter will default to folder name
app = Flask(__name__)


#from the app folder, import the routes.py file, and startup at index
#will alway look for '/' as starting route 
from app import routes
