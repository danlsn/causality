from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load Environment Variables
from dotenv import load_dotenv
load_dotenv()
import os

LOCAL_DB_ENGINE_PATH = os.environ.get('LOCAL_DB_ENGINE_PATH')

engine = create_engine(LOCAL_DB_ENGINE_PATH, echo=True, future=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
