import flet as ft 
from pages.authentication.login import Login  
from pages.authentication.signup import Signup
from pages.dashboard.test import UIPage


class Router:

    def __init__(self, page):
        self.page = page

        self.routes = {
            "pages/authentication/login" : Login(page),
            "pages/authentication/signup": Signup(page),
            "pages/dashboard/test": UIPage(page)
        }
        self.body = ft.Container(content=self.routes['pages/authentication/login'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()




