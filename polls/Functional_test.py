from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from unittest import TestCase, skip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FunctionalTest (TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\santi\PycharmProjects\KataWebHelp\geckodriver.exe')
        #self.browser = webdriver.Firefox(executable_path=r'..\geckodriver.exe')
        self.browser.implicitly_wait(2)
        self.browser._is_remote = False

    def tearDown(self):
        self.browser.quit()

    @skip('')
    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    @skip('')
    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        sleep(0.3)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Lavanderia']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys(r'C:\Users\santi\Downloads\bacteria.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    @skip('')
    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        wait = WebDriverWait(self.browser, 5)

        user = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#login-form > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)")))
        user.clear()
        user.send_keys('juan645')

        clave = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#login-form > div:nth-child(2) > div:nth-child(2) > input:nth-child(2)")))
        clave.clear()
        clave.send_keys('clave123')

        botonLogin = self.browser.find_element_by_id('id_log')
        botonLogin.click()

        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_edicion_independiente(self):

        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_editar')
        link.click()
        sleep(0.3)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('David')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Rodriguez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Lavanderia']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('1234567')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys(r'C:\Users\santi\Downloads\bacteria.jpg')

        botonEdicion = self.browser.find_element_by_id('id_grabar')
        botonEdicion.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="David Rodriguez"]')

        self.assertIn('David Rodriguez', span.text)