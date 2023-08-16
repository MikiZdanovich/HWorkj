from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


class DriverManager:
    @staticmethod
    def get_driver(driver_name,
                   is_headless=False):
        if driver_name == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.headless = is_headless
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("disable-infobars")

            return webdriver.Chrome(
                service=ChromiumService(
                    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
                ),
                options=chrome_options
            )

        elif driver_name == "firefox":
            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )
        elif driver_name == "edge":
            return webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install())
            )
        else:
            raise ValueError(f"Driver {driver_name} is not supported!")
