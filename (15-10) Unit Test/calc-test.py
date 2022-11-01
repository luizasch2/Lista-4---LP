import unittest
import calc

def setUpModule():
    print('\nExecutando SetUpModule')

def tearDownModule():
    print('\nExecutando TearDownModule')

class TesteModuloQualidades(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nExecutando SetUpClass')
    
    @classmethod
    def tearDownClass(cls):
        print('\nExecutado TearDownClass')
    
    def setUp(self):
        print('\nExecutando SetUpModule')
    
    def tearDown(self) -> None:
        print('\nExecutando TearDownModule')
    

    #Teste da função add:
    def testcase_inteiros_negativo_negativo(self):
        print("Executando caso de teste: Inteiros - negativo e negativo")
        self.assertEqual(calc.add(-1, -1),-2)
       
    def testcase_decimais_positivo_positivo(self):
        print("Executando caso de teste: Decimais - positivo e positivo")
        self.assertAlmostEqual(calc.add(1.0, 1.0),2.0, 5)
       
    def testecase_decimais_negativo_negativo(self):
        print("Executando caso de teste: Decimais - negativo e negativo")
        self.assertAlmostEqual(calc.add(-1.0, -1.0),-2.0)

    #Teste da função substract
    def testcase_inteiros_positivo_positivo(self):
        print('\nExecutando caso de teste: inteiros - positivo e positivo ')
        self.assertEqual(calc.subtract(5,2),3)
    
    def testcase_inteiros_negativo_positivo(self):
        print('\nExecutando caso de teste: inteiros - negativo e positivo ')
        self.assertEqual(calc.subtract(-5,2),-7)
    
    def testcase_decimal_positivo_negativo(self):
        print('\nExecutando caso de teste: decimal - positivo e negativo ')
        self.assertAlmostEqual(calc.subtract(-5.0,2.0),-7.0)
    
    #Teste função multiply
    def testecase_inteiro_positivo_positivo(self):
        print('\nExecutando caso de teste: inteiro - positivo e positivo')
        self.assertEqual(calc.multiply(3,2),6)
    
    def testecase_inteiro_negativo_positivo(self):
        print('\nExecutando caso de teste: inteiro - negativo e positivo')
        self.assertEqual(calc.multiply(-3,2),-6)
    
    def testecase_inteiro_negativo_negativo(self):
        print('\nExecutando caso de teste: inteiro - negativo e negativo')
        self.assertEqual(calc.multiply(-3,-2),6)
    
    #Teste função divide

    def testecase_inteiro_positivo_negativo(self):
        print('\nExecutando caso de teste: inteiro - positivo e negativo')
        self.assertEqual(calc.divide(12,-2),-6)
    
    def testecase_inteiro_zero_positivo(self):
        print('\nExecutando caso de teste: inteiro - zero e positivo')
        self.assertEqual(calc.divide(0,10),0)
    
    def testecase_divisao_por_zero(self):
        with self.assertRaises(ValueError) as exception_context:
            calc.divide(10, 0)
            self.assertEqual(str(exception_context.exception),"you cannot divide by zero!")
    
    #Teste função exp

    def testecase_inteiro_par_negativo(self):
        print('\nExecutando caso de teste: inteiro - negativo e par')
        self.assertEqual(calc.exp(2,-3),9)
    
    def testecase_decimal_inteiro(self):
        print('\nExecutando caso de teste: decimal e inteiro')
        self.assertEqual(calc.exp(0.5,4),2)

    def teste_negativo_positivo(self):
        self.assertEqual(calc.exp(-2,2),1/4)    

if __name__ == "__main__":
    unittest.main(verbosity=2)

