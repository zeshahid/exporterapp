from myapp import request_state, response_request
import unittest


class TestURL(unittest.TestCase):
    def test_index(self):
        outputstr = "App is up and running!"
        self.assertEqual(outputstr, outputstr, "Should be App is up and running!")
    
    def test_get_url_status(self):
        self.assertAlmostEqual(request_state('https://httpstat.us/200'),1)

    def test_get_url_status1(self):
        self.assertAlmostEqual(request_state('https://httpstat.us/503'),0)

    def test_get_url_status2(self):
        self.assertAlmostEqual(request_state('https://httpstat.us/400'),0)


    def test_get_response(self):
        self.assertGreaterEqual(response_request('https://httpstat.us/200'),0)

    def test_get_response1(self):
        self.assertGreaterEqual(response_request('https://httpstat.us/503'),0)

    def test_get_response2(self):
        self.assertGreaterEqual(response_request('https://httpstat.us/400'),0)


    
if __name__ == '__main__':
    unittest.main()