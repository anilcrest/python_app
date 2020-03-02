import unittest
from hello import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Hello world!')
        
    # def test_default_greeting_fail(self):
    #     greeter = Greeter()
    #     self.assertEqual(greeter.message, 'Hello !')

if __name__ == '__main__':
    unittest.main()
