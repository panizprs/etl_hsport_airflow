""" one task dag """

from airflow.operators.python import PythonOperator
from airflow import DAG
import products_etl_logic
from datetime import datetime

default_args = {
        'owner': 'Paniz',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
        'catchup': False,
        'start_date': datetime(2024, 3, 25)
}

with DAG(
        dag_id='products_dag',
        description='An Airflow DAG to load products',
        schedule_interval=None,
        default_args=default_args
    ) as dag:
        transform_task = PythonOperator(
                task_id='products_task',
                python_callable=products_etl_logic.main,
                dag=dag)
