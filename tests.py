import unittest
import flask_app  # flask app name

class FizzBuzzTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flask_app.app.test_client()

    def test_fizz_buzz(self):
        response = self.app.get('/fizzbuzz?int1=3&str1=fizz&int2=5&str2=buzz&limit=15')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz'])

    def test_stats(self):
        response = self.app.get('/stats')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'int1': 3, 'int2': 5, 'str1': 'fizz', 'str2': 'buzz', 'limit': 15, 'count': 1})

if __name__ == '__main__':
    unittest.main()
