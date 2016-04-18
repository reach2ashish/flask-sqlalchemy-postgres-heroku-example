from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

uri = os.environ.get('DATABASE_URL', 'postgres://wfgbweioifdejs:mnr1DloWvx9VJC3CJ-hLI2zgSx@ec2-79-125-126-192.eu-west-1.compute.amazonaws.com:5432/d98fdmm7p34k7d')
engine = create_engine(uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
					 autoflush=False,
					 bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  import Flasktest.models
  Base.metadata.create_all(bind=engine)
