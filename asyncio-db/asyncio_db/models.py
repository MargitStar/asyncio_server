from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from asyncio_db.utils import create_session


Base = declarative_base()
session = create_session()


class Packet(Base):
    __tablename__ = 'packets'
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    client_id = Column(Integer, nullable=False)
    packet = relationship('DataPacket', back_populates='data_packet', uselist=False)
    mp_packet = relationship('MultipartData', back_populates='packet')
    
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

    @classmethod
    def get_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()


class DataPacket(Base):
    __tablename__ = 'data_packets'
    id = Column(Integer, primary_key=True)
    packet_id = Column(Integer, ForeignKey('packets.id'), nullable=False)
    data = Column(String, nullable=False)
    data_packet = relationship('Packet', back_populates='packet')

    @classmethod
    def add(cls, data, packet):
        data_packet = cls(data=data, packet=packet)
        session.add(data_packet)
        session.commit()
        return data_packet

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()


class MultipartPacket(Base):
    __tablename__ = 'multipart_packets'
    id = Column(Integer, primary_key=True)
    start_packet_id = Column(Integer, ForeignKey('packets.id'), nullable=False)
    end_packet_id = Column(Integer, ForeignKey('packets.id'), nullable=False)
    start_packet = relationship('Packet', foreign_keys=[start_packet_id])
    end_packet = relationship('Packet', foreign_keys=[end_packet_id])
    mp_data = relationship('MultipartData', back_populates='mp_packet')

    @classmethod
    def add(cls, start_packet, end_packet):
        mp_data_packet = cls(start_packet=start_packet, end_packet=end_packet)
        session.add(mp_data_packet)
        session.commit()
        return mp_data_packet

    @classmethod
    def all(cls):
        return session.query(cls).all()


class MultipartData(Base):
    __tablename__ = 'multipart_data'
    id = Column(Integer, primary_key=True)
    mp_packet_id = Column(
        Integer,
        ForeignKey('multipart_packets.id'),
        nullable=False)
    packet_id = Column(Integer, ForeignKey('packets.id'), nullable=False)
    data = Column(String, nullable=False)
    idx = Column(Integer, nullable=False)
    packet = relationship('Packet', back_populates='mp_packet')
    mp_packet = relationship('MultipartPacket', back_populates='mp_data')

    @classmethod
    def add(cls, data, idx, packet, mp_packet):
        mp_data_packet = cls(data=data, idx=idx, packet=packet, mp_packet=mp_packet)
        session.add(mp_data_packet)
        session.commit()
        return mp_data_packet

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def filtered_by_idx(cls, mp_packet_id):
        return session.query(cls).filter_by(mp_packet_id=mp_packet_id).all()

    @classmethod
    def get_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
