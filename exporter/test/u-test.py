from myapp import request_state, response_request
import unittest
# urls =["https://httpstat.us/503","https://httpstat.us/200","https://google.com"]
urls =["https://httpstat.us/503"]
# class Testexporterapp(unittest.TestCase):
    # def test_index(self):
    #     outputstr = "App is up and running!"
    #     self.assertEqual(outputstr, outputstr, "Should be App is up and running!")
    
def test_status(self):
    self.assertAlmostEqual(request_state('https://httpstat.us/503'),1)


    # def test_status1(self):
    #     for a in urls:
    #         self.assertAlmostEqual(request_state('https://httpstat.us/503'),0)

    # def test_status2(self):
    #     for a in urls:
    #         self.assertAlmostEqual(request_state('https://google.com'),0)


    # def test_response(self):
    #     self.assertGreaterEqual(response_request('https://httpstat.us/200'),0)

    # def test_response1(self):
    #     self.assertGreaterEqual(response_request('https://httpstat.us/503'),0)

    # def test_response2(self):
    #     self.assertGreaterEqual(response_request('https://google.com'),0)
if __name__ == "__main__":
    unittest.main()

    
# if __name__ == '__main__':
#     unittest.main()