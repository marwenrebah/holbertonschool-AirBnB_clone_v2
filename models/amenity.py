#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class representation
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False, overlaps="place_amenities")
