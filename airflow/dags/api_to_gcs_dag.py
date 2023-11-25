#imports
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models.baseoperator import chain
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime, timedelta
from datetime import datetime, timedelta 
from packages.functions import get_and_extract_fakestore_product_to_gcs
from packages.functions import get_and_extract_fakestore_cart_to_gcs
from packages.functions import get_and_extract_fakestore_users_to_gcs
import os

# set environment variableS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/opt/airflow/creds/merch-store-399816-963a8ea93cb6.json"


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
api_to_gcs_dag = DAG(
    'api_to_gcs_dag',
    default_args = default_args,
    description = 'This DAG loads data to destination GCS from Fakestore API',
    schedule_interval = None
)

#extract data from fakestore api to gcs destination tasks
api_product_to_gcs_task = PythonOperator(
    task_id = 'api_product_to_gcs',
    python_callable = get_and_extract_fakestore_product_to_gcs,
    op_kwargs = {'destination_gcs_path':'fakestore/fakestore_product/fakestore_product.csv'},
    dag = api_to_gcs_dag
)

api_cart_to_gcs_task = PythonOperator(
    task_id = 'api_cart_to_gcs',
    python_callable = get_and_extract_fakestore_cart_to_gcs,
    op_kwargs = {'destination_gcs_path':'fakestore/fakestore_cart/fakestore_cart.csv'},
    dag = api_to_gcs_dag
)

api_user_to_gcs_task = PythonOperator(
    task_id = 'api_user_to_gcs',
    python_callable = get_and_extract_fakestore_users_to_gcs,
    op_kwargs = {'destination_gcs_path':'fakestore/fakestore_user/fakestore_user.csv'},
    dag = api_to_gcs_dag
)

trigger_airbyte_dag_task = TriggerDagRunOperator(
    task_id ='trigger_airbyte_dag',
    trigger_dag_id = 'airbyte_trigger_dag', # Dag id of the dag to trigger -- airbyte_dag.py
    dag = api_to_gcs_dag,
    wait_for_completion = True
)

#set task dependencies
#chain([api_product_to_gcs_task, api_cart_to_gcs_task, api_user_to_gcs_task] trigger_airbyte_dag_task) 
api_product_to_gcs_task >> api_cart_to_gcs_task >> api_user_to_gcs_task >> trigger_airbyte_dag_task