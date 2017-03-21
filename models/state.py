#!/usr/bin/python3
from models import *
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City")

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
