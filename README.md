# Grafana Workshop

## Overview

This repo aims to be a PoC for Grafana monitoring.

Everything is configured to be run with docker compose.

Currently contains the following stats (although it requires a bit of manual work to set up the dashboards using the available data sources):

- Prometheus
    - metrics for self
    - metrics for 3 node exporters to demo resource monitoring using Prometheus
- CSV information from INE

For an extensive explanation for the manual configuration see [GRAFANA_CONFIG.md](GRAFANA_CONFIG.md)

## Related documentation
- [Grafana documentation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)
- [Grafana plugins](https://grafana.com/grafana/plugins)
- [Prometheus getting started](https://prometheus.io/docs/prometheus/latest/getting_started/#configure-prometheus-to-monitor-the-sample-targets)
- [Prometheus node exporter](https://prometheus.io/docs/guides/node-exporter/)

## Requirements

- Make (optional, you could run the commands in the Makefile manually but if you already have it should make your life easier).
- Docker
- Docker compose
- Python3.11+

## Instructions

1. Run `make generate_csv` to set up the venv + poetry + download the data.csv sample
2. Run `make up` to raise the Docker containers with the needed configuration

After this, you should have the [app running in local](http://localhost:3000).

You can add new data sources and configure the Dashboard as you want!
