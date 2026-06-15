<h1 align="center"> Playwright & Python Automation Suite (Screenplay Pattern)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/playwright-%232EAD33.svg?style=for-the-badge&logo=playwright&logoColor=white" />
  <img src="https://img.shields.io/badge/pytest-%230A9EDC.svg?style=for-the-badge&logo=pytest&logoColor=white" />
  <img src="https://img.shields.io/badge/allure-%23D45A3C.svg?style=for-the-badge&logo=allure&logoColor=white" />
</p>

## Sobre el Proyecto

Este repositorio alberga un **framework de automatización avanzado e independiente**, diseñado bajo los más altos estándares de la ingeniería de software (*Clean Architecture*). En lugar del Page Object Model tradicional, este ecosistema ha sido estructurado pieza a pieza utilizando el patrón **Screenplay**, logrando pruebas modulares, altamente reutilizables y desacopladas de la interfaz técnica.

## Tech Stack

| Herramienta | Tecnología |
| :--- | :--- |
| **Lenguaje** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) v3.11+ |
| **Automatización** | ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white) (Async/Sync API) |
| **Test Runner** | ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) Framework |
| **Entorno/Gestión** | ![Conda](https://img.shields.io/badge/Conda-44A833?style=flat-square&logo=anaconda&logoColor=white) / Pip |
| **Estrategia** | Patrón de Diseño Screenplay (Actors, Tasks, Questions) |
| **Reporting** | Allure Framework (Pasos en lenguaje natural & evidencias vídeográficas/capturas) |

---

## Arquitectura del Framework (Screenplay Pattern)

La arquitectura rompe con el acoplamiento clásico del POM, organizando la suite alrededor de los conceptos del diseño guiado por el comportamiento del usuario:

* **Actores (`Actors`):** Los protagonistas de las pruebas. Cada actor cuenta con **Habilidades** (`Abilities`), como `BrowseTheWeb`, encapsulando el contexto del navegador de Playwright.
* **Tareas (`Tasks`):** Flujos de alto nivel que representan acciones del negocio (ej. `BuscarEnGoogle`). Se redactan emulando el lenguaje natural de los pasos de BDD/Gherkin.
* **Interacciones e Interfaz (`UI`):** Separación absoluta de selectores web (Locators), asegurando que los cambios en el DOM solo impacten un único archivo de configuración.
* **Preguntas (`Questions`):** La capa encargada de las aserciones. El actor interroga el estado de la aplicación de manera semántica, eliminando validaciones directas en el script principal.

## Escenarios de Automatización

- ✅ **Motores de Búsqueda y Navegación:** Validación de flujos de interacción rápidos y control de estados en el DOM.
- ✅ **Captura Dinámica de Pasos:** Registro cronológico de acciones interpretadas por el actor directamente en la bitácora de ejecución.
- ✅ **Gestión Aislada de Entornos:** Configuración robusta para prevenir la colisión de contextos virtuales en Python.

## Reportería & Evidencias con Allure

> [!IMPORTANT]
> **Documentación Viva:** Gracias al patrón Screenplay combinado con los decoradores de Allure, los reportes técnicos se transforman automáticamente en documentación legible para perfiles de negocio (Product Owners / QAs Manuales).

* **Pasos Detallados:** Cada tarea ejecutada por el actor se desglosa cronológicamente en la interfaz gráfica de Allure.
* **Evidencia Visual Interactiva:** El framework adjunta capturas de pantalla (`.png`) automáticas en puntos clave del flujo del actor.
* **Análisis de Estado:** Monitoreo gráfico de tiempos de respuesta, fallos e historial de suites directamente desde el servidor local de Allure.

---

## 🐳 Arquitectura y Ejecución en Docker

Para garantizar la portabilidad absoluta del framework y evitar el clásico *"en mi máquina sí funciona"*, el proyecto está estructurado para ejecutarse de manera aislada dentro de contenedores. Esto permite correr las pruebas en entornos headless de integración continua sin preocuparse por las dependencias del sistema operativo o las versiones locales de los navegadores.

El flujo de infraestructura utiliza las imágenes oficiales de Microsoft Playwright optimizadas para Python:

* **Aislamiento Total:** El contenedor empaqueta el entorno virtual, las variables de entorno, las dependencias de Python y los binarios de los navegadores (`chromium`, `firefox`, `webkit`).
* **Volúmenes Dinámicos:** Mapeo de la carpeta de resultados para extraer las evidencias (`allure-results/`) directamente a la máquina host tras finalizar la ejecución.

### Comandos de Infraestructura (Próxima Implementación)

1. **Construir la imagen del contenedor:**
   ```bash
   docker build -t playwright-screenplay-suite .