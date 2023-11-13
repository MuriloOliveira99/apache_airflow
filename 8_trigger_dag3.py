from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule

with DAG(
    dag_id='trigger_dag3',
    description='Trigger DAG 3',
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False) as dag:

    task1 = BashOperator(
            task_id='tsk1',
            bash_command='exit 1')

    task2 = BashOperator(
            task_id='tsk2',
            bash_command='exit 1')

    # all_failed: A tarefa é executada se todas as tarefas anteriores falharam.
    task3 = BashOperator(
            task_id='tsk3',
            bash_command='sleep 5',
            trigger_rule=TriggerRule.ALL_FAILED)

    [task1, task2] >> task3