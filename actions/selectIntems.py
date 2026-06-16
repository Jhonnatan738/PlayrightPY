import allure
from utils.core import BrowseTheWeb, Actor
from utils.dictionary import diccionarioSteps

class darClick:
    def __init__(self, campo_seleccionar: str):
        self.campo_seleccionar = campo_seleccionar

    @staticmethod
    def alElemento(campo_seleccionar: str):
        return darClick(campo_seleccionar)

    def perform_as(self, actor: Actor):
        with allure.step(f"El actor dara click '{diccionarioSteps.personalizar_step(self.campo_seleccionar)}'"):
            browser = actor.ability_to(BrowseTheWeb)
            page = browser.page
            page.click(self.campo_seleccionar)
            browser.take_screenshot("click exitoso")
        

   