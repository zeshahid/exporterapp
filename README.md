# Prometheus exporterapp 
Prometheus exporter for monitoring website status and response times



* [Installation](#Installation)
    * [Deploy using Helm Charts](#Deploy-using-Helm-Charts)   
    * [Run Only Exporter app on docker](#Run-only-exporter-on-docker)
    * [How to only exporter app on kubernetes](#Run-exporter-in-kubernetes)
    * [Run Prometheus & Grafana with app ](#Run-Prometheus-&-Grafana-with-app)
     



## Installation

Requirements app can be deployed as docker conaiter, kubernetes deployement with grafana and prometheus or using helm chart details are listed below.
## Deploy using Helm Charts
 
You can run the app using helm chart as below  

```sh 
git clone https://github.com/zeshahid/exporterapp.git
cd exporterapp

helm install {app-name} .\helmexporterapp\
or 
helm upgrade --install {app-name} .\helmexporterapp\  
```
## Run only exporter on docker

Run the below to launch the container and open http://localhost:8000 in browser 

```sh
docker run -d -p 8000:8000 zeeshanshahid/exporterapp:1.1
```
## Run exporter in kubernetes 
 kubernetes manifests are in the [exporterapp/k8smanifest](exporterapp/k8smanifest/) directory and can be deployed as is. 
 The manifests will create a exporterapp namespace as well as a deployment and service.  Prometheus scrape configuration are listed here (#prometheus-conf) .

 ```sh 
 kubectl apply -f main.yaml
 ```

## Run Prometheus & Grafana with app 
if you don no have the prometherus and grafana already setup you can use [exporterapp/k8smanifest/garfana](exporterapp/k8smanifest/garfana) and [exporterapp/k8smanifest/prometheus](exporterapp/k8smanifest/prometheus) to deploy Or ulternatively you can use below command to apply all .

```sh
git clone https://github.com/zeshahid/exporterapp.git
cd exporterapp/k8smanifest/
 kubectl apply -R -f .
```


### Build the Image for the python app

```sh
cd exporterapp/exporter
docker build -t image name  .
```
# Prometheus scrape configuration
Here is an example scrape configuration for the exporter:

```sh
   - job_name: 'exporterapp'
     scrape_interval: 10s
     honor_labels: true
     static_configs:
       - targets: ['exporterapp:8000']
```
### Urls 

```sh
exporter Application: http://localhost:8000/metrics
Prometheus: http://localhost:9090/
Grafana: http://localhost:3000/
```
## Metrics

```sh
# HELP sample_external_url_up site status check
# TYPE sample_external_url_up gauge
sample_external_url_up{endpoint="https://httpstat.us/503"} 0.0
sample_external_url_up{endpoint="https://httpstat.us/200"} 1.0
# HELP sample_external_url_response_ms Response Time in milliseconds
# TYPE sample_external_url_response_ms gauge
sample_external_url_response_ms{endpoint="https://httpstat.us/503"} 0.000266561
sample_external_url_response_ms{endpoint="https://httpstat.us/200"} 0.000270083
```