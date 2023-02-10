from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.btn_alerts = WebElement(driver, 'div:nth-child(3) > div > ul > #item-1')

        self.btn_modal_1 = WebElement(driver, '//*[@id="showSmallModal"]', 'xpath')
        self.btn_modal_2 = WebElement(driver, '//*[@id="showLargeModal"]', 'xpath')

        self.modal_1 = WebElement(driver, 'body > div.fade.modal.show > div.modal-sm')
        self.modal_2 = WebElement(driver, 'body > div.fade.modal.show > div.modal-lg')

        self.close_1 = WebElement(driver, '#closeSmallModal')
        self.close_2 = WebElement(driver, '#closeLargeModal')

