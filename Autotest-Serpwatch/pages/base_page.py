import datetime
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.expected_conditions import text_to_change


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    @staticmethod
    def click_btn(wait_page, btn):
        wait_page.until(EC.element_to_be_clickable(btn)).click()


    @staticmethod
    def slider(self, wait_page, slid, amount):
        slider_pricing = wait_page.until(EC.presence_of_element_located(slid))
        move = ActionChains(self.browser)
        move.click_and_hold(slider_pricing).move_by_offset(amount, 0).release().perform()


    def click_js_btn(self, wait_page, btn):
        element = self.browser.find_element(*btn)
        wait_page.until(EC.element_to_be_clickable(btn))
        self.browser.execute_script("arguments[0].click();", element)


    def enable_checkbox(self, wait_page, btn):
        wait_page.until(EC.visibility_of_element_located(btn))
        self.browser.execute_script("document.getElementById('enabled').checked = true")

    def click_js_simple_btn(self, btn):
        element = self.browser.find_element(*btn)
        self.browser.execute_script("arguments[0].click();", element)

    @staticmethod
    def activate_new_tab(self, wait_page, elem):
        first_window = self.browser.window_handles[0]  # Запомнить имя текущей вкладки
        print('First:', first_window)

        wait_page.until(EC.element_to_be_clickable(elem)).click()

        new_window = self.browser.window_handles[1]  # выбираем вторую вкладку
        print('Second:', new_window)
        self.browser.switch_to.window(new_window)  # переключения на новую вкладку


    @staticmethod
    def send_key(wait_page, elem, key):
        wait_page.until(EC.visibility_of_element_located((elem)))
        wait_page.until(EC.presence_of_element_located(elem)).send_keys(key)

    @staticmethod
    def send_file(wait_page, elem, key):
        wait_page.until(EC.presence_of_element_located(elem)).send_keys(key)

    def take_text(self, elem):
        element = self.browser.find_element(*elem).text

    @staticmethod
    def select(wait_page, elem, text):
        wait_page.until(EC.presence_of_element_located(elem)).is_displayed()
        select_element =  wait_page.until(EC.visibility_of_element_located((elem)))
        select = Select(select_element)
        select.select_by_visible_text(text)

    @staticmethod
    def ajax_complete(wait_ajax):
        wait_ajax.until(
            lambda driver: driver.execute_script("return jQuery.active") == 0
        )
        wait_ajax.until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

    def text_change(self, wait_page, elem):
        try:
            text_before = self.browser.find_element(*elem).text
        except NoSuchElementException:
            text_before = ""

        wait_page.until(text_to_change(elem, text_before))

    def change_style(self, elem, style):
        element = self.browser.find_element(*elem)
        self.browser.execute_script(f"arguments[0].style = '{style}'", element)

    def is_element_clickable(self, how, what, timeout=25, screenshot=True):
        try:
            # self.browser.find_element(how, what)
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what))
            )
        except TimeoutException:
            if screenshot:
                self.take_screenshot()
            return False

        except NoSuchElementException:
            if screenshot:
                self.take_screenshot()
            return False

        return True

    def is_element_present(self, how, what, timeout=15, screenshot=True):
        try:
            # self.browser.find_element(how, what)
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )

        except TimeoutException:
            if screenshot:
                self.take_screenshot()
            return False

        except NoSuchElementException:
            if screenshot:
                self.take_screenshot()
            return False

        return True

    # делаем скриншот
    def take_screenshot(self):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        namefile = f"screenshot-{now}.png"
        self.browser.get_screenshot_as_file(namefile)
        print(f"Taked screenshot: {namefile}")

    def is_element_present_wait(self, how, what, timeout=150, screenshot=True):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:

            if screenshot:
                self.take_screenshot()
            return False

        except NoSuchElementException:
            if screenshot:
                self.take_screenshot()
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4, screenshot=True):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            if screenshot:
                self.take_screenshot()
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    # метод для проверки, что  элемент исчезает, следует воспользоваться явным ожиданием вместе с функцией until_not,
    # в зависимости от того, какой результат мы ожидаем:
    def wait_and_click(self, how, what, timeout=30):
        try:
            WebDriverWait(self.browser, timeout).until(
                expected_conditions.element_to_be_clickable((how, what))
            ).click()
        except TimeoutException:
            return False
        return True


    def close_popup(self):
        self.browser.execute_script("$('#featuresModal').modal('hide');")

    def until(self, param):
        pass

# пример вставки формулы
# def solve_quiz_and_get_code(self):
# alert = self.browser.switch_to.alert
# x = alert.text.split(" ")[2]
# answer = str(math.log(abs((12 * math.sin(float(x))))))
# alert.send_keys(answer)
#  alert.accept()
#      alert = self.browser.switch_to.alert
#     alert_text = alert.text
#     print(f"Your code: {alert_text}")
#     alert.accept()
# except NoAlertPresentException:
#    print("No second alert presented")
