from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from environs import Env

env = Env()
env.read_env()

db_host = env.str("DB_HOST")
db_user = env.str("DB_USER")
db_password = env.str("DB_PASSWORD")
db_port = env.int("DB_PORT")  # Use int instead of str
db_name = env.str("DB_NAME")

# Construct the database URI
DATABASE_URI = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Creating database engine
engine = create_engine(DATABASE_URI)

# Creating a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
