import os

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from asyncio_db.utils import create_session


Base = declarative_base()
session = create_session()

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
