from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(dag_id='dag_executa_dag', description='DAG que executa DAG', schedule_interval=None, start_date=datetime(2023, 3, 5), catchup=False) as dag:

    task1 = BashOperator(
        task_id='tsk1',
        bash_command='sleep 5')
    
    task2 = TriggerDagRunOperator(
        task_id='tsk2',
        trigger_dag_id='dag_taskgroup')
    
    task1 >> task2
    



