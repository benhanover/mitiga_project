# Mitiga Home Project

This is a small project that serves 2 html pages both locally and on remotely.
Technologies: Kubernetes, Docker, Pulumi, Nginx, Google Cloud SDK


### GKE - BONUS
Using GKE and basic yaml files: https://35.193.213.0/index.html , https://35.193.213.0/welcome.html

### Minikube - 

1. Clone the repo
``` bash
git clone https://github.com/benhanover/mitiga_project.git
cd ./mitiga_project
```

2. Create Self Signed SSL
```bash
cd ./resources
mkdir certs
cd certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./nginx-selfsigned.key -out ./nginx-selfsigned.crt
```

3. Build the image
```bash
cd ../../
docker build -t mynginx ./
```

4. Start minikube
```bash
minikube start
```
5. Push mynginx into minikube docker registry using this tutorial: 
https://minikube.sigs.k8s.io/docs/handbook/registry/

6. Run pulumi
```bash
cd ./pulumi_minikube
pulumi up
```

7. Find HTTP and HTTPS IP adresses
```bash
minikube service nginx-service
```




![pulumi up](./images/pulumi%20up.png)
![pods](./images/pods.png)
![pod description 1](./images/pod%20description%201.png)
![pod description 2](./images/pod%20description%202.png)
![volumes](./images/volumes.png)
![URL's](./images/URL'S.png)
![HTTP](./images/HTTP.png)
![HTTPS](./images/HTTPS.png)

