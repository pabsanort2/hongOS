import os
from pathlib import Path
from fastbook import load_learner
from django.test import TestCase
from django.conf import settings

# Create your tests here.

class testModel(TestCase):

    def test_agaricus_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/agaricus.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Agaricus')

    def test_amanita_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/amanita.jpeg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Amanita')
    
    def test_boletus_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/boletus.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Boletus')

    def test_cortinarius_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/cortinarius.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Cortinarius')

    def test_entoloma_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/entoloma.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Entoloma')

    def test_hygrocybe_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/hygrocybe.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Hygrocybe')

    def test_lactarius_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/lactarius.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Lactarius')

    def test_russula_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/russula.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Russula')

    def test_suillus_image(self):
        imagePath = os.path.join(settings.BASE_DIR, 'hongOS_app/tests/data/suillus.jpg')
        learner = load_learner(os.path.join(settings.BASE_DIR, '89,1207.pkl'))
        pred, pred_idx, probs = learner.predict(imagePath)
        nombre_hongo = pred
        self.assertEqual(nombre_hongo, 'Suillus')