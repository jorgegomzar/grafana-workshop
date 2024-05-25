
# Grafana configuration

1. Configure the data sources
![00_data_sources.png](./media/00_data_sources.png)

2. Configure the prometheus data source
![01_grafana_prometheus_data_source_config.png](01_grafana_prometheus_data_source_config.png)

3. Set 3 dashboards
![02_grafana_dashboards.png](02_grafana_dashboards.png)

    - Grafana CSV INE
    ![03_grafana_csv_ine.png](03_grafana_csv_ine.png)

        - Query config (screenshot only shows 1, but data.csv contains info for Sexo = Total, Hombre and Mujer)
        ![04_grafana_csv_ine_query.png](04_grafana_csv_ine_query.png)

    - Grafana prometheus self monitoring
    ![05_grafana_prometheus_self_monitoring.png](05_grafana_prometheus_self_monitoring.png)

    - Grafana prometheus monitoring other apps
    ![06_grafana_prometheus_monitoring_other_apps.png](06_grafana_prometheus_monitoring_other_apps.png)

        - Query config
        ![07_grafana_prometheus_monitoring_other_apps_query.png](07_grafana_prometheus_monitoring_other_apps_query.png)
