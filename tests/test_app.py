import unittest
import requests

class TestTemperatureApp(unittest.TestCase):
    BASE_URL = 'http://localhost:5000' 

    def test_home_page(self):
        response = requests.get(f'{self.BASE_URL}/')
        
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
