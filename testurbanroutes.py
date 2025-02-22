import data
import main
from urbanroutespage import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono

        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    def test_select_order_a_taxi_button_and_select_comfort_icon(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_a_taxi_button()
        routes_page.click_comfort_icon()

        comfort_icon = routes_page.get_the_select_comfort_icon().text
        comfort_text = "Comfort"
        assert comfort_text in comfort_icon


    def test_button_to_open_phone_number_modal(self):
        self.test_select_order_a_taxi_button_and_select_comfort_icon()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_to_open_phone_number_modal()

        assert routes_page.get_button_to_open_phone_number_modal().text in "Número de teléfono"


    def test_field_on_phone_number(self):
        self.test_select_order_a_taxi_button_and_select_comfort_icon()
        routes_page = UrbanRoutesPage(self.driver)
        the_phone_number = data.phone_number
        routes_page.get_button_to_open_phone_number_modal()
        routes_page.click_to_open_phone_number_modal()
        routes_page.click_and_set_phone_number_field()

        entered_phone_number = routes_page.get_phone_number_value()

        assert entered_phone_number == the_phone_number, f"El número de teléfono ingresado es incorrecto. Se esperaba {the_phone_number} pero se obtuvo {entered_phone_number}"


    def test_siguiente_button(self):
        self.test_field_on_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_at_siguiente_button()


    def test_sms_code_and_confirmation_button(self):
        self.test_siguiente_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_sms_code()
        assert routes_page.get_confirmation_button().text == "Confirmar", "El texto del botón no es 'Confirmar'"
        routes_page.click_at_confirmation_button()


    def test_add_payment_methods(self):
        self.test_sms_code_and_confirmation_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_text_payment_methods()


    def test_add_number_credit_card (self):
        #self.test_add_payment_methods()
        self.test_sms_code_and_confirmation_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_text_payment_methods()
        routes_page.click_credit_card_option()
        routes_page.get_card_number_field()
        routes_page.set_card_number()

        assert routes_page.get_card_number_field().get_attribute(
            "value") == '1234 5678 9100', "El número de tarjeta no se ha ingresado correctamente"


    def test_add_security_code (self):
        self.test_add_number_credit_card()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_code_number()

        assert routes_page.get_card_security_code_field().get_attribute("value") == '111', "El código de seguridad no se ha ingresado correctamente"


    def test_finally_add_credit_card(self):
        self.test_add_security_code()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_anyplace_continue()
        routes_page.get_and_click_agregar_button()
        routes_page.get_and_click_close_window_of_information_creditcard()


    def test_message_for_the_driver(self):
        self.test_finally_add_credit_card()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_for_the_driver()

        assert routes_page.get_message_for_the_driver_field().get_attribute(
            "value") == 'Traiga un aperitivo', "El mensaje para el conductor no se ha ingresado correctamente"


    def test_select_blanket_and_tissues(self):
        self.test_message_for_the_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_blanket_and_tissue_button()
        routes_page.select_the_blanket_and_tissue()
        assert not routes_page.get_blanket_and_tissue_button().is_selected(), \
        "El botón de manta y pañuelos sigue visible después de la selección."


    def test_request_ice_creams(self):
        self.test_select_blanket_and_tissues()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_to_order_ice_cream()


    def test_request_taxi_last_button(self):
         self.test_select_blanket_and_tissues()
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.click_to_ask_for_a_taxi_last_button()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()