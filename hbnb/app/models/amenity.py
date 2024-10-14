#!/usr/bin/python3
import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name):
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = name


# ============================ Name Property with Getter and Setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) > 50:
            raise ValueError("Name cannot exceed 50 characters.")
        self._name = value.strip()

# ============================ Save Method

    def save(self):
        self.updated_at = datetime.now()
