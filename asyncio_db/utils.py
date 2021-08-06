import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_env_vars():
    user = os.environ.get('USER')
    password = os.environ.get('PASSWORD')
    host = os.environ.get('HOST')
    db_name = os.environ.get('DB_NAME')
    return user, password, host, db_name


def create_engine_psql():
    user, password, host, db_name = get_env_vars()
    return create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}/{db_name}'
    )


def create_session():
    engine = create_engine_psql()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
