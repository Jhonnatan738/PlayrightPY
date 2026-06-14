import allure

class GoogleSearchPage:
    def __init__(self, page):
        self.page = page

    @allure.step("Realizando una búsqueda básica en Google")
    def realizar_busqueda_basica(self):
        self.page.fill('textarea[id="APjFqb"]', 'Playwright')
        self.allurePicture('search_filled.png')
        self.page.press('textarea[id="APjFqb"]', 'Enter')

    def allurePicture(self, picture_path):
        self.page.screenshot(path=picture_path)
        allure.attach.file(
            picture_path, 
            name=picture_path, 
            attachment_type=allure.attachment_type.PNG
        )