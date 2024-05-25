# Grafana Workshop

- [Documentation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)
- [Plugins](https://grafana.com/grafana/plugins)

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
