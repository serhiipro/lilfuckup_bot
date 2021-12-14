from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///some_db.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

