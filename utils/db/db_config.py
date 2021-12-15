from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///utils/db/memes.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

