#!/usr/bin/python3
from os import environ
from models.state import State
from models.user import User
from models.city import City
from models.place import Place, PlaceAmenity
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None
    classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def __init__(self):
        user = environ.get('HBNB_MYSQL_USER')
        passwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        database = environ.get('HBNB_MYSQL_DB')
        mysql = "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host,
                                                     database)
        self.__engine = create_engine(mysql)

    def all(self, cls=None):
        db_store = {}
        if cls and cls in self.classes:
            for obj in self.__session.query(eval(cls)):
                db_store.update({obj.id: obj})
        elif cls is None:
            for class_name in self.classes:
                for obj in self.__session.query(eval(class_name)):
                    db_store.update({obj.id: obj})
        return(db_store)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        self.__session.remove()
