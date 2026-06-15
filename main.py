import allure
from playwright.sync_api import Page
from utils.core import Actor, BrowseTheWeb
from actions.basicSearch import BuscarEnGoogle

@allure.feature("Búsqueda básica en Google")
def test_main(page: Page):
    jhonnatan = Actor("Jhonnatan").who_can(BrowseTheWeb(page))
    
    page.goto('https://www.google.com')
    jhonnatan.ability_to(BrowseTheWeb).take_screenshot('pantalla_inicio')
    
    jhonnatan.attempts_to(
        BuscarEnGoogle.el_termino('Playwright')
    )