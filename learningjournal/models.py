from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)

class ObjectModel(Base):
    __tablename__ = 'foos'
    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    height = Column(Integer)
    volume = Column(Integer)

Index('object_index', ObjectModel.name, unique=True, mysql_length=255)



