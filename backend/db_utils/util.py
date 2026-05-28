import sqlite3
import sqlalchemy as db
from pathlib import Path

# DB_PATH = 'map.db'
# BASE_DIR = Path(__file__).resolve().parent
engine = db.create_engine('sqlite:///risk_map.db')
metadata_obj = db.MetaData()

tract = db.Table(
    'tract',
    metadata_obj,
    db.Column('tract_id', db.String, primary_key=True),
    db.Column('state_abbr', db.String),
    db.Column('lat', db.Float),
    db.Column('lon', db.Float)
)

feature_prevalence = 