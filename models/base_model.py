#!/usr/bin/python3
import datetime
import uuid
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.now())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.now())

    """The base class for all storage objects in this project"""
    def __init__(self, *args, **kwargs):
        """initialize class object"""
        self.created_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        if len(args) > 0:
            if isinstance(args[0], dict):
                for k in args[0]:
                    setattr(self, k, args[0][k])
        """
        else:
            self.created_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
        """

    def save(self):
        """method to update self"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if ("_sa_instance_state" in dupe):
            dupe.pop("_sa_instance_state", None)
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe

    def delete(self):
        from models.__init__ import storage
        storage.delete(self)
