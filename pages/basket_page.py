from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket item is presented, but should not be"

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "'Your basket is empty.' text is not presented"
