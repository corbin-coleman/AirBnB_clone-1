#!/usr/bin/python3
from models import *
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
