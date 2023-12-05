#imports
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
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

#define task to navigate to dbt directory and build the dbt models
run_dbt_task = BashOperator(
    task_id = 'run_dbt',
    bash_command = 'cd /opt/airflow/dbt && dbt build --profiles-dir .',
    dag = dbt_dag
)

