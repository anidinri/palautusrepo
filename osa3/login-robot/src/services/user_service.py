"""jotain"""

import re
import sys
import os


from entities.user import User
from repositories.user_repository import UserRepository

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))




class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    """jotain"""
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        """jotain"""
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")
            
        

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )


        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        try:
            self.check_credentials(username, password)
            raise Exception(f"User with username {username} already exists")
        except AuthenticationError:
            # This means the username doesn't exist or password is incorrect
            # Continue with user creation or other logic
            pass
        except UserInputError:
            # This means either username or password was missing
            raise Exception("Username and password are required")

        if (re.match("^[a-z]{3,}$", username)):
            print("Valid username")
        else:
            raise UserInputError("Invalid username")

        if (re.match("^[a-z]{8,}\d+$", password)):
            (print("Valid password"))
        else:
            raise UserInputError("Invalid password")

        
        
    
