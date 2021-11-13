from typing import Counter
from prometheus_client import start_http_server, Summary, Counter, Gauge ,__all__
import random
import time

from requests import get
import requests
from requests.api import post 
urls =["https://httpstat.us/503","https://httpstat.us/200"]

# Create a metric to track time spent and requests made.
# sitestatus = Gauge('sample_external_url_up', 'site status check')
# std_lables=["url1"]
sitestatus = Gauge('sample_external_url_up', 'site status check', ['endpoint'])

def response_request (a):
        response = requests.get(a)
        if response.status_code == 503:
            # sitestatus.labels(url1)
            print("down")
            # sitestatus.set(23)
            sitestatus.labels(endpoint=a).set(0)
        elif  response.status_code == 200:
            print("up")
            # sitestatus.set(23)
            sitestatus.labels(endpoint=a).set(1)
        # else:
        #     print("up")
        #     sitestatus.set(1)

        # print (response.status_code)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    url1 =  "https://httpstat.us/503"
    start_http_server(8100)
    # Generate some requests.
    while True:
        for a in urls:
            response_request (a)
        # sitestatus.labels(url1)