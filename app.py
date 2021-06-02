#Import dependencies including  flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask , jsonify


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

session = Session(engine)
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
        f"/api/v1.0/2010-01-01<br/>"
        f"/api/v1.0/2010-01-01/2017-08-18<br/>"
    )


    if __name__ == "__main__":
        app.run(debug=True)


