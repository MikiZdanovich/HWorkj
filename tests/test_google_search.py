import pytest
import json
from src.pages.google_search_page import GoogleSearchPage


@pytest.mark.smoke
def test_google_search(driver):
    page = GoogleSearchPage(driver)

    page.navigate_to()

    page.search("Python")

    links = page.get_search_links()
    for link in links:
        print(link)

    assert "Python" in page.get_first_result_text()
    assert page.get_num_results() > 1000

    report = {
        "links": links,
        "first_search_result_text": page.get_first_result_text(),
        "first_search_result_verification": "Python" in page.get_first_result_text(),
        "number_of_search_results": page.get_num_results(),
        "number_of_search_results_verification": page.get_num_results() > 1000,
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)
