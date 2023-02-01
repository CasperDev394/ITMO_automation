from pages.demoqa_page import Demoqa
from pages.elements_page import ElementsPage
import time


# def test_check_text_please(browser):
#     demo_qa_page = Demoqa(browser)
#     elements_page = ElementsPage(browser)
#     demo_qa_page.visit()
#     demo_qa_page.btn_elements.click()
#     assert elements_page.text_please.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_please.get_text() == 'Please select an item from left to start practice.'
    assert elements_page.text_elements.get_text() == 'Elements'

    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()



