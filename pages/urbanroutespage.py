import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers.retrieve_phone_code import retrieve_phone_code



class UrbanRoutesPage:
    from_field = (By.ID, 'from')  # webelements
    to_field = (By.ID, 'to')

    order_a_taxi_button = (By.CSS_SELECTOR, '.button.round')
    select_comfort_icon = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]")

    click_button_open_phone_number_modal = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[1]/div")
    phone_number_field = (By.ID, "phone")
    click_on_siguiente_button = (By.XPATH, "//button[text()='Siguiente']")
    sms_code_field = (By.XPATH, "//*[@id='code']")
    confirmation_button = (By.XPATH, "//button[text()='Confirmar']")

    click_payment_method_button = (By.CSS_SELECTOR, ".pp-button")
    card_number_field = (By.ID, "number")
    select_add_credit_card_option = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]")
    add_card_number = (By.CSS_SELECTOR, ".card-number-input")
    add_card_security_code = (By.XPATH, "//input[@placeholder='12']")
    click_anyplace_to_continue = (By.CLASS_NAME, "card-wrapper")
    click_agregar_button = (By.XPATH, "//button[text()='Agregar']")
    close_window_of_information_credit_card = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")

    fill_message_for_the_driver = (By.NAME, "comment")
    select_blanket_and_tissue = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")

    ice_cream = (By.CLASS_NAME, 'counter-plus')
    counter_value = (By.CLASS_NAME, 'counter-value')
    quantity_2 = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

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

    def click_and_set_phone_number_field (self):
        #time.sleep(4)
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.phone_number_field).send_keys(data.phone_number)

    def set_number_phone(self):
        self.driver.find_element(*self.phone_number_field).send_keys(data.phone_number)

    def get_phone_number_value(self):
        phone_field = self.get_phone_number_field()              #Extrae el valor del campo de número de teléfono.
        return phone_field.get_attribute("value")                #con get_attribute("value"), obtiene lo que el usuario ha ingresado.


        # Los metodos para el botón "Siguiente"
    def get_siguiente_button(self):
       return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.click_on_siguiente_button))

    def click_at_siguiente_button(self):
        self.get_siguiente_button().click()


        # Los metodos para el sms
    def get_sms_code_field(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.sms_code_field))

    def set_sms_code(self):
        self.get_sms_code_field().send_keys(retrieve_phone_code(self.driver))


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
    def get_credit_card_option(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.select_add_credit_card_option))

    def click_credit_card_option (self):
        self.get_credit_card_option().click()


        # Los metodos para escribir el número de tarjeta de crédito
    def get_card_number_field(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.card_number_field))

    def set_card_number (self):
        self.get_card_number_field().send_keys(data.card_number)
        #time.sleep(2)
        self.driver.implicitly_wait(2)


        # Los metodos del campo de "Número de código"
    def get_card_security_code_field(self):
        return WebDriverWait(self.driver,5).until(EC.presence_of_element_located(self.add_card_security_code))

    def click_on_card_security_code_field(self):
        self.get_card_security_code_field().click()

    def set_code_number(self):
        self.driver.implicitly_wait(2)
        #time.sleep(2)
        self.driver.find_element(*self.add_card_security_code).send_keys(data.card_code)


        # El metodo hace clik en un costado para que se active el botón de "Agregar"
    def click_anyplace_continue (self):
        self.driver.find_element(*self.click_anyplace_to_continue).click()


        # Los metodos del botón de "Agregar"
    def get_and_click_agregar_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.click_agregar_button)).click()


        # Los metodos para cerrar ventana de información de metodo de pago
    def get_and_click_close_window_of_information_creditcard(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.close_window_of_information_credit_card)).click()



        # Los metodos para enviar mensaje al conductor
    def get_message_for_the_driver_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.fill_message_for_the_driver))

    def click_to_activate_message_driver_field(self):
        self.get_message_for_the_driver_field().click()

    def set_message_for_the_driver(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.fill_message_for_the_driver)).send_keys(data.message_for_driver)



       # Los metodos para seleccionar la manta y los pañuelos
    def get_blanket_and_tissue_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.select_blanket_and_tissue))

    def select_the_blanket_and_tissue (self):
        self.driver.find_element(*self.select_blanket_and_tissue).is_selected()



      # Los metodos para pedir un helado de chocolate
    def request_to_order_ice_cream (self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.ice_cream).click()
        self.driver.find_element(*self.counter_value)
        self.driver.find_element(*self.quantity_2)

    def get_ice_cream_counter(self):
        return self.driver.find_element(*self.ice_cream).get_property('value')



        # Los metodos del botón de "Pedir un taxi" al final
    def get_ask_for_a_taxi_last_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ask_for_the_taxi_button))

    def click_to_ask_for_a_taxi_last_button (self):
        self.get_ask_for_a_taxi_last_button().click()




