import datetime
class Base():

    # передаем драйвер,который хранит экзепляр драйвера хром
    def __init__(self, driver):
        self.driver = driver

    # -------------------------------------------------------
    # Метод для мониторинга текущего URL
    def get_url(self):
        get_curret_url = self.driver.current_url
        print(f"Наш url: {get_curret_url}")

    # -------------------------------------------------------

    # Метод для спрасивания значения
    def word_check(self,word,result):
        get_word = word.text
        assert get_word == result
        print(f"Мы успешно спарсили значение: {result}")

    # -------------------------------------------------------

    # Метод для создания скриншота
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screnn = f"screenshot{now_date}.png"
        self.driver.save_screenshot('/Users/artem/Desktop/StepikTests/pythonTest_Task_Tenzor/screen/' + name_screnn)
        print("Сделали скриншот")
    # -------------------------------------------------------



