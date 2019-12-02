import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://yieqasktdngdap:ae5d27f49b650964142cb6b09e3bddc7f4e71334cbc83a7a052bf0b681a5df8d@ec2-54-225-173-42.compute-1.amazonaws.com:5432/d5fup55cdi35ms"

db = SQLAlchemy(app)

metadata = MetaData()
metadata.reflect(db.engine)#, only=['Yelp', 'Zomato'])

Base = automap_base(metadata=metadata)
Base.prepare()
# print('keys', Base.classes.keys())
yelp = Base.classes.Yelp
zomato= Base.classes.Zomato

yelp = Base.classes.Yelp
zomato= Base.classes.Zomato

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
