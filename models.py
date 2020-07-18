import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('sqlite:///database.db', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    google_id = sqlalchemy.Column(sqlalchemy.String)
    location = sqlalchemy.Column(sqlalchemy.String)
    sex = sqlalchemy.Column(sqlalchemy.String)
    start_year = sqlalchemy.Column(sqlalchemy.Integer)
    phone_number = sqlalchemy.Column(sqlalchemy.String)
    height = sqlalchemy.Column(sqlalchemy.Integer)
    weight = sqlalchemy.Column(sqlalchemy.Integer)
    aura = sqlalchemy.Column(sqlalchemy.Boolean)
    events = sqlalchemy.relationship("Event", back_populates="user")
class Event(Base):
    __tablename__ = 'event'
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('user.id'))
    user = sqlalchemy.relationship("User", back_populates="events")
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    pain_intensity = sqlalchemy.Column(sqlalchemy.Integer)
    start_time = sqlalchemy.Column(sqlalchemy.DATETIME)
    end_time = sqlalchemy.Column(sqlalchemy.DATETIME)
    previous_night_sleep = sqlalchemy.Column(sqlalchemy.Float)
    trigger = sqlalchemy.relationship("Trigger")
class Trigger(Base):
    __tablename__ = 'trigger'
    event = sqlalchemy.relationship("Event")
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    category = sqlalchemy.Column(sqlalchemy.String)

class Interventions(Base):
    __tablename__ = 'trigger'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    category = sqlalchemy.Column(sqlalchemy.String)

class Therapies(Base):
    __tablename__ = 'trigger'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    category = sqlalchemy.Column(sqlalchemy.String)

class Sympotms(Base):
    __tablename__ = 'trigger'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    category = sqlalchemy.Column(sqlalchemy.String)

Base.metadata.create_all(engine)
