import time

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utils.logger import Logger


class Search_page(Base):

    url = 'https://fix-online.sbis.ru/page/staff-list'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # Locators(нашел на вашем сайте через DevTools)
    input_search = '/html/body/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[7]/div[2]/div[2]/div/div/div/div[2]/input'
    btn_search = '//div[@data-qa = "Search__searchButton"]'


    # Getters(Которые возвращают нам значения из переменных)
    def getters_input_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_search)))

    def getters_btn_clear(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_search)))

    # Action(Тут уже говорим что делать нашим значениям)
    def setters_input_search(self,user_login):
        self.getters_input_search().send_keys(user_login)
        print(f"Написали буквы имени: {user_login}")

    def setters_btn_search(self):
        self.getters_btn_clear().click()
        print(f"Нажали на поиск ")

    def Search_user_one_simbol_ru(self):
        Logger.add_start_step(method="Search_user_one_simbol_ru")
        self.driver.get(self.url)
        self.get_url()
        time.sleep(3)
        self.setters_input_search("А")
        time.sleep(3)
        self.setters_btn_search()
        time.sleep(1)
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="Create_employee_en")

    def Search_user_tree_simbol_ru(self):
        Logger.add_start_step(method="Search_user_tree_simbol_ru")
        self.driver.get(self.url)
        self.get_url()
        time.sleep(5)
        self.setters_input_search("Арт")
        time.sleep(2)
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="Search_user_tree_simbol_ru")

    def Search_user_one_simbol_en(self):
        Logger.add_start_step(method="Search_user_one_simbol_en")
        self.driver.get(self.url)
        self.get_url()
        time.sleep(3)
        self.setters_input_search("A")
        time.sleep(3)
        self.setters_btn_search()
        time.sleep(2)
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="Search_user_one_simbol_en")

    def Search_user_tree_simbol_en(self):
        Logger.add_start_step(method="Search_user_tree_simbol_en")
        self.driver.get(self.url)
        self.get_url()
        time.sleep(3)
        self.setters_input_search("Art")
        time.sleep(2)
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="Search_user_tree_simbol_en")
