from prometheus_client import start_http_server, Counter, Gauge
from prometheus_client.parser import text_string_to_metric_families
import random
import time
import logging
import sys
import requests
import logging
import sys
import json

#logging
log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)


# a Python object (dict):



if __name__ == '__main__':
    start_http_server(8000)
    
    x = {
      "asctime": "2020-03-27 05:51:50,017",
      "levelname": "INFO",
      "message": "Testing logs with timestamp",
      "app_port": 8000
    }
    # convert into JSON:
    y = json.dumps(x)

    c = Counter('static_increment_counter', 'Counter that increments by 50 every 2 seconds')
    g = Gauge('static_increment_gauge', 'Gauge that increments by 50 every 2 seconds')

    c_rand = Counter('random_increment_counter', 'Counter that increments in a random fashion every 15 seconds')
    g_rand = Gauge('random_increment_gauge', 'Gauge that increments in a random fashion every 15 seconds')

    #i  = 1
    run = 0
    random.seed()

    while True:
        log.info("*******RUN %i **********",run)

        # Increment the counter and gauge by the same value at each run
        c.inc(50)
        g.inc(50)

        rand = random.randint(1,1000)
        c_rand.inc(rand)
        g_rand.inc(rand)
        log.info("Incremented Rand by {0}".format(rand))
        # Scrape endpoint to get metric values logged to stdout
        metrics = requests.get("http://localhost:8000/").content
        for family in text_string_to_metric_families(metrics.decode()):
            for sample in family.samples:
                 log.info("Name: {0} Labels: {1}  Value: {2}".format(*sample))
                 log.info("\"User email\": \"masked_user@example.com\"")
                 log.info(y)

        time.sleep(15)
        run+=1