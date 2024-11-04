import uuid
from datetime import datetime

class Amenity:
    # id = None
    # name = ""
    # description = ""
    # created_at = None
    # updated_at = None

    def __init__(self, name, description):
        if name is None or description is None:
            raise ValueError("Required attributes not specified!")

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = name
        self.description = description

    # --- Getters and Setters ---
    @property
    def name(self):
        """ Returns value of property name """
        return self._name

    @name.setter
    def name(self, value):
        """Setter for prop name"""
        # ensure that the value is up to 50 characters after removing excess white-space
        is_valid_name = 0 < len(value.strip()) <= 50
        if is_valid_name:
            self._name = value.strip()
        else:
            raise ValueError("Invalid name length!")

    @property
    def description(self):
        """ Returns value of property description """
        return self._description

    @description.setter
    def description(self, value):
        """Setter for prop description"""
        self._description = value

    # --- Methods ---
    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Convert Amenity object to dictionary """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def update(self, data):
        """ Update Amenity attributes from a dictionary """
        from app.services.facade import HBnBFacade
        facade = HBnBFacade()
        
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
        facade.update_amenity(self.id, data)
