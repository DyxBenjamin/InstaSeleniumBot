from time import sleep

from selenium.webdriver.common.keys import Keys


def load(driver):
    driver.get('https://web.whatsapp.com')
    print('Open: ', 'https://web.whatsapp.com')
    sleep(3)


def login(driver):
    button_chat = driver.find_element_by_xpath('//*[@id="action-button"]')
    button_chat.click()
    sleep(2)
    button_web = driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
    button_web.click()
    sleep(2)

    print('Scan QR Code, And then Enter')
    input()
    print('Logged In')


def login_name():
    print('Scan QR Code, And then Enter')
    input()
    print('Logged In')


def search_user_by_name(driver, name):
    text_input_search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    text_input_search.send_keys(name + Keys.ENTER)


def send_message(driver, message):
    for i in range(1, 400):
        text_input_message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
        text_input_message.send_keys(message + Keys.ENTER)
        print(i)
        sleep(1)
