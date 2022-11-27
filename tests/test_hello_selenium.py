import time


def test_hello_world(browser):
    browser.get('https://ya.ru')
    time.sleep(3)
    assert 'Яндекс' in browser.title
