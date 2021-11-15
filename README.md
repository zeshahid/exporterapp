# websitecheck_exporter
Prometheus exporter for monitoring website status and response times



# exporterapp ProPrometheus exporterm

* [Installation](#Installation)
* [How to only exporter app on kubernetes](# Run-only-exporter:)
    * [Run Prometheus & Grafana with app ](#Run Prometheus & Grafana with app )
    * [Deploy using Helm Charts](#Deploy using Helm Charts)    



## Installation

## Run only exporter:
 kubernetes manifests are in the [exporterapp/k8smenifests](exporterapp/k8smenifests/) directory and can be deployed as is. 
 The manifests will create a exporterapp namespace as well as a deployment and service.  Prometheus scrape configuration are listed [below](#prometheus conf) .

 ```sh 
 kubectl apply -f main.yaml
 ```

## Run Prometheus & Grafana with app 
if you don no have the prometherus and grafana already setup you can use (exporterapp/k8smenifests/garfana) and (exporterapp/k8smenifests/prometheus) to deploy Or ulternatively you can use below command to apply all .

```sh
git clone https://github.com/zeshahid/exporterapp.git
cd exporterapp/k8smenifests/
 kubectl apply -R -f .
```

## Deploy using Helm Charts
 
if you 

```sh 
cd exporterapp

helm upgrade --install exporter .\helmexporterapp\  
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


## How to deploy on Kubernetes
