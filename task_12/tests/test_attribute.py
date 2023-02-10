import time
import allure
from pages.text_box_page import TextBoxPage


@allure.feature('check attr')
@allure.story('проверка значения атрибута элемента')
@allure.severity(allure.severity_level.NORMAL)
def test_placeholder(browser):
    """ проверка значения атрибута элемента """

    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name1'


@allure.feature('check attr')
@allure.story('Проверка наличия атрибута')
@allure.severity(allure.severity_level.CRITICAL)
def test_attr_exist(browser):
    """ Проверка наличия атрибута """
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    text_box_page.btn_first.click()
    time.sleep(2)
    assert text_box_page.box_first_menu.get_dom_attribute('style')


@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.BLOCKER)
def test_attr_not_exist(browser):
    """ Проверка отсутствия атрибута """
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    assert not text_box_page.btn_first.get_dom_attribute('style11')


@allure.feature('check attr')
@allure.story('Проверка упавшего теста')
@allure.severity(allure.severity_level.BLOCKER)
def test_fail():
    assert 221 == 222

