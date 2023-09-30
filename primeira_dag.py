from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime

# criando um objeto do tipo DAG
dag = DAG(
    'primeira_dag', # nome da tag
    description = 'Nossa primeira DAG', # descrição da tag,
    schedule_interval = None, # intervalo de agendamento
    start_date = datetime(2023, 3, 5), # data da execução da DAG,
    catchup = False # False não irá agendar e executar tarefas para todos os intervalos de data no histórico do DAG,
                    # desde a data de início especificada até a data de fim, mesmo que essas tarefas já devessem ter sido executadas no passado
    )

# TASKS
# do BashOperador (executa um comando na linha de comando)

task1 = BashOperator(
    task_id = 'tsk1', # id da task (tem que ser único dentro da DAG)
    bash_command = 'sleep 5', # o comando que iremos executar 
    dag = dag # recebe o nome da tag
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

# Ordem que as TASKS serão executadas
task1 >> task2 >> task3