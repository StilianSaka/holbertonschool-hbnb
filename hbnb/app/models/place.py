#!/usr/bin/python3
import uuid
from datetime import datetime
from app.models.user import User

class Place:
    def __init__(self, title, description, price, latitude, longitude, owner):
        if title is None or latitude is None or longitude is None:
            raise ValueError("Attributes are required.")
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

# ============================ Title Property with Getter and Setter

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) <= 100:
            self._title = value.strip()
        else:
            raise ValueError("Invalid title")

# ============================ Description Property with Getter and Setter

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

# ============================ Price Property with Getter and Setter

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (float, int)) and value > 0:
            self._price = value
        else:
            raise ValueError("Price must be positive")

# ============================ Latitude Property with Getter and Setter

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if -90 <= value <= 90:
            self._latitude = value
        else:
            raise ValueError("Invalid value")

# ============================ Longitude Property with Getter and Setter

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if -180 <= value <= 180:
            self._longitude = value
        else:
            raise ValueError("Invalid value")

# ============================ Owner Property with Getter and Setter

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, User):
            self._owner = value
        else:
            raise ValueError("Invalid type")



    def save(self):
        self.updated_at = datetime.now()

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    @staticmethod
    def place_exists(place):
        pass
