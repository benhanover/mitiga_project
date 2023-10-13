# Mitiga Home Project

This is a small project that serves 2 html pages locally.
Technologies: Kubernetes, Docker, Pulumi, Nginx

### Getting Started

1. Install minikube and run 
```bash
minikube start
```
2. Cd into the project and build the image
```bash
 docker build -t mynginx .
```
3. Push mynginx into minikube docker registry using this tutorial: https://minikube.sigs.k8s.io/docs/handbook/registry/
4. Cd inside pulumi directory and run
```bash
 pulumi up
```
5. Test HTTP and HTTPS 
```bash
minikube service nginx-service
```
6. run the URL's provided 

![pulumi up](./images/pulumi%20up.png)
![pods](./images/pods.png)
![pod description 1](./images/pod%20description%201.png)
![pod description 2](./images/pod%20description%202.png)
![volumes](./images/volumes.png)
![URL's](./images/URL'S.png)
![HTTP](./images/HTTP.png)
![HTTPS](./images/HTTPS.png)

