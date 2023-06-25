import unittest
import time

class Terceros(unittest.TestCase):
    def setUp(self):
        pass

    def test_producto_envio_domicilio1(self):
        self.assertEquals(2,2, "Fallo la prueba 1")

    def test_producto_envio_domicilio2(self):
        self.assertEquals(2,2, "Fallo la prueba 2")

    def test_producto_envio_domicilio3(self):
        self.assertEquals(2,3, "Fallo la prueba 3")