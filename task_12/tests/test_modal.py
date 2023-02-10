import time

from pages.modal_dialogs_page import ModalDialogsPage
import pytest

from selenium import webdriver


def param():
    browser = webdriver.Chrome()
    modal_page = ModalDialogsPage(browser)
    modal_page.visit()
    return modal_page.equal_url()


@pytest.mark.skipif(condition=not param(), reason='Пропустить если страница недоступна')
def test_modal(browser):
    modal_page = ModalDialogsPage(browser)

    modal_page.visit()
    assert modal_page.btn_modal_1.exist()
    assert modal_page.btn_modal_2.exist()

    modal_page.btn_modal_1.click()
    assert modal_page.modal_1.exist()
    modal_page.close_1.click()
    assert not modal_page.modal_1.exist()

    modal_page.btn_modal_2.click()
    assert modal_page.modal_2.exist()
    modal_page.close_2.click()
    assert not modal_page.modal_2.exist()
