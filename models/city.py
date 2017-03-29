#!/usr/bin/python3
from os import getenv
from models import *
from models.state import State
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey("states.id"))
        name = Column(String(128), nullable=False)
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
