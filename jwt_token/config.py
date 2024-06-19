import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class EnvVariables:
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER = os.getenv("MYSQL_SERVER")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DB = os.getenv("MYSQL_DB")
