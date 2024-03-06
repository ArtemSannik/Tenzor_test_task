import pytest
from selenium import webdriver
from pages.authorization_page import Authorization_page
from pages.main_page_sbis import Main_page
from pages.create_employee_pages import Emppoyee_create_page
from pages.search_person_page import Search_page

@pytest.mark.run(order=1)
def test_people_tenzor_ru():

    driver = webdriver.Chrome()
    # -------------------------------------------------------

    print("Начало позитивного тестирования: авторизации аккаунта с тестовыми данным")
    pages_authorization = Authorization_page(driver)
    pages_authorization.Authorization()
    print("Конец позитивного тестирования: авторизации")
    # -------------------------------------------------------

    print("\nНачало Smoke тестирования основной логики по добавлению нового сотрудника(кириллица)")
    pages_main = Main_page(driver)
    pages_main.Main_pages()
    print("Конец позитивного тестирования: основной логики пути")
    # -------------------------------------------------------

    print("\nНачало Smoke тестирования по добавлению сотрудника с позитивным сценарием(кириллица)")
    pages_empoloyee = Emppoyee_create_page(driver)
    pages_empoloyee.Create_employee_ru()
    print("Конец позитивного тестирования")
    # -------------------------------------------------------

    print("\nНачало Smoke тестирования по поиску пользователя по одному символу(кириллица)")
    pages_search = Search_page(driver)
    pages_search.Search_user_one_simbol_ru()
    print("Конец позитивного тестирования: поиск сотрудника по одному символу")
    # -------------------------------------------------------

    print("\nНачало Smoke тестирования по поиску пользователя по нескольким символам(кириллица)")
    pages_search = Search_page(driver)
    pages_search.Search_user_tree_simbol_ru()
    print("Конец позитивного тестирования: поиск сотрудника по нескольким символам")
    # -------------------------------------------------------


@pytest.mark.run(order=2)
def test_people_tenzor_en():

    driver = webdriver.Chrome()
    # -------------------------------------------------------

    print("Начало позитивного тестирования: авторизации аккаунта с тестовыми данным")
    pages_authorization = Authorization_page(driver)
    pages_authorization.Authorization()
    print("Конец позитивного тестирования: авторизации")
    # -------------------------------------------------------

    print("\nНачало Smoke тестирования основной логики по добавлению нового сотрудника")
    pages_main = Main_page(driver)
    pages_main.Main_pages()
    print("Конец позитивного тестирования: основной логики пути")
    # -------------------------------------------------------

    print("\nНачало Smoke тестирования по добавлению сотрудника с позитивным сценарием(En)")
    pages_empoloyee = Emppoyee_create_page(driver)
    pages_empoloyee.Create_employee_en()
    print("Конец позитивного тестирования")
    # -------------------------------------------------------

    print("\nНачало Smoke тестирования по поиску пользователя по одному символу(En)")
    pages_search = Search_page(driver)
    pages_search.Search_user_one_simbol_en()
    print("Конец позитивного тестирования: поиск сотрудника по одному символу")
    # -------------------------------------------------------

    print("\nНачало Smoke тестирования по поиску пользователя по нескольким символам(En)")
    pages_search = Search_page(driver)
    pages_search.Search_user_tree_simbol_en()
    print("Конец позитивного тестирования: поиск сотрудника по нескольким символам")



