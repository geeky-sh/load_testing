# Containerisation testing on local

(the name load_testing is deceptive. Beware!)

### To run the app without docker
```sh
export FLASK_APP="app.app:app"
flask run

# OR
gunicorn app.app:app
```

### Steps for configuring docker and kubectl:
- Install [minikube](https://minikube.sigs.k8s.io/docs/start/)
- create dockerfile for the project you are running
  - VSCode provides a docker plugin which automatically generates the docker file depending on the type of application
- Test dockerfile and see if the application is running properly (See docker commands for more help)
- Create `deployment.yaml` that contains deployment config for k8s
- Create `service.yaml` that contains service config for k8s

Docker Standalone helpful commands:

```sh
docker build -f Dockerfile -t load_testing:v1 . # build image
docker run -p 5000:5000 load_testing:v1 # run container
```

Kubernetes Orchestration Steps for local:

```sh
minikube start # start local k8s cluster
kubectl create --filename deployment.yaml # create deployment in cluster
kubectl create --filename service.yaml # create service in cluster
minikube load image load_testing:v1 # get locally built image into minikube cluster
kubectl get all # get details of all pods, deployments, services
minikube tunnel # creates a tunnel from localip to all the loadbalancer services. Basically access the service from local
minikube service --url <service-name> # to get the customer url + port through which one can access the service

kubectl delete -f service.yaml # delete resource (deployment / service)
kubectl delete <resource> <name> # delete resource (deployment / service)
minikube delete # delete local kubernetes cluster

kubectl logs <resource>/<name> -f # view logs -f is for follow
kubectl exec -it pod/load-testing-5b696fc88c-57fdl -- /bin/bash # to get in a shell of a particular pod
kubectl port-forward pod/load-testing-5b696fc88c-57fdl 8000:5000 # forwarding port for a particular pod from local to pod. This is used for testing whether pod APIs are working fine
```

## How to make life easy
Add the below lines in `~/.zshrc` or `~/.bashrc`
```sh
alias d="docker"
alias di="docker image"
alias dc="docker container"
alias dr="docker run"
alias kl="kubectl"
alias mk="minikube"
```

## Remaining learnings:
- Learn autoscale strategies and how to implement them
- Check how can images be loaded from remote server


## Ref:
- https://minikube.sigs.k8s.io/docs/handbook/accessing/ (for tunneling basically)
- https://thecodinginterface.com/blog/flask-rest-api-minikube/ (very helpful)

