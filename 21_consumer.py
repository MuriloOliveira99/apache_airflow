from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

dataset = Dataset('/opt/airflow/data/Churn_new.csv')

with DAG(
    dag_id='consumer',
    description='consumer',
    schedule=[dataset],
    start_date=datetime(2023, 5, 3),
    catchup=False
) as dag:
    
    def meu_arquivo():
        dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
        dataset.to_csv('/opt/airflow/data/Churn_new2.csv', sep=';')

    t1 = PythonOperator(
        task_id='tsk1', 
        python_callable=meu_arquivo,
        provide_context=True) # avisa q a task vai atualizar o dataset