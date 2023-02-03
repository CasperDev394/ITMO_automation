from pages.demoqa_page import Demoqa


def test_icon_exist(browser):
    """ Demo qa page - icon exist. """
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()

