#!/usr/bin/python3
from os import getenv
from models import *
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey("places.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        text = Column(String(1024), nullable=False)
    else:
        place = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
