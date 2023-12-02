'''
- Pools
    - Os pools são usados para gerenciar a concorrência e a alocação de recursos.
    - Exemplos:
        - Varias tarefas que precisam acessar um banco de dados.
        - Limites de conexões e recursos.
        - Você cria um pool que vai limitar e gerenciar o uso destas conexões.
    - slot
        - worker disponivel para o recurso
        - dessa forma, o pool vai gerenciar o uso do worker
    - Criar pools
        - Na aba 'Admin', clique em 'Pools'
'''

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='pool_operator',
    description='Pool Operator',
    schedule_interval=None,
    start_date=datetime(2023, 3, 5)
) as dag:
    
    # priority_weight: executará 1º a task4 e depois a task2
    # as taks 1 e 3, o airflow que decidirá a ordem de exec.

    task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', pool='meu_pool')
    task2 = BashOperator(task_id='tsk2', bash_command='sleep 5', pool='meu_pool', priority_weight=5)
    task3 = BashOperator(task_id='tsk3', bash_command='sleep 5', pool='meu_pool')
    task4 = BashOperator(task_id='tsk4', bash_command='sleep 5', pool='meu_pool', priority_weight=10)
