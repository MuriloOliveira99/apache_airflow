from airflow import DAG
from airflow.operators.bash import BashOperator
# DummyOperator agora se chama EmptyOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id='task_dummy_1', 
    description='Exemplo 1: Task Dummy',
    schedule_interval=None,
    start_date=datetime(2023,3,5),
    catchup=False
) as dag:

    task1 = BashOperator(task_id = 'tsk1', bash_command='sleep 1')
    task2 = BashOperator(task_id = 'tsk2', bash_command='sleep 1')
    task3 = BashOperator(task_id = 'tsk3', bash_command='sleep 1')
    task4 = BashOperator(task_id = 'tsk4', bash_command='sleep 1')
    task5 = BashOperator(task_id = 'tsk5', bash_command='sleep 1')
    task_dummy = EmptyOperator(task_id='task_dummy')

    # airflow n suporta lista >> lista
    # [task1, task2, task3] >> [task4, task5]

    # O CORRETO A SE FAZER É: Importar o dummyOperator(EmptyOperator)
    [task1, task2, task3] >> task_dummy >> [task4, task5]
