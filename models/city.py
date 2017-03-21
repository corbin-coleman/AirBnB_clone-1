#!/usr/bin/python3
from models import *
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"))
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
