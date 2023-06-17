from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self, alert=True):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        if alert == True:
            self.solve_quiz_and_get_code()

    def check_add_to_basket_massege(self):
        ITEM_NAME_TEXT = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        MESSAGE_NAME_TEXT = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME).text
        assert ITEM_NAME_TEXT == MESSAGE_NAME_TEXT, ITEM_NAME_TEXT + " is not equal to " + MESSAGE_NAME_TEXT

    def check_basket_price_after_add(self):
        ITEM_PRICE = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        BASKET_PRICE = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert ITEM_PRICE == BASKET_PRICE, "Sum price" + ITEM_PRICE + " is not equal to item price " + BASKET_PRICE

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappeare_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared, but should be"