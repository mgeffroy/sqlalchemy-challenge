#Import dependencies including  flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask , jsonify


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect =True)

# Save reference to the table

Station = Base.classes.station
Measurement = Base.classes.measurement


# Flask setup 
# Create an app, being sure to pass _name_
app = Flask(__name__)

#Define routes 
#Homepage route 
## Homepage
@app.route("/")
def home():
    print("Server received request for Home")
    return (
      f"Hi! This is the Climate App!<br/><br/>"
      f"These are the available routes:<br/>"
      f"/api/v1.0/precipitation<br/>"
      f"/api/v1.0/stations<br/>"
      f"/api/v1.0/tobs<br/>"
      f"/api/v1.0/temp/start/end<br/>"
       
       )

#Make precipitation part 
@app.route("/precipitation")
def precipitation():
  return(
  )

@app.route("/stations")
def stations():
  return(
  )

@app.route("/tobs")
def tobs():
  return(
  )

@app.route("/temp")
def precipitation():
  return(
  )


if __name__ == "__main__":
    app.run(debug=True)