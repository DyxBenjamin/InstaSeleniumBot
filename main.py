from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    NoSuchElementException
from selenium.webdriver import Opera
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.opera.options import Options
from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep


def load_inst():
    driver.get('https://www.instagram.com')
    print('Open: ', 'https://www.instagram.com')


def load_publication_inst(link):
    driver.get(link)
    print('Open: ', link)


def login_inst(instagram_username, inst_password):
    wait.until(element_to_be_clickable((By.NAME, 'username')))
    username = driver.find_element_by_name('username')
    username.send_keys(instagram_username)
    password = driver.find_element_by_name('password')
    password.send_keys(inst_password)
    button_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    button_login.click()

    wait.until(element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
    button_login_info = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    button_login_info.click()

    wait.until(presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div')))

    driver.find_element_by_css_selector(
        'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()

    print('Sesión iniciada')


def comment_inst():
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[2]/button').click()

    sleep(0.2)

    text_input = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
    text_input.send_keys('yo' + Keys.ENTER)
    sleep(5)

    print('Comentario exitoso')


def reload_page(page):
    print('Caja inactiva')
    load_publication_inst(page)


def check_active_comment_box_inst(page):
    wait.until(
        presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[1]/div/div/div[2]')))

    def check():
        try:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[2]/button').click()
            return True
        except NoSuchElementException:
            return False

    comment_box = check()
    print(comment_box)

    while not comment_box:
        reload_page(page)
        comment_box = check()
        print(comment_box)

    else:
        comment_inst()


new_options = Options()
driver: WebDriver = Opera(executable_path=r'C:/Users/Benjamin/Documents/operadriver/operadriver.exe',
                          options=new_options)

wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

load_inst()
login_inst('BenjaminGarridoG', 'Dayex23596')
load_publication_inst('https://www.instagram.com/p/CGLVt_cFp6v/')
check_active_comment_box_inst('https://www.instagram.com/p/CGLVt_cFp6v/')

driver.close()
