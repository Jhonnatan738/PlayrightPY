import allure
from utils.core import BrowseTheWeb, Actor

class IngresarTexto:
    def __init__(self, campo_ingresar: str, termino_busqueda: str):
        self.termino_busqueda = termino_busqueda
        self.campo_ingresar = campo_ingresar

    @staticmethod
    def el_termino(campo_ingresar: str, termino_busqueda: str):
        return IngresarTexto(campo_ingresar, termino_busqueda)
    
    
    @allure.step("El actor realiza una búsqueda básica del término requerido")
    def perform_as(self, actor: Actor):
        browser = actor.ability_to(BrowseTheWeb)
        page = browser.page
        page.fill(self.campo_ingresar, self.termino_busqueda)
        browser.take_screenshot("busqueda_completada")