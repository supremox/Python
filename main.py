import sys
sys.dont_write_bytecode = True

import flet as ft
from router import Router

def main(page: ft.Page):
    
    myRouter = Router(page)
    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )    
    page.go("pages/authentication/login")
       
ft.app(target=main, assets_dir="assets")
