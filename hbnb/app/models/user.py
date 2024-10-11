#!/usr/bin/python3

class User:
    def __init__(self, first_name, last_name, email, password, is_admin):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

	def register(self):
		return f"The user {self.name} {self.last_name} is registered."
        
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
		
		

	def delete_user(self):
		return f"The user {self.first_name} {self.last_name} is deleted."

	def list_user_info(self):
		return f"The user info is: {self.first_name}, {self.last_name}, {self.email}, {self.password}"

	def full_name(self):
		return f" The user fullname is: {self.first_name}, {self.last_name}"
	