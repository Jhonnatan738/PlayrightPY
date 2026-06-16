from playwright.sync_api import Page 

class diccionarioSteps:
    def __init__(self, page: Page):
        self.page = page

    def personalizar_step(valorVerificar:str):
        match valorVerificar.lower():
            case texto if "login-button" in texto:
                return "en el boton de inicio de sesion"
            case texto if "user-name" in texto:
                return "de usuario en el login"
            case texto if "password" in texto:
                return "de contraseña en el login"