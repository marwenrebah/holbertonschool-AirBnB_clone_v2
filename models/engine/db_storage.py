#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Handles database connections and sessions for SQLAlchemy ORM."""

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the DBStorage class with a new SQLAlchemy session.
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )

        # drop all tables if the HBNB_ENV is equal to test
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all instances of a given class"""
        classes_to_query = [State, City, User, Place, Review, Amenity]
        if cls is None:
            obj = self.__session.query(State).all()
            for cls in classes_to_query:
                obj.extend(self.__session.query(cls).all())
        else:
            if isinstance(cls, str):
                cls = globals()[cls]  # Assuming cls is the name of the class
            obj = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in obj}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload objects that have been committed"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.remove()
