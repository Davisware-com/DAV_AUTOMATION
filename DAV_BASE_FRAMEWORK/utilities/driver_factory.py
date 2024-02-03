from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from DAV_BASE_FRAMEWORK.utilities.webdriver_listener import WebDriverListener
from msedge.selenium_tools import EdgeOptions, Edge
from DAV_BASE_FRAMEWORK.utilities.webdriver_extended import WebDriverExtended


class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            if config["chrome_driver_manager"] is True:
                driver = WebDriverExtended(
                    webdriver.Chrome(ChromeDriverManager().install(), options=options),
                    WebDriverListener(), config
                )
                return driver
            else:
                driver = WebDriverExtended(
                    webdriver.Chrome(executable_path='C:/Users/BHARGAV.PULIKONDA/Drivers/chromedriver-win64'
                                                     '/chromedriver.exe', options=options),
                    WebDriverListener(), config
                )
                return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtended(
                webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options),
                WebDriverListener(), config
            )
            return driver
        elif config["browser"] == "edge":
            options = EdgeOptions()
            options.add_argument("start-maximized")
            options.use_chromium = True
            if config["headless_mode"] is True:
                options.headless = True
            driver_path = EdgeChromiumDriverManager().install()
            driver = WebDriverExtended(
                Edge(executable_path=driver_path, options=options),
                WebDriverListener(), config
            )
            return driver
        raise Exception("Provide valid driver name")
