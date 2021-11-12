from typing import Counter
from prometheus_client import start_http_server, Summary, Counter
import random
import time
from requests import get
import requests
from requests.api import post 

# Create a metric to track time spent and requests made.
sitestatus = Counter('sample_external_url_up', 'site status check',['endpoint'])

@sitestatus.collect()
def response_request (url):
        response = requests.get(url)
        if response.status_code == 503:
            return  0
            print("down")
        else:
            return 1
            print("up")

        # print (response.status_code)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    url1 =  "https://httpstat.us/503"
    start_http_server(8100)
    # Generate some requests.
    while True:
        response_request (url1)