import allure
from playwright.sync_api import Page
from ui import login
from utils.core import Actor, BrowseTheWeb
from actions.basicSearch import IngresarTexto
from actions.selectIntems import darClick

@allure.feature("Búsqueda básica en Google")
def test_main(page: Page):
    jhonnatan = Actor("Jhonnatan").who_can(BrowseTheWeb(page))
    
    page.goto('https://www.saucedemo.com/')
    jhonnatan.ability_to(BrowseTheWeb).take_screenshot('pantalla_inicio')
    
    jhonnatan.attempts_to(IngresarTexto.el_termino(login.USERNAMEINPUT, 'standard_user'))
    jhonnatan.attempts_to(IngresarTexto.el_termino(login.PASSWORDINPUT, 'secret_sauce'))
    jhonnatan.attempts_to(darClick.alElemento(login.BUTTONLOGIN))