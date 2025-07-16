from ..utilities.webdriver_listener import WebDriverListener
from ..utilities.webdriver_extended import WebDriverExtended
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:

    @staticmethod
    def get_driver(config) -> WebDriverExtended:

        if config["browser"] == "chrome":
            options = ChromeOptions()
            options.add_argument("start-maximized")

            if config["headless_mode"]:
                options.add_argument("--headless=new")

            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=options)

        elif config["browser"] == "firefox":
            options = FirefoxOptions()
            if config["headless_mode"]:
                options.headless = True
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()

        elif config["browser"] == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("start-maximized")

            if config["headless_mode"]:
                options.add_argument("--headless=new")

            # options.add_experimental_option("detach", True)
            # driver = webdriver.Edge(options=options)
            service = EdgeService(EdgeChromiumDriverManager(cache_valid_range=30).install())
            driver = webdriver.Edge(service=service, options=options)

        else:
            raise Exception("Provide valid browser name")

        return WebDriverExtended(driver, WebDriverListener(), config)




