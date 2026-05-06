from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from key import url

engine: Engine = create_engine(
    url=url['key']
)
