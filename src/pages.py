import element


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def close_popup(self):
        element = self.driver.find_element_by_xpath('//*[@id="newsletter_popup"]/div/div/form/a')
        element.click()

    def click_sing_up(self):
        element = self.driver.find_element_by_id('newsletter-btn')
        element.click()

    def do_a_sing_up(self, email, gender):
        self.click_sing_up()
        element = self.driver.find_element_by_xpath('//*[@class="newsletter__form__item__input popup-newsletter__form__item__input form-email-item"]')
#        element = self.driver.find_elements_by_class_name('newsletter__form__item__input popup-newsletter__form__item__input form-email-item')
        element.send_keys(email)
        element = self.driver.find_element(by='value', value='men')
        element.click()
