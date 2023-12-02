from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# dicionario de argumentos padrão que serão aplicados a todas as tarefas
# da DAG, a menos que sejam especificamente substituidos.
default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 5),
    'email': 'murilo@gmail.com', # aceita lista de emails 
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}


with DAG(dag_id='criando_dag_com_dicionario',
         default_args=default_args, 
         description='Criando DAG com dicionario', 
         schedule_interval='@hourly', 
         start_date=datetime(2023, 3, 5), 
         catchup=False,
         default_view='graph',
         tags=['processo', 'tag', 'pipeline']) as dag:
    
    task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', retries=3)
    task2 = BashOperator(task_id='tsk2', bash_command='sleep 5')
    task3 = BashOperator(task_id='tsk3', bash_command='sleep 5')

    task1 >> task2 >> task3
    

    
    


