#!/usr/bin/python3
from os import environ
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def init(self):
        user = environ.get('HBNB_MYSQL_USER')
        passwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        database = environ.get('HBNB_MYSQL_ENV')
        mysql = "mysql+mysqldb://{}:{}@{}/{}".format(passwd, user, host,
                                                     database)
        self.__engine = create_engine(mysql)
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        db_store = {}
        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        if cls and cls in classes:
            for obj in self.__session.query(cls):
                db_store.update({obj.id: obj})
        elif cls is None:
            for class_name in classes:
                for obj in self.__session.query(class_name):
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
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
