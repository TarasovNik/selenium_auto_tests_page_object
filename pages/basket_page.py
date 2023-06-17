from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_message_de(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert "Ihr Warenkorb ist leer" in message.text, "There is no massage in basket"

    def should_not_be_button_checkout(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_BUTTON_CHECKOUT, 1), \
           "There are some items in basket, but should not be"