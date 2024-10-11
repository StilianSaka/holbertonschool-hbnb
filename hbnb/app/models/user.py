#!/usr/bin/python3

class User:
    def __init__(self, first_name, last_name, email, password, is_admin):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = is_admin

        def register_user(self):
            # Registration logic here
        return f"User {self.full_name()} registered."

    def update_user_info(self, first_name=None, last_name=None, email=None, password=None):

        if first_name:
            self.first_name = first_name

        if last_name:
            self.last_name = last_name

        if email:
            self.email = email

        if password:
            self.password = password

        if is_admin is not None:
            self.is_admin = is_admin
        return f"The User {self.full_name()} updated."

        def delete_user(self):
            return f"The user {self.first_name} {self.last_name} is deleted."

        def list_user_info(self):
            return f"The user info is: {self.first_name}, {self.last_name}, {self.email}, {self.password}"

        def full_name(self):
            return f" The user fullname is: {self.first_name}, {self.last_name}"


if __name__ == "__main__":
    user = User("Jane", "Doe", "jane.doe@example.com", "securepassword", False)
    print(user.register())
    print(user.list())
    print(user.update_user_info(first_name="Janet", is_admin=True))
    print(user.list_user_info())
    print(user.delete_user())
