from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule

with DAG(
    dag_id='trigger_dag1',
    description='Trigger DAG 1',
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False) as dag:

    task1 = BashOperator(
            task_id='tsk1',
            bash_command='sleep 5')

    task2 = BashOperator(
            task_id='tsk2',
            bash_command='sleep 5')

    # one_failed: A tarefa é executada se pelo menos uma das tarefas anteriores falhou
    task3 = BashOperator(
            task_id='tsk3',
            bash_command='sleep 5',
            trigger_rule=TriggerRule.ONE_FAILED)

    [task1, task2] >> task3