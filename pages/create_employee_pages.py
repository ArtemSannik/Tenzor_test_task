from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

from utils.logger import Logger


class Emppoyee_create_page(Base):

    url = 'https://fix-online.sbis.ru/page/staff-list'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # -------------------------------------------------------

    #Locators
    input_last_name = '//input[@name="ws-lastName"]'
    input_first_name = '//input[@name="ws-firstName"]'
    input_middle_name = '//input[@name="ws-middleName"]'
    input_job_title = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[2]'
    job_title = '/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div/table/tbody/tr[7]/td/div/div[2]/div/div/div/div'
    input_number_phone = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[4]/div/div[2]/div[1]/div[3]/div/div/div/div/div/div/div/div/input'
    input_birth_day = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[5]/div[2]/div/div/div/div/div[1]/input'
    drop_gender = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[5]/div[3]/div'
    drop_gender_male = '/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[2]/div/div'
    btn_sucesfull = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/span[3]/span/i'
    btn_okey = "/html/body/div[1]/div/div/div/div[1]/div[3]/div/div/div[4]/div/div[2]/span/span/span"

    # -------------------------------------------------------

    # Getters
    def getters_lastName(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_last_name)))

    def getters_firstName(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_first_name)))

    def getters_middleName(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_middle_name)))

    def getters_birth_day(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_birth_day)))

    def getters_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_number_phone)))

    def getters_input_job_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_job_title)))

    def getters_job_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.job_title)))

    def getters_btn_sucsefull(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_sucesfull)))

    def getters_btn_okey(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_okey)))

    def getters_drop_gender(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drop_gender)))

    def getters_drop_gender_male(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drop_gender_male)))


    # -------------------------------------------------------

    #Action
    def setters_lastName(self,user_lastName):
        self.getters_lastName().send_keys(user_lastName)
        print(f"Написали фамилию: {user_lastName}")

    def setters_firstName(self, user_firstName):
        self.getters_firstName().send_keys(user_firstName)
        print(f"Написали Имя: {user_firstName}")

    def setters_middleName(self, user_middleName):
        self.getters_middleName().send_keys(user_middleName)
        print(f"Написали Отчество: {user_middleName}")

    def setters_job_title(self):
        self.getters_input_job_title().click()
        print(f"Нажали на кнопку добавления должности")

    def setters_job(self):
        self.getters_job_title().click()
        print(f"мы добавили должность")

    def setters_phoneNumber(self, user_phoneNumber):
        self.getters_phone_number().send_keys(user_phoneNumber)
        print(f"номер телефона: {user_phoneNumber}")

    def setters_birthDay(self, user_birthDay):
        self.getters_birth_day().send_keys(user_birthDay)
        print(f"Написали дату рождения: {user_birthDay}")

    def setters_drop_gender(self):
        self.getters_drop_gender().click()
        print("нажали на выбор пола")

    def setters_drop_gender_male(self):
        self.getters_drop_gender_male().click()
        print("нажали на выбор пола мужской")

    def setters_btn_sucsefull(self):
        self.getters_btn_sucsefull().click()
        print("Нажали на кнопку добавления нового сотрудника")

    def setters_btn_okey(self):
        self.getters_btn_okey().click()
        print("согласились")

    # -------------------------------------------------------

    def Create_employee_ru(self):
        Logger.add_start_step(method="Create_employee_ru")
        self.get_url()
        time.sleep(1)
        self.get_screenshot()
        self.setters_lastName("Артемов")
        self.setters_firstName("Артем")
        self.setters_middleName("Артемьевич")
        self.setters_job_title()
        self.setters_job()
        self.setters_phoneNumber("+79997238222")
        self.setters_birthDay("15.07.1999")
        time.sleep(1)
        self.get_screenshot()
        self.setters_drop_gender()
        self.setters_drop_gender_male()
        time.sleep(1)
        self.setters_btn_sucsefull()
        time.sleep(10)
        # self.setters_btn_okey()
        self.driver.refresh()
        Logger.add_end_step(url=self.driver.current_url, method="Create_employee_ru")
    # -------------------------------------------------------

    def Create_employee_en(self):
        Logger.add_start_step(method="Create_employee_en")
        self.get_url()
        time.sleep(1)
        self.get_screenshot()
        self.setters_lastName("Artemov")
        self.setters_firstName("Artem")
        self.setters_middleName("Artemievich")
        self.setters_job_title()
        self.setters_job()
        self.setters_phoneNumber("+79997238222")
        self.setters_birthDay("15.07.1999")
        time.sleep(1)
        self.get_screenshot()
        self.setters_drop_gender()
        self.setters_drop_gender_male()
        time.sleep(1)
        self.setters_btn_sucsefull()
        # self.get_screenshot()
        # self.setters_btn_okey()
        time.sleep(10)
        self.driver.refresh()
        Logger.add_end_step(url=self.driver.current_url, method="Create_employee_en")

