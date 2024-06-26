import allure
from dataclasses import dataclass
import requests

from helpers.faker import *
from helpers.user_api_urls import *


@dataclass
class Credentials:
    email: str = ''
    password: str = ''
    name: str = ''


class User:
    def __init__(self):
        self.user_credentials: Credentials = None
        self.access_token: str = None
        self.refresh_token: str = None

    @staticmethod
    def generate_user_credentials() -> Credentials:
        return Credentials(
            email=generate_email(),
            password=generate_password(),
            name=generate_username(),
        )

    def get_email(self):
        return self.user_credentials.email

    def get_password(self):
        return self.user_credentials.password

    def get_name(self):
        return self.user_credentials.name

    def get_user_credentials(self) -> Credentials:
        return self.user_credentials

    @allure.step('Создание пользователя: POST /api/auth/register')
    def create_user(self, email: str = '', password: str = '', name: str = ''):
        if not email and not password and not name:
            self.user_credentials = self.generate_user_credentials()
        else:
            self.user_credentials = Credentials(email, password, name)

        return requests.post(f"{BASE_URL}{CREATE_USER}", json=self.user_credentials.__dict__)

    @allure.step('Удаление пользователя: DELETE /api/auth/user')
    def delete_user(self, access_token: str = None):
        token = access_token if access_token else self.access_token
        return requests.delete(f"{BASE_URL}{DELETE_USER}", headers={"Authorization": token})

    def logout_user(self):
        return requests.post(f"{BASE_URL}{LOGOUT_USER}", json={"token": self.refresh_token})
