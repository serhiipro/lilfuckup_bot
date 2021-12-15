from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from utils.db.db_config import engine


Base = declarative_base(cls=DeferredReflection)


class MemesBase(Base):
    __tablename__ = 'memesbase'
    id = Column(Integer, primary_key=True)

    file_id = Column(String)
    file_unique_id = Column(String)
    associated_text = Column(String)

    def to_dict(self):
        return {
            'file_id ': self.name,
            'file_unique_id ': self.address,
            'associated_text': self.associated_text
        }


Base.prepare(engine)

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)