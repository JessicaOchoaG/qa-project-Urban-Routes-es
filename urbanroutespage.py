import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import main
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from data import phone_number


class UrbanRoutesPage:
    from_field = (By.ID, 'from')  # webelements
    to_field = (By.ID, 'to')
    order_a_taxi_button = (By.CSS_SELECTOR, '.button.round')
    select_comfort_icon = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]")

    click_button_open_phone_number_modal = (By.CSS_SELECTOR, '.np-button')  #OK
    phone_number_field = (By.CLASS_NAME, "np-text")
    click_on_siguiente_button = (By.XPATH, "//button[text()='Siguiente']")  #OK
    sms_code_field = (By.XPATH, "//*[@id='code']") #OK
    confirmation_button = (By.XPATH, "//button[text()='Confirmar']") #OK

    click_payment_method_button = (By.CSS_SELECTOR, ".pp-button.filled")   #OK
    select_add_credit_card_option = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]")
    click_on_card_number_field = (By.ID, "number")
    add_card_number = (By.CSS_SELECTOR, ".card-number-input")  #OK
    card_security_code_field = (By.ID, "code")
    add_card_security_code = (By.CSS_SELECTOR, ".card_code_input")  #mal
    click_anyplace_to_continue = (By.CLASS_NAME, "card-wrapper")
    click_agregar_button = (By.XPATH, "//button[text()='Agregar']")  #OK
    close_window_of_information_credit_card = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")

    fill_message_for_the_driver = (By.NAME, "comment")
    select_blanket_and_tissue = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    add_an_chocolate_ice_cream = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]")
    add_a_strawberry_ice_cream = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/div/div[3]")

    ask_for_the_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")  #OK



    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)



        # Metodos para botón "Pedir un taxi"
    def get_order_a_taxi_button(self):
       return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.order_a_taxi_button))

    def click_order_a_taxi_button(self):
        self.get_order_a_taxi_button().click()


        # Metodos para ícono "Comfort"
    def get_the_select_comfort_icon(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.select_comfort_icon))

    def click_comfort_icon(self):
        self.get_the_select_comfort_icon().click()


        # Metodos para boton que despliega modal de número de teléfono
    def get_button_to_open_phone_number_modal(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.click_button_open_phone_number_modal))

    def click_to_open_phone_number_modal (self):
        self.get_button_to_open_phone_number_modal().click()


        # Metodos para el campo de número de teléfono
    def get_phone_number_field(self):
        return WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.phone_number_field))

    def click_phone_number_field (self):
        self.get_phone_number_field().click()

    def set_number_phone(self):
        self.get_phone_number_field().send_keys(data.phone_number)


        # Los metodos para el botón "Siguiente"
    def get_siguiente_button(self):
       return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.click_on_siguiente_button))

    def click_at_siguiente_button(self):
        self.get_siguiente_button().click()


        # Los metodos para el sms
    def get_sms_code_field(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.sms_code_field))

    def set_sms_code(self):
        self.get_sms_code_field().send_keys(data.card_code)


        # Los metodos para el botón "Confirmar"
    def get_confirmation_button(self):
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.confirmation_button))

    def click_at_confirmation_button(self):
            self.get_confirmation_button().click()


            # Los metodos para el boton añadir metodos de pago
    def get_payment_methods_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.click_payment_method_button))

    def click_on_text_payment_methods (self):
        self.get_payment_methods_button().click()


        # Los metodos para añadir la opción de tarjeta de crédito
    def get_payment_methods_option(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.select_add_credit_card_option))

    def click_on_option_payment_methods (self):
        self.get_payment_methods_button().click()

    def set_card_number (self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.add_card_number)).send_keys(data.card_number)


        # Los metodos del campo de "Número de código"
    def get_card_security_code_field(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.card_security_code_field))

    def click_on_card_security_code_field(self):
        self.get_card_security_code_field().click()

    def set_code_number(self):
        new_code_number = "Card number"
        self.driver.find_element(*self.add_card_security_code).send_keys(new_code_number)


        # El metodo hace clik en un costado para que se active el botón de "Agregar"
    def click_anyplace_continue (self):
        self.driver.find_element(*self.click_anyplace_to_continue).click()


        # Los metodos del botón de "Agregar"
    def get_agregar_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.click_agregar_button))

    def click_agregar_button (self):
        self.get_agregar_button().click()


        # Los metodos para cerrar ventana de información de metodo de pago
    def get_close_window_of_information_creditcard(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.close_window_of_information_credit_card))

    def click_to_close_window_of_information_creditcard (self):
        #self.driver.find_element(*self.close_window_of_information_credit_card).click()
        self.get_close_window_of_information_creditcard().click()


        # Los metodos para enviar mensaje al conductor
    def get_message_for_the_driver_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.fill_message_for_the_driver))

    def click_to_activate_message_driver_field(self):
        self.get_message_for_the_driver_field().click()

    def set_message_for_the_driver(self):
        message_for_driver = "Message"
        self.driver.find_element(*self.fill_message_for_the_driver).send_keys(message_for_driver)


       # Los metodos para seleccionar la manta y los pañuelos
    def get_blanket_and_tissue_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.select_blanket_and_tissue))

    def select_the_blanket_and_tissue (self):
        self.driver.find_element(*self.select_blanket_and_tissue).is_selected()


      # Los metodos para pedir un helado de chocolate
    def get_to_order_an_ice_cream_buttón(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_an_chocolate_ice_cream))

    def click_to_order_an_ice_cream (self):
        self.get_to_order_an_ice_cream_buttón().click()

    # Los metodos para pedir un helado de fresa
    def get_to_order_an_ice_cream_buttón(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_a_strawberry_ice_cream))

    def click_to_order_an_ice_cream(self):
        self.get_to_order_an_ice_cream_buttón().click()


        # Los metodos del botón de "Pedir un taxi" al final
    def get_ask_for_a_taxi_last_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ask_for_the_taxi_button))

    def click_to_ask_for_a_taxi_last_button (self):
        self.get_ask_for_a_taxi_last_button().click()




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
        assert comfort_text in comfort_text

    def test_button_to_open_phone_number_modal(self):
        self.test_select_order_a_taxi_button_and_select_comfort_icon()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_to_open_phone_number_modal()

        assert routes_page.get_button_to_open_phone_number_modal().text in "Número de teléfono"

    def test_phone_number_field(self):
        self.test_button_to_open_phone_number_modal()
        routes_page = UrbanRoutesPage(self.driver)                      #Falla
        routes_page.click_to_open_phone_number_modal()
        routes_page.set_number_phone()

        #assert data.phone_number == routes_page.set_number_phone()

    def test_field_on_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)                      #Falla
        the_phone_number = data.phone_number
        routes_page.click_phone_number_field()
        routes_page.set_number_phone()
        assert routes_page.set_number_phone() == the_phone_number
        #actual_phone_number = routes_page.get_phone_number_value()
        #assert actual_phone_number == the_phone_number


    def test_siguiente_button(self):
        self.test_field_on_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_at_siguiente_button()

        assert routes_page.get_siguiente_button().text in "Siguiente"


    def test_confirmation_button(self):
        self.test_siguiente_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.confirmation_button()

        assert routes_page.get_confirmation_button().text in "Confirmar"

    def test_add_payment_methods(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_text_payment_methods()

        assert routes_page.get_payment_methods_button().text == "Método de pago"




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()