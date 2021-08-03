from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from asyncio_db.utils import create_session


Base = declarative_base()
session = create_session()

class Packet(Base):
    __tablename__ = 'packets'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    timestamp = Column(DateTime)
    client_id = Column(String)

    def __str__(self):
            return self.packet

    @classmethod
    def add(cls, type, timestamp, client_id):
        pack = cls(type=type, timestamp=timestamp, client_id=client_id)
        session.add(pack)
        session.commit()
        return pack

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def filtered_by_client_id(cls, client_id):
        return session.query(cls).filter_by(client_id=client_id).all()


class DataPacket(Base):
    __tablename__ = 'data_packets'
    id = Column(Integer, primary_key=True)
    packet_id = Column(Integer, ForeignKey('packets.id'))
    data = Column(String)
    packet = relationship('Packet')

    @classmethod
    def add(cls, data, packet):
        data_packet = cls(data=data, packet=packet)
        session.add(data_packet)
        session.commit()
        return data_packet

class MultipartPacket(Base):
    __tablename__ = 'multipart_packets'
    id = Column(Integer, primary_key=True)
    start_packet_id = Column(Integer, ForeignKey('packets.id'))
    end_packet_id = Column(Integer, ForeignKey('packets.id'))
    start_packet = relationship('Packet', foreign_keys=[start_packet_id])
    end_packet = relationship('Packet', foreign_keys=[end_packet_id])



class MultipartData(Base):
    __tablename__ = 'multipart_data'
    id = Column(Integer, primary_key=True)
    mp_packet_id = Column(Integer, ForeignKey('multipart_packets.id'))
    packet_id = Column(Integer, ForeignKey('packets.id'))
    data = Column(String)
    idx = Column(Integer)
    packet = relationship('Packet')
    mp_packet = relationship('MultipartPacket')



