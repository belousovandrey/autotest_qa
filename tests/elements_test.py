from pages.element_page import TextBoxPage
import time


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            print()
            print(output_name)
            print(output_email)
            print(output_cur_address)
            print(output_per_address)
            # time.sleep(10)