#imports
from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime, timedelta


#Set up defaults arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 4),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 5)

}

#dag 
airbyte_dag = DAG(
    'airbyte_trigger_dag',
    default_args = default_args,
    description = 'This DAG triggers airbyte sync operation',
    schedule_interval = None
)

#define airbyte sync tasks to load data frm gcs to postgres

#gcs_product_to_postgres_task
gcs_product_to_postgres_task = AirbyteTriggerSyncOperator(
     task_id = 'gcs_product_to_postgres_sync',
     airbyte_conn_id = 'airbyte_connection_id_set_in_airflow',
     connection_id = 'ID of the airbyte connection to be triggered by airflow. gcs_product_to_postgres_sync_url_on_airbyte',
     asynchronous = False,
     timeout = 3600,
     wait_seconds = 3,
     dag = airbyte_dag
)

#gcs_user_to_postgres_task
gcs_user_to_postgres_task = AirbyteTriggerSyncOperator(
     task_id = 'gcs_user_to_postgres_sync',
     airbyte_conn_id = 'airbyte_connection_id_set_in_airflow',
     connection_id = 'ID of the airbyte connection to be triggered by airflow. gcs_user_to_postgres_sync_url_on_airbyte',
     asynchronous = False,
     timeout = 3600,
     wait_seconds = 3,
     dag = airbyte_dag
)

#gcs_cart_to_postgres_task
gcs_cart_to_postgres_task = AirbyteTriggerSyncOperator(
     task_id = 'gcs_cart_to_postgres_sync',
     airbyte_conn_id = 'airbyte_connection_id_set_in_airflow',
     connection_id = 'ID of the airbyte connection to be triggered by airflow. gcs_cart_to_postgres_sync_url_on_airbyte',
     asynchronous = False,
     timeout = 3600,
     wait_seconds = 3,
     dag = airbyte_dag
)
 
#trigger dbt task
trigger_dbt_dag_task = TriggerDagRunOperator(
    task_id ='trigger_dbt_dag',
    trigger_dag_id = 'dbt_build_dag', # Dag id of the dag to trigger -- airbyte_dag.py
    dag = airbyte_dag,
    wait_for_completion = True
)

#set task dependencies 
[gcs_product_to_postgres_task, gcs_user_to_postgres_task, gcs_cart_to_postgres_task] >> trigger_dbt_dag_task