import re
from entities.user import User
from repositories.user_repository import UserRepository


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
        if UserRepository.find_by_username(self, username) != None:
            raise Exception(
                f"User with username {username} already exists"
            )

        if (re.match("^[a-z]{3,}$", username)):
            print("Ok")
        else:
            print("Virheellinen")
