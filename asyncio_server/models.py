import os

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
db_name = os.environ.get('DB_NAME')

engine = create_engine(
    f'postgresql+psycopg2://{user}:{password}@{host}/{db_name}'
)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Packet(Base):
    __tablename__ = 'packets'
    id = Column(Integer, primary_key=True)
    packet = Column(String)

    def __str__(self):
            return self.packet

    @classmethod
    def add(cls, packet):
        pack = cls(packet=packet)
        session.add(pack)
        session.commit()
        return pack
