from  flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from config import data

app=Flask(__name__)
app.config.from_mapping(data)
manager=Manager(app)
db=SQLAlchemy(app)
from app import view
from app.data_db.models import HostAssets
