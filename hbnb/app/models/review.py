#!/usr/bin/python3
import uuid
from datetime import datetime
from app.models.user import User
from app.models.place import Place

class Review:
    def __init__(self, text, rating, place, user):
        if not text or not isinstance(text, str):
            raise ValueError("Text is required and must be a string.")
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5.")
        if not isinstance(place, Place) or not place.place_exists(place):
            raise ValueError("Invalid place.")
        if not isinstance(user, User):
            raise ValueError("Invalid user.")
        
        self.id = str(uuid.uuid4())
        self.text = text.strip()
        self.rating = rating
        self.place = place
        self.user = user
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

# ============================ Text Property with Getter and Setter

    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise ValueError("Text must be a string.")
        self._text = value.strip()

# ============================ Rating Property with Getter and Setter

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, value):
        if not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = value

# ============================ Place Property with Getter and Setter

    @property
    def place(self):
        return self._place
    @place.setter
    def place(self, value):
        if not isinstance(value, Place) or not Place.place_exists(value):
            raise ValueError("Invalid place.")
        self._place = value

# ============================ User Property with Getter and Setter

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise ValueError("Invalid user.")
        self._user = value

# ============================ Save Method

    def save(self):
        self.updated_at = datetime.now()
