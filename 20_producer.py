from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

with DAG(
    dag_id='producer',
    description='producer',
    schedule_interval=None,
    start_date=datetime(2023, 5, 3),
    catchup=False
) as dag:
    
    dataset = Dataset('/opt/airflow/data/Churn_new.csv')

    def meu_arquivo():
        dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
        dataset.to_csv('/opt/airflow/data/Churn_new.csv', sep=';')

    t1 = PythonOperator(
        task_id='tsk1', 
        python_callable=meu_arquivo,
        outlets=[dataset]) # avisa q a task vai atualizar o dataset