# 1. Base image = Airflow + its own Python (Env A). Already sets AIRFLOW_HOME=/opt/airflow.
FROM apache/airflow:2.10.5-python3.12

# 2. Paths for Dag
ENV PROJECT=/opt/airflow
ENV MARKET_INTEL_PY=/opt/venvs/market-intel/bin/python
ENV DBT=/opt/venvs/market-intel/bin/dbt
ENV DBT_PROFILES_DIR=/opt/airflow/market_intel

# 3. Make the pipeline venv (Env B)
USER root
RUN mkdir -p /opt/venvs && chown airflow: /opt/venvs
USER airflow
RUN python -m venv /opt/venvs/market-intel

# 4. Install project (pyproject deps + src) + dbt into Env B.
COPY --chown=airflow:0 pyproject.toml /opt/airflow/project/pyproject.toml
COPY --chown=airflow:0 src            /opt/airflow/project/src
RUN /opt/venvs/market-intel/bin/pip install --no-cache-dir /opt/airflow/project

# 5. Bake your dags + dbt project into the image (immutable, self-contained).
COPY --chown=airflow:0 dags         /opt/airflow/dags
COPY --chown=airflow:0 market_intel /opt/airflow/market_intel
