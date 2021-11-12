from prometheus_client import start_http_server, Summary
import random
import time
from requests import get
import requests
from requests.api import post 

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('zeeshan_request_processing_seconds', 'Time spent processing request')
# REQUEST_TIME = Summary('zeeshan_request_processing_seconds', 'Time spent processing request')
# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


def response_request (url):
        response = requests.get(url)
        print (response)
        print(response.elapsed.total_seconds())


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    url1 =  "https://httpstat.us/503"
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        response_request (url1)