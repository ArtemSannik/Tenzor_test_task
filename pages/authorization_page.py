import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utils.logger import Logger

# потомок класса Base
class Authorization_page(Base):

    url = 'https://fix-online.sbis.ru/page/staff-list'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # -------------------------------------------------------

    # Locators
    user_login = "//input[@type = 'text']"
    btn_authorization_1 = "/html/body/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/span/span/div"
    user_password = "//input[@type = 'password']"
    btn_authorization_2 = "/html/body/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div[1]/div/div/div/div/div[3]/span/span/div"
    btn_password = '/html/body/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]'
    # -------------------------------------------------------


    # Getters(Которые возвращают нам значения из переменных)
    def getters_user_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))

    def getters_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def getters_btn_authorization_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_authorization_1)))

    def getters_btn_authorization_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_authorization_2)))

    def getters_btn_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_password)))
    # -------------------------------------------------------

    # Action(Тут уже говорим что делать нашим значениям)
    def setters_user_login(self,user_login):
        self.getters_user_login().send_keys(user_login)
        print(f"Написали логин: {user_login}")

    def setters_user_password(self,user_password):
        self.getters_user_password().send_keys(user_password)
        print(f"Написали пароль: {user_password}")

    def setters_btn_authorization_1(self):
        self.getters_btn_authorization_1().click()
        print(f"Нажали на кнопку входа")

    def setters_btn_authorization_2(self):
        self.getters_btn_authorization_2().click()
        print(f"Нажали на кнопку входа")

    def setters_btn_password(self):
        self.getters_btn_password().click()
        print(f"Нажали на показать пароль")
    # -------------------------------------------------------

    def Authorization(self):
        Logger.add_start_step(method="Authorization")
        self.driver.get(self.url)
        self.get_url()
        self.driver.maximize_window()
        self.setters_user_login('newfix')
        self.setters_btn_authorization_1()
        self.setters_user_password('123qwerty')
        self.setters_btn_password()
        time.sleep(1)
        self.get_screenshot()
        self.setters_btn_authorization_2()
        Logger.add_end_step(url=self.driver.current_url, method="Authorization")

