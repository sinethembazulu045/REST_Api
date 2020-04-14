import psycopg2
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#engine = create_engine('postgresql+psycopg2://pguser:password@localhost/sql_alchem')
#engine.connect()
connection = psycopg2.connect(database="gps_heatmap", user="postgres", password="1234", host="localhost", port=5432)
connection.connect()