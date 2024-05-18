#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base
from os import getenv
from models.base_model import BaseModel
from models.city import City
import models


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:

        @property
        def cities(self):
            """returns the list of City instances"""
            instance_list = []
            for ins in models.storage.all(City).values():
                if ins.state_id == self.id:
                    instance_list.append(ins)
            return instance_list
