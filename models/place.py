#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from os import getenv
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete")
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False)

    @property
    def reviews(self):
        """returns the list of Review instances
        with place_id equals to the current Place.id"""
        from models import storage
        l = []
        res = storage.all("Review")
        for v in res.values():
            if v["place_id"] == self.id:
                l.append(v)
        return l

    @property
    def amenities(self):
        """returns the list of Amenity instances based on the attribute amenity_ids"""
        from models import storage
        l = []
        res = storage.all("Amenity")
        for v in res.values():
            if v["amenity_ids"] == self.id:
                l.append(v)
        return l

    @amenities.setter
    def amenities(self, v):
        """adding an Amenity.id to the attribute amenity_ids"""
        from models.amenity import Amenity
        if isinstance(v, Amenity):
            self.amenity_ids.append(v.id)