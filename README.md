## This repository contains code for creating the web service using following steps
> 1. Creating REST full web application using Python and Flask

> 2. Dockerising the web application.
```
cd  /pathtodockerfile
```

command to build the image from Dockerfile
```
sudo docker build -t timestamp-service .
```

command to tag and push the image to Docker hub
```
sudo docker tag timestamp-service:latest samiksha34/centos:firstimage
sudo docker push samiksha34/centos:firstimage
```


> 3. Deploying the Docker image in minikube cluster.
I have written 3 files deployment.yaml, service.yaml and ingress.yaml and created these files using below commands.
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Once the service has been created, We can access the web service using port forwarding to test it.
Using below command we are forwading the request to access the application from localz available port to the port where Service is listing, however it is still accessible from within the cluster.
```
kubectl port-forward service/timestamp-service 8080:80
```

* To make web service available over the internet we need to create a ingress service. 
* To enable the ingress service we need to configure ingress controller. 
* I have configured nginx ingress controller in our usecase
* To make this service accessible by everyone we need to map the kubernetes api server ip/loadbalancer ip to a DNS name in a valid DNS registra which i have not used yet in our case. In our case I created a DNS in /etc/hosts file locally and passed the DNS name in host field in ingress.yaml
* we can access the web service over the internet using DNSname:Nodeport

```
kubectl apply -f ingress.yaml
```

> 4. Monitoring the application using Promeatheus in Kubernetes.

* To monitor the service in kubernetes, I configured Prometheus operator using helm. and configured service monitor so prometheus can scrap the metrics from it and pass to grafana.

```
kubectl apply -f service-monitor.yaml
```
