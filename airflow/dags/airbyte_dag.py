#imports
from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.sensors import ExternalTaskSensor
from airflow.models.baseoperator import chain
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

#tasks
gcs_product_to_postgres_task = AirbyteTriggerSyncOperator(
     task_id = 'gcs_product_to_postgres_sync',
     airbyte_conn_id = 'airbyte_connection_id_set_in_airflow',
     connection_id = 'ID of the airbyte connection to be triggered by airflow. gcs_product_to_postgres_sync_url_on_airbyte',
     asynchronous = False,
     timeout = 3600,
     wait_seconds = 3,
     dag = airbyte_dag
)

gcs_user_to_postgres_task = AirbyteTriggerSyncOperator(
     task_id = 'gcs_user_to_postgres_sync',
     airbyte_conn_id = 'airbyte_connection_id_set_in_airflow',
     connection_id = 'ID of the airbyte connection to be triggered by airflow. gcs_user_to_postgres_sync_url_on_airbyte',
     asynchronous = False,
     timeout = 3600,
     wait_seconds = 3,
     dag = airbyte_dag
)

gcs_cart_to_postgres_task = AirbyteTriggerSyncOperator(
     task_id = 'gcs_cart_to_postgres_sync',
     airbyte_conn_id = 'airbyte_connection_id_set_in_airflow',
     connection_id = 'ID of the airbyte connection to be triggered by airflow. gcs_cart_to_postgres_sync_url_on_airbyte',
     asynchronous = False,
     timeout = 3600,
     wait_seconds = 3,
     dag = airbyte_dag
)
 

wait_for_api_to_gcs_completion = ExternalTaskSensor(
    task_id='wait_for_api_to_gcs_dag_completion', #ID of this task
    external_dag_id='api_to_gcs_dag', #Dag id of the DAG to be completed first--api_to_gcs_dag.py
    external_task_id= 'api_user_to_gcs', # task IDs in the first DAG to be completed
    mode='reschedule',  # This means it will keep polling until the dependency is met
    poke_interval = 60,  # Interval between polling attempts
    dag = airbyte_dag,
    allowed_states = ['success']
)

#set tasks dependencies
#chain(wait_for_api_to_gcs_completion,[gcs_product_to_postgres_task, gcs_user_to_postgres_task, gcs_cart_to_postgres_task]) 
wait_for_api_to_gcs_completion >> [gcs_product_to_postgres_task, gcs_user_to_postgres_task, gcs_cart_to_postgres_task] 
