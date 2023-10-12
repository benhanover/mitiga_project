import pulumi
import pulumi_kubernetes as k8s

app_labels = {"app": "nginx"}

# Define a PersistentVolumeClaim for the volume
pvc = k8s.core.v1.PersistentVolumeClaim(
    "my-pvc",
    spec={
        "accessModes": ["ReadWriteOnce"],
        "resources": {"requests": {"storage": "1Gi"}},
    },
)

# Define a Deployment of 4 replicas with resource requests and limits, that mounts the volume
deployment = k8s.apps.v1.Deployment(
    "app-dep",
    metadata={
        "labels": app_labels,
    },
    spec={
        "replicas": 4,
        "selector": {
            "matchLabels": app_labels,
        },
        "template": {
            "metadata": {"labels": app_labels},
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "localhost:5000/mynginx",  # Use the local Docker image named "mynginx"
                        "resources": {
                            "requests": {"cpu": "100m", "memory": "128Mi"},
                            "limits": {"cpu": "200m", "memory": "256Mi"},
                        },
                        "volumeMounts": [
                            {"name": "pvc", "mountPath": "/data"},
                        ],
                    },
                ],
                "volumes": [
                    {"name": "pvc", "persistentVolumeClaim": {"claimName": pvc.metadata["name"]}},
                ],
            },
        },
    },
)

# Define a Service to expose the nginx deployment via ClusterIP
service = k8s.core.v1.Service(
    "nginx-service",
    metadata={"name": "nginx-service"},
    spec={
        "selector": app_labels,
        "ports": [
            {"name": "http", "port": 80, "targetPort": 80},
            {"name": "https", "port": 443, "targetPort": 443},
        ],
        "type": "ClusterIP",  # Expose the service with ClusterIP type
    },
)

# Export the name of the deployment and service
pulumi.export("deployment_name", deployment.metadata["name"])
pulumi.export("service_name", service.metadata["name"])
