from typing import Counter
from prometheus_client import start_http_server, Summary, Counter, Gauge ,__all__ ,Histogram
import random
import time

from requests import get
import requests
from requests.api import post 
urls =["https://httpstat.us/503","https://httpstat.us/200"]

sitestatus = Gauge('sample_external_url_up', 'site status check', ['endpoint'])
response_time = Gauge('sample_external_url_response_ms', 'Response Time in milliseconds', ['endpoint'])

# Create a metric to track time spent and requests made.
def response_request (url):
        response = requests.get(url)
      
        response_time.labels(endpoint=a).set(response.elapsed.total_seconds()/1000)
        # response_time2.labels(endpoint=a).observe(response.elapsed.total_seconds())
# Create a metric to for status
def request_state (a):
        response = requests.get(a)
        if response.status_code == 503:
            sitestatus.labels(endpoint=a).set(0)
        elif  response.status_code == 200:
            sitestatus.labels(endpoint=a).set(1)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        for a in urls:
    
            request_state (a)
            response_request (a)
