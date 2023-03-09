import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage
import random


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person_info = next(generated_person())  # перебор по одному значению ниже
        full_name, path = generated_file()
