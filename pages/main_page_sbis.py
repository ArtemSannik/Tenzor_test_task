from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

from utils.logger import Logger


class Main_page(Base):

    url = 'https://fix-online.sbis.ru/page/staff-list'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    personal_btn = '/html/body/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[7]/div[2]/div[1]/span/span'
    person = '//span[@class="ws-ellipsis"]'
    create_new_persona = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/div/div[2]'
    # -------------------------------------------------------

    # Getters
    def getters_personal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_btn)))

    def getters_personal_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.person)))

    def getters_personal_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create_new_persona)))

    # -------------------------------------------------------

    #Action
    def setters_personal(self):
        self.getters_personal().click()
        print("Нажали на кнопку +")

    def setters_personal_2(self):
        self.getters_personal_2().click()
        print("Нажали на кнопку 'добавить сотрудник'")

    def setters_personal_3(self):
        self.getters_personal_3().click()
        print("Нажали на 'просто компания'")


    # -------------------------------------------------------

    def Main_pages(self):
        Logger.add_start_step(method="Main_pages")
        self.get_url()
        self.get_screenshot()
        self.setters_personal()
        time.sleep(1)
        self.get_screenshot()
        self.setters_personal_2()
        # self.get_screenshot()
        self.setters_personal_3()
        Logger.add_end_step(url=self.driver.current_url, method="Main_pages")


