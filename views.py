import sqlalchemy.orm
from models import engine, User

Session = sqlalchemy.orm.sessionmaker(bind=engine)

def add_new_user(first_name, last_name):
    session = Session()
    new_user = User(first_name=first_name, last_name=last_name, location='90211')
    session.add(new_user)
    session.commit()
