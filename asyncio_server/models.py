from sqlalchemy import Column, String, Integer, TypeDecorator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:///packets.sqlite'
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


Base.metadata.create_all(engine)