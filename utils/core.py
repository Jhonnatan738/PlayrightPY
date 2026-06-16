import allure
from playwright.sync_api import Page

class BrowseTheWeb:
    def __init__(self, page: Page):
        self.page = page

    def take_screenshot(self, name: str):
        imagen_en_bytes = self.page.screenshot()
        allure.attach(
            imagen_en_bytes, 
            name=name, 
            attachment_type=allure.attachment_type.PNG
        )

class Actor:
    def __init__(self, name: str):
        self.name = name
        self.abilities = {}

    def who_can(self, ability):
        self.abilities[type(ability).__name__] = ability
        return self

    def ability_to(self, ability_class):
        return self.abilities[ability_class.__name__]

    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)