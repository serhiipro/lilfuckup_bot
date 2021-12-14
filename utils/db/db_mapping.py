from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from utils.db.db_config import engine


Base = declarative_base(cls=DeferredReflection)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    address = Column(String)
    email = Column(String)

    def to_dict(self):
        return {
            'name': self.name,
            'address': self.address,
            'email': self.address
        }


Base.prepare(engine)
