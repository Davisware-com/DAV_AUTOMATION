from ..utilities.webdriver_listener import WebDriverListener
from ..utilities.webdriver_extended import WebDriverExtended
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")

            if config["headless_mode"]:
                options.add_argument("--headless=new")

            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")

            if config["headless_mode"]:
                options.headless = True

            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)

        elif config["browser"] == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("start-maximized")
            options.use_chromium = True

            if config["headless_mode"]:
                options.headless = True
                options.add_argument('disable-gpu')

            driver_path = EdgeChromiumDriverManager().install()
            service = EdgeService(driver_path)
            driver = webdriver.Edge(service=service, options=options)

        else:
            raise Exception("Provide valid browser name")

        return WebDriverExtended(driver, WebDriverListener(), config)
