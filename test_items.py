link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_add_to_the_basket(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary1')
    assert button, 'Кнопка не найдена'
