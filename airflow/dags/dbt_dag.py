#imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.sensors import ExternalTaskSensor
from datetime import datetime, timedelta

#Set up defaults arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 2),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 5)

}

#dag 
dbt_dag = DAG(
    'dbt_build_dag',
    default_args = default_args,
    description = 'This DAG runs dbt build command',
    schedule_interval = None
)

#directory path of dbt project
#dbt_proj_dir = '/opt/airflow/dbt'

#define the dbt build command
#dbt_build_comm = f'dbt build --profiles-dir {dbt_proj_dir}'

#airflow task
#run_dbt_build = BashOperator(
    #task_id = 'run_dbt_build',
    #bash_command = dbt_build_comm,
    #dag = dag
#)

run_dbt_task = BashOperator(
    task_id = 'run_dbt',
    bash_command = 'cd /opt/airflow/dbt && dbt build --profiles-dir .',
    dag = dbt_dag
)

#set task dependencies
wait_for_airbyte_dag_completion_task = ExternalTaskSensor(
    task_id='wait_for_airbyte_dag_completion', #ID of this task
    external_dag_id='airbyte_trigger_dag', #Dag id of the DAG to be completed first--airbyte_dag.py
    external_task_id= ['gcs_product_to_postgres_task', 'gcs_user_to_postgres_task', 'gcs_cart_to_postgres_task'], # task IDs in the first DAG to be completed
    mode = 'reschedule', # This means it will keep polling until the dependency is met
    poke_interval = 120, # Interval between polling attempts
    dag = dbt_dag
)

wait_for_airbyte_dag_completion_task >> run_dbt_task