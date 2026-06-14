import allure
from actions.basicSearch import GoogleSearchPage

@allure.feature("Búsqueda básica en Google")
def test_main(page):
    page.goto('https://www.google.com')
    page.screenshot(path='example.png')
    search_page = GoogleSearchPage(page)
    search_page.realizar_busqueda_basica()