from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.azure.compute import VM
from diagrams.gcp.compute import ComputeEngine
from diagrams.onprem.monitoring import Grafana, Prometheus


with Diagram("Cloud monitoring", show=False):
    metrics = Prometheus("Prometheus")
    metrics << Grafana("Grafana") << metrics

    with Cluster("Compute cluster"):
        compute = [
            EC2("AWS EC2"),
            VM("Azure VM"),
            ComputeEngine("GCP Compute Engine"),
        ]

    compute >> metrics
