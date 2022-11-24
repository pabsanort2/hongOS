import os
from pathlib import Path
from fastbook import load_learner
from django.test import TestCase
from django.conf import settings
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from .models import HongOSUser, ImagenDataset
from selenium.webdriver.common.action_chains import ActionChains
import PIL


# Create your tests here.

class testModel(TestCase):

    def test_agaricus_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/agaricus.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Agaricus')

    def test_amanita_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/amanita.jpeg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Amanita')
    
    def test_boletus_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/boletus.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Boletus')

    def test_cortinarius_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/cortinarius.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Cortinarius')

    def test_entoloma_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/entoloma.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Entoloma')

    def test_hygrocybe_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/hygrocybe.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Hygrocybe')

    def test_lactarius_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/lactarius.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Lactarius')

    def test_russula_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/russula.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Russula')

    def test_suillus_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/test_data/suillus.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Suillus')

class SeleniumTestCases(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        user = User.objects.create_user('dummy', 'dummy@dummy.com', 'dummy')
        hongosUser = HongOSUser(user= user, email=user.email)
        hongosUser.save()
        super().setUp()    

    def testImagenRepetida(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/agaricus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/agaricus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.XPATH, "//*[contains(text(), 'Es probable que ya hayas subido esta imagen.')]").text == 'Es probable que ya hayas subido esta imagen.'

    def testImagenAgaricus(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/agaricus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Agaricus')

    def testImagenAmanita(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/amanita.jpeg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Amanita')
    
    def testImagenBoletus(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/boletus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Boletus')

    def testImagenCortinarius(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/cortinarius.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Cortinarius')

    def testImagenEntoloma(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/entoloma.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Entoloma')

    def testImagenHygrocybe(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/hygrocybe.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Hygrocybe')

    def testImagenLactarius(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/lactarius.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Lactarius')

    def testImagenRussula(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/russula.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Russula')

    def testImagenSuillus(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/suillus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.ID, "texto-hongos").text.__contains__('Suillus')

    def testSinHongosRegistrados(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        assert self.driver.find_element(By.ID, "hongos_registrados").text.__contains__('Aún no has registrado ningún hongo')

    def testRegistrarHongos(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/agaricus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        self.driver.find_element(By.ID, "home").click()
        assert self.driver.find_element(By.ID, "div-lista-hongos").text.__contains__('Agaricus')
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/boletus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        self.driver.find_element(By.ID, "home").click()
        assert self.driver.find_element(By.ID, "div-lista-hongos").text.__contains__('Agaricus')

    def testBusqueda(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/agaricus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/boletus.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        self.driver.find_element(By.ID, "barra-busqueda").send_keys('agari')
        self.driver.find_element(By.ID, "submit-busqueda").click()
        
        assert self.driver.find_element(By.ID, "div-lista-hongos").text.__contains__('Agaricus')

        self.driver.find_element(By.ID, "barra-busqueda").send_keys('bolet')
        self.driver.find_element(By.ID, "submit-busqueda").click()
        
        assert self.driver.find_element(By.ID, "div-lista-hongos").text.__contains__('Boletus')

    def testImagenDataset(self):
        print(settings.BASE_DIR)
        ruta = "/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/imagen_dataset.jpg"
        tamanio = os.stat(ruta).st_size
        picture = PIL.Image.open(ruta)
        alto, ancho = picture.size
        resolucion = str(alto) + 'x' + str(ancho)
        imagenDataset = ImagenDataset(
                    especie="Cortinarius", tamanio=tamanio, resolucion=resolucion, nombre_archivo="imagen_dataset.jpg")
        imagenDataset.save()
        
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, "username").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys("dummy")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "clasificar").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys('/home/pablo/hongOS/hongOS_project/hongOS_app/test_data/imagen_dataset.jpg')
        self.driver.find_element(By.ID, "form_button").click()
        assert self.driver.find_element(By.XPATH, "//*[contains(text(), 'Es probable que la imagen que haya subido se haya usado para entrenar el modelo de clasificación.')]").text == 'Es probable que la imagen que haya subido se haya usado para entrenar el modelo de clasificación.'
