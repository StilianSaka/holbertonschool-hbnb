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

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, value):
		if len(value) <= 100:
			self._title = value.strip()
		else:
            raise ValueError("Invalid title")

	@property
	def description(self):
		return self._description
	
	@description.setter
	def description(self, value):
		self._description = value()

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, value):
		if isinstance(value, float) and value > 0:
			self._price = value
		else:
			raise ValueError("Price must be positive")
		
	@property
	def lat

	@property
	def owner(self, value):
		if isinstance(value, User):
			self._owner = owner
		else:
			raise ValueError("Invalid type")
		
	def save(self):
        self.update_at = datetime.now()

	def add_review(self, review):
        self.reviews.append(review)

	def add_amenity(self, amenity):
        self.amenities.append(amenity)

	@staticmethod
	def place_exists(place):
        pass