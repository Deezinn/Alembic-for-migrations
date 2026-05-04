import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class PostgresKey(BaseModel):
    key: str

    @staticmethod
    def load_key():
        url_database = os.getenv('url_database')

        if url_database:
            return url_database

        return 'sqlite:///../estudo.db'

url = PostgresKey(key=PostgresKey.load_key()).model_dump()
