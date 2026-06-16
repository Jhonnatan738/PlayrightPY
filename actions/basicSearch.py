import allure
from utils.core import BrowseTheWeb, Actor
from utils.dictionary import diccionarioSteps

class IngresarTexto:
    def __init__(self, campo_ingresar: str, termino_busqueda: str):
        self.termino_busqueda = termino_busqueda
        self.campo_ingresar = campo_ingresar

    @staticmethod
    def el_termino(campo_ingresar: str, termino_busqueda: str):
        return IngresarTexto(campo_ingresar, termino_busqueda)
    
    
    def perform_as(self, actor: Actor):
        with allure.step(f"El actor ingresara el valor correspondiente en el campo '{diccionarioSteps.personalizar_step(self.campo_ingresar)}'"):
            browser = actor.ability_to(BrowseTheWeb)
            page = browser.page
            page.fill(self.campo_ingresar, self.termino_busqueda)
            browser.take_screenshot("ingreso completado")