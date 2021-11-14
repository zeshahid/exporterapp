from typing import Counter
from prometheus_client import start_http_server, Summary, Counter, Gauge ,__all__
import random
import time

from requests import get
import requests
from requests.api import post 


from typing import Counter
from prometheus_client import start_http_server, Summary, Counter, Gauge ,__all__
import random
import time

from requests import get
import requests
from requests.api import post 

from prometheus_client import Counter
c = Gauge('my_requests_total', 'HTTP Failures', ['method', 'endpoint'])
c.labels(method='get', endpoint='/').inc()
c.labels(method='post', endpoint='/submit').inc()


def response_request (url):
        response = requests.get(url)
        if response.status_code == 503:
            # sitestatus.labels(url1)
            print("down")
            c.set(0)
            # c.labels(method='get', endpoint='/').inc()
          


        else:
            print("up")
            sitestatus.set(1)

        # print (response.status_code)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    url1 =  "https://httpstat.us/503"
    start_http_server(8700)
    # Generate some requests.
    while True:
        response_request (url1)
        # sitestatus.labels(url1)


