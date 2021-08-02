from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

from asyncio_db.utils import create_session


Base = declarative_base()
session = create_session()

class Packet(Base):
    __tablename__ = 'packets'
    id = Column(Integer, primary_key=True)
    packet = Column(String)
    timestamp = Column(DateTime)
    client_id = Column(String)

    def __str__(self):
            return self.packet

    @classmethod
    def add(cls, packet, timestamp, client_id):
        pack = cls(packet=packet, timestamp=timestamp, client_id=client_id)
        session.add(pack)
        session.commit()
        return pack

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def filtered_by_client_id(cls, client_id):
        return session.query(cls).filter_by(client_id=client_id).all()

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id' : self.id,
           'packet': self.packet,
           'timestamp': self.timestamp,
           'client_id': self.client_id
       }