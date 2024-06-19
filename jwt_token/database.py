from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import EnvVariables

# Extract variables
MYSQL_USER = EnvVariables.MYSQL_USER
MYSQL_PASSWORD = EnvVariables.MYSQL_PASSWORD
MYSQL_SERVER = EnvVariables.MYSQL_SERVER
MYSQL_PORT = EnvVariables.MYSQL_PORT
MYSQL_DB = EnvVariables.MYSQL_DB

# Construct database URL
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create all tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
