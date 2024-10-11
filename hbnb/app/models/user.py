#!/usr/bin/python3
import uuid
import re
from datetime import datetime


class User:

    def __init__(self, first_name, last_name, email, password, is_admin=False):

        if first_name is None or last_name is None or email is None:
            raise ValueError("Attributes are required.")

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

# ============================ "first_name" Property with Getter and Setter

	@property
    def first_name(self):
        return self._first_name
    
	@first_name.setter
    def first_name(self, value):
		if len(value) <= 50:
			self._first_name = value.strip()
		else:
            raise ValueError("Invalid first name")

# ============================ "last_name" Property with Getter and Setter

    @property
    def last_name(self):
        return self._last_name
    
	@last_name.setter
    def last_name(self, value):
		if len(value) <= 50:
			self._last_name = value.strip()
		else:
        	raise ValueError("Invalid last name")

# ============================ "email" Property with Getter and Setter

	@property
    def email(self):
		return self._email
    
    @email.setter
    def email(self, value):
        """Setter for prop last_name"""
        # calls the method in the facade object
        from app.services import facade        # add a simple regex check for email format. Nothing too fancy.
        is_valid_email = len(value.strip()) > 0 and re.search("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", value)
        email_exists = facade.get_user_by_email(value.strip())
        if is_valid_email and not email_exists:
            self._email = value
        else:
            if email_exists:
                raise ValueError("Email already exists!")
			raise ValueError("Invalid email format!")

# ============================ "is_admin" Property with Getter and Setter

	@property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if isinstance(value, bool):
            self._is_admin = value
        else:
            raise ValueError("Invalid Value")

# ============================ # Save and Update Timestamp

	def save(self):
        self.update_at = datetime.now()
    
# ============================ Add Place to List

	def add_place(self, place):
        self.places.append(place)

# ============================ Add Review to List

	def add_review(self, review):
        self.reviews.append(review)
		
# ============================ Check if Email Exists (Static Method)

	@staticmethod
	def email_exists(email):
        pass

# ============================ Check if User Exists (Static Method)

	@staticmethod
    def user_exists(user):
        pass
