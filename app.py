#Import dependencies.
import datetime as dt
import numpy as np
import pandas as pd
#Dependencies we need for SQLAlchemy.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#Dependencies we need for Flask.
from flask import Flask, jsonify

#Set up database.
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect database.
Base = automap_base()
Base.prepare(engine, reflect=True)

#Create a variable for each of the classes so that we can reference them later.
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a session link from Python to our database.
session = Session(engine)

#Define Flask app.
app = Flask(__name__)

#Define the welcome route to be the root.
@app.route("/")
#Add the routing information for each of the other routes.
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#Create Precipitation Route
@app.route("/api/v1.0/precipitation")
#Pull the Precipitation data with function
def precipitation():
    #Create query.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all() 
    #Format results into a JSON structured file.
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#Create Stations Route
@app.route("/api/v1.0/stations")
#Pull the Stations data with function.
def stations():
    #Create query.
    results = session.query(Station.station).all()
    #Convert results into a list and return as JSON
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
                   
#Create Temperature Observations route.
@app.route("/api/v1.0/tobs")
#Pull the Termperature Observations data.
def temp_monthly():
    #Calculate the data one year ago from the last date in the database.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Create query for the primary station for all temperature observations from previoue year.
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    #Unravel the results into a one-dimensional arry and convert that array into a list.
    temps = list(np.ravel(results))
    #Jsonify.
    return jsonify(temps=temps)

#Create the Statistics route.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#Pull the Statistics data with function.
def stats(start = None, end = None):
    #Create query.
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    #The asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures.
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    #Calculate the temperature minimum, average, and maximum with the start and end dates.
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)