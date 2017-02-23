from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Notebook(Base):
    __tablename__ = 'notebook'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


class Card(Base):
    __tablename__ = 'card'

    id = Column(Integer, primary_key=True)
    term = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    tag = Column(String(250))
    notebook_id = Column(Integer, ForeignKey('notebook.id'))
    notebook = relationship(Notebook)

    @property
    def serialize(self):
        return {
            'term': self.term,
            'description': self.description,
            'tag': self.tag,
            'id': self.id,
        }


engine = create_engine('sqlite:///notecards.db')

Base.metadata.create_all(engine)









