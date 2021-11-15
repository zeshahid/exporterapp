import myapp
from unittest.mock import Mock, patch
import unittest
url = 'https://httpstat.us/200'
# class Testexporterapp(unittest.TestCase):
# test response_request and expect 200
def test_response():
    with patch('requests.get') as mock_req:
        mock_req.return_value.status_code = 200
        assert myapp.response_request(url) == 200

# test response_request and expect 503
def test_response():
    with patch('requests.get') as mock_req:
        mock_req.return_value.status_code = 503
        assert myapp.response_request(url) == 503




if __name__ == "__main__":
        unittest.main()