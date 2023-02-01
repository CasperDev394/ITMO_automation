from pages.elements_page import ElementsPage
from pages.accordion_page import Accordion
import time


# def test_visible_btn_sidebar(browser):
#     elements_page = ElementsPage(browser)
#     elements_page.visit()
#     # elements_page.btn_sidebar_first.click()
#     time.sleep(3)
#     assert elements_page.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(3)
    assert elements_page.btn_sidebar_first_checkbox.not_visible()


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.one_paragraph.visible()
    accordion_page.one_section_btn.click()
    time.sleep(2)
    assert accordion_page.one_paragraph.not_visible()


def test_visible_default_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.one_paragraph.visible()
    accordion_page.one_section_btn.click()
    time.sleep(2)
    browser.set_window_size(width=1000, height=300)
    assert accordion_page.one_paragraph.not_visible()
    browser.refresh()
    assert accordion_page.one_paragraph.visible()
    browser.set_window_size(width=1000, height=1000)
    assert not accordion_page.not_elem.exist()
