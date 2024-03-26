from airflow.operators.python import PythonOperator
from airflow import DAG
import orders_etl_logic
from datetime import datetime

with DAG(
    dag_id='orders_dag',
    schedule_interval=None,
    start_date=datetime(2024, 3, 26),
    catchup=False) as dag:
    transform_task = PythonOperator(
        task_id='orders_task',
        python_callable=orders_etl_logic.main,
        dag=dag)