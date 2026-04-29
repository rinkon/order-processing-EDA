import os
from dotenv import load_dotenv

load_dotenv()


DB_USER = os.environ['POSTGRES_USER']
DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['POSTGRES_DB']
DB_PORT = os.environ["POSTGRES_PORT"]
TOKEN_EXPIRY_IN_MINUTES = os.environ["TOKEN_EXPIRY_IN_MINUTES"]
SECRET_KEY = os.environ["TOKEN_EXPIRY_IN_MINUTES"]

print(DB_NAME)

