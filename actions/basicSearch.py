import allure
from ui import login
from utils.core import BrowseTheWeb, Actor

class BuscarEnGoogle:
    def __init__(self, termino_busqueda: str):
        self.termino_busqueda = termino_busqueda

    @staticmethod
    def el_termino(termino_busqueda: str):
        return BuscarEnGoogle(termino_busqueda)

    @allure.step("El actor realiza una búsqueda básica del término ingresado")
    def perform_as(self, actor: Actor):
        browser = actor.ability_to(BrowseTheWeb)
        page = browser.page
        
        page.fill(login.SEARCH_TEXTAREA, self.termino_busqueda)
        
        browser.take_screenshot("busqueda_completada")
        
        page.press(login.SEARCH_TEXTAREA, 'Enter')