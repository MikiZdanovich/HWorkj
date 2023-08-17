import pytest
import json


@pytest.mark.smoke
def test_google_search(google_search_page):

    google_search_page.navigate_to()

    google_search_page.search("Python")

    links = google_search_page.get_search_links()
    for link in links:
        print(link)

    assert "Python" in google_search_page.get_first_result_text()
    assert google_search_page.get_num_results() > 1000

    report = {
        "links": links,
        "first_search_result_text": google_search_page.get_first_result_text(),
        "first_search_result_verification": "Python" in google_search_page.get_first_result_text(),
        "number_of_search_results": google_search_page.get_num_results(),
        "number_of_search_results_verification": google_search_page.get_num_results() > 1000,
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)
