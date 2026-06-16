import allure
from utils.core import BrowseTheWeb, Actor

class darClick:
    def __init__(self, campo_ingresar: str):
        self.campo_ingresar = campo_ingresar

    @staticmethod
    def alElemento(campo_ingresar: str):
        return darClick(campo_ingresar)

    @allure.step("El usuario presionara el boton requerido")
    def perform_as(self, actor: Actor):
        browser = actor.ability_to(BrowseTheWeb)
        page = browser.page
        page.click(self.campo_ingresar)
        browser.take_screenshot("clickDado")