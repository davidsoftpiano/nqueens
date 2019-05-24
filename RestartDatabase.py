# RestartDatabase.py
# D.R 23/05/2019

# This script is used to restart the database in order to delete all the solutions previously calculated

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

###config.py###
# db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"
# DATABASE_URI = 'postgres+psycopg2://david:admin@localhost:5432/nqueens'
DATABASE_URI = "postgres+psycopg2://postgres:p4ssw0rd@172.17.0.2:5432/nqueens"
DATABASE_URI = "postgres+psycopg2://postgres:p4ssw0rd@db:5432/nqueens"
db = create_engine(DATABASE_URI)
base = declarative_base()

###models.py###
# Table that stores the N value and solutions number
class SolutionsNumber(base):
    __tablename__ = "solutions_number"
    id = Column(Integer, primary_key=True)
    n_value = Column(Integer)
    solutions_number = Column(Integer)


# Table that stores all the solutions
class Solutions(base):
    __tablename__ = "solutions"
    id = Column(Integer, primary_key=True)
    n_value = Column(Integer)
    column_values = Column(String)


# crud.py
Session = sessionmaker(db)
session = Session()
base.metadata.drop_all(db)
base.metadata.create_all(db)
print("[RestartDatabase]: Database restarted")
