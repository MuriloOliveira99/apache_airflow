from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'terceira_dag_precedencia',
    description = 'precedência',
    schedule_interval = None,
    start_date = datetime(2023, 3, 5),
    catchup = False
)

task1 = BashOperator(
    task_id = 'tsk1',
    bash_command = 'sleep 5',
    dag = dag
)

task2 = BashOperator(
    task_id = 'tsk2',
    bash_command = 'sleep 5',
    dag = dag
)

task3 = BashOperator(
    task_id = 'tsk3',
    bash_command = 'sleep 5',
    dag = dag
)

# RODANDO AS TASKS COM PRECEDÊNCIA
# TASKS 1 e 2, DPS A TASKS 3
[task1, task2] >> task3