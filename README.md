# FAKE STORE PROJECT
For this project, we consider a case where data has to be retrieved from an API, Fakestore API , and data retrieved stored in a staging zone, Google Cloud Storage Bucket, which serves as the source of data for Extract-Load (EL) phase of the ELT pipeline. The Extract-Load phase will be carried out using Airbyte which is an open source data integration engine that provides the ability to connect data source to destination with ease. Just the click of buttons and the data integration sync is created. After data is loaded in the data warehouse, PostgreSQL for this project, dbt is used to perform data transformation on the data warehouse, this way, data does not have to be extracted from the data warehouse to perform data transformation.  The entire process is orchestrated using Apache Airflow which is a powerful open source data orchestration tool.

# Project Requirements and Dependencies

VS code 

Apache Airflow

Airbyte

Docker desktop

DBT adapter

PostgreSQL Database

Gmail account

Google Cloud Account

Google Cloud Storage Bucket

Virtualization and WSL enabled (if using windows PC) – refer to this link to do so:

# How To Make Use Of The Project

Link to medium article:

https://medium.com/@chibuokejuliet/modern-data-stack-airbyte-dbt-and-apache-airflow-5339c72e3296
