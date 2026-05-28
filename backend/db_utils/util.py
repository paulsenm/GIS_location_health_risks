import sqlite3
#import sqlalchemy as db
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

db = SQLAlchemy()
# DB_PATH = 'map.db'
# BASE_DIR = Path(__file__).resolve().parent
engine = db.create_engine('sqlite:///risk_map.db')
metadata_obj = db.MetaData()

class Tract(db.Model):
    __tablename__= 'tract'
    db.Column('tract_id', db.String, primary_key=True)
    db.Column('state_abbr', db.String)
    db.Column('lat', db.Float)
    db.Column('lon', db.Float)


class TractFeaturePrevalence(db.Model):
    __tablename__ = 'tract_feature_prevalence'    
    db.Column('id', db.Integer, primary_key=True)
    db.Column('tract_id', db.String, db.ForeignKey('tract.tract_id'), nullable = False)
    db.Column('feature_name', db.String)
    db.Column('feature_prevalence', db.Float)


