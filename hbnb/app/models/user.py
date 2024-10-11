#!/usr/bin/python3

class User:
    def __init__(self, first_name, last_name, email, password, is_admin):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        
    def update(self, first_name=None, last_name=None, email=None, password=None):

    	if first_name:
    		self.first_name = first_name

        if last_name:
			self.last_name = last_name

		if email:
			self.email = email
		
		if password:
			self.password = password
		
		if is_admin
			self.is_admin = is_admin
		return f"User {self.first_name} {self.last_name} is Updated"
		

	def full_name(self):
		return f"{self.first_name} {self.last_name}"