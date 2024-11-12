import unittest

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("División por cero no permitida")
        return a / b

    def valor_absoluto(self, a):
        return abs(a)

class TestCalculadora(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Método de setUp para inicializar la calculadora antes de todas las pruebas
        cls.calculadora = Calculadora()

    @classmethod
    def tearDownClass(cls):
        # Método de tearDown para limpiar después de todas las pruebas
        del cls.calculadora

    # Pruebas para el método suma
    def test_suma_positivos(self):
        # Clase de equivalencia: números positivos
        self.assertEqual(self.calculadora.suma(10, 5), 15)

    def test_suma_negativos(self):
        # Clase de equivalencia: números negativos
        self.assertEqual(self.calculadora.suma(-10, -5), -15)

    def test_suma_frontera(self):
        # Valor frontera: cero
        self.assertEqual(self.calculadora.suma(0, 0), 0)

    # Pruebas para el método resta
    def test_resta_positivos(self):
        # Clase de equivalencia: números positivos
        self.assertEqual(self.calculadora.resta(10, 5), 5)

    def test_resta_negativos(self):
        # Clase de equivalencia: números negativos
        self.assertEqual(self.calculadora.resta(-10, -5), -5)

    def test_resta_frontera(self):
        # Valor frontera: cero
        self.assertEqual(self.calculadora.resta(0, 0), 0)

    # Pruebas para el método multiplicacion
    def test_multiplicacion_positivos(self):
        # Clase de equivalencia: números positivos
        self.assertEqual(self.calculadora.multiplicacion(10, 5), 50)

    def test_multiplicacion_negativos(self):
        # Clase de equivalencia: números negativos
        self.assertEqual(self.calculadora.multiplicacion(-10, -5), 50)

    def test_multiplicacion_frontera(self):
        # Valor frontera: multiplicación por cero
        self.assertEqual(self.calculadora.multiplicacion(10, 0), 0)

    # Pruebas para el método division
    def test_division_positivos(self):
        # Clase de equivalencia: números positivos
        self.assertEqual(self.calculadora.division(10, 5), 2)

    def test_division_negativos(self):
        # Clase de equivalencia: números negativos
        self.assertEqual(self.calculadora.division(-10, -5), 2)

    def test_division_frontera(self):
        # Valor frontera: división de cero
        self.assertEqual(self.calculadora.division(0, 5), 0)

    def test_division_por_cero(self):
        # Prueba de excepción esperada
        with self.assertRaises(ValueError):
            self.calculadora.division(10, 0)

    # Pruebas para el método valor_absoluto
    def test_valor_absoluto_positivo(self):
        # Clase de equivalencia: valor positivo
        self.assertEqual(self.calculadora.valor_absoluto(10), 10)

    def test_valor_absoluto_negativo(self):
        # Clase de equivalencia: valor negativo
        self.assertEqual(self.calculadora.valor_absoluto(-10), 10)

    def test_valor_absoluto_frontera(self):
        # Valor frontera: cero
        self.assertEqual(self.calculadora.valor_absoluto(0), 0)

# Ejecución de las pruebas
if __name__ == '__main__':
    unittest.main()