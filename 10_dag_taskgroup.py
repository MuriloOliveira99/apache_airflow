from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule
from airflow.utils.task_group import TaskGroup

with DAG(
    dag_id='dag_taskgroup',
    description='DAG Task Group',
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False) as dag:

    task1 = BashOperator(
        task_id='tsk1',
        bash_command='sleep 5'
    )

    task2 = BashOperator(
        task_id='tsk2',
        bash_command='sleep 5'
    )

    task3 = BashOperator(
        task_id='tsk3',
        bash_command='sleep 5'
    )

    task4 = BashOperator(
        task_id='tsk4',
        bash_command='sleep 5'
    )

    task5 = BashOperator(
        task_id='tsk5',
        bash_command='sleep 5'
    )

    task6 = BashOperator(
        task_id='tsk6',
        bash_command='sleep 5'
    )

    task_group = TaskGroup(
        'tsk_group'
    )

    task7 = BashOperator(
        task_id='tsk7',
        bash_command='sleep 5',
        task_group=task_group
    )

    task8 = BashOperator(
        task_id='tsk8',
        bash_command='sleep 5',
        task_group=task_group
    )

    # all_failed: A tarefa é executada se todas as tarefas anteriores falharam.
    task9 = BashOperator(
        task_id='tsk9',
        bash_command='sleep 5',
        trigger_rule=TriggerRule.ALL_FAILED,
        task_group=task_group

    )
    
    # https://prnt.sc/4flpfdPGTFAj
    # https://prnt.sc/ZqWTyiyUseBD
    task1 >> task2
    task3 >> task4
    [task2, task4] >> task5 >> task6
    task6>> task_group
