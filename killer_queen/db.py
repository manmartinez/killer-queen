import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ['DATABASE_URL'])
metadata = MetaData(bind=engine)
Session = sessionmaker(bind=engine)
