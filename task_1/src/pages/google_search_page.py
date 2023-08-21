from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com"
        self.search_input = (By.CSS_SELECTOR, '[title="Search"]')
        self.search_results = (By.CSS_SELECTOR, "h3")
        self.result_stats = (By.ID, "result-stats")

    def navigate_to(self):
        self.driver.get(self.url)

    def search(self, query):
        search_field = self.driver.find_element(*self.search_input)
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)

    def get_search_links(self):
        elements = self.driver.find_elements(*self.search_results)
        return [
            element.find_element_by_xpath("../..").get_attribute("href")
            for element in elements
        ]

    def get_first_result_text(self):
        return self.driver.find_element(*self.search_results).text

    def get_num_results(self):
        result_stats_text = self.driver.find_element(*self.result_stats).text
        return int(result_stats_text.split()[1].replace(",", ""))
