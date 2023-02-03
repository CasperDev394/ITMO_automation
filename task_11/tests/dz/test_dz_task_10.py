from pages.modal_dialogs_page import ModalDialogsPage
from pages.alerts_page import AlertsPage


def test_elements_dz(browser):
    modal_dialog_page = ModalDialogsPage(browser)
    modal_dialog_page.visit()
    assert modal_dialog_page.btns_menu.check_count_elements(5)


def test_navigation_dz(browser):
    modal_dialog_page = ModalDialogsPage(browser)
    alerts_page = AlertsPage(browser)

    modal_dialog_page.visit()
    modal_dialog_page.btn_alerts.click()
    browser.back()
    browser.set_window_size(width=900, height=400)
    browser.forward()
    assert alerts_page.equal_url()
    browser.set_window_size(width=1000, height=1000)
