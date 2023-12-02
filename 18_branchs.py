'''
- Branchs
    - Muito comum um pipeline precisar seguir em direções diferentes
      de acordo com o resultado de eventos:
      - Caminhos para dados válçidos e inválidos
      - Diferentes testes de qualidade
      - Encaminhar diferentes e-mails conforme o resultado da análise
      - etc.
'''

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime
from random import randint

with DAG(
    dag_id='branchs',
    description='Branchs',
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False
) as dag:
    
    # funcao pra gerar um num. aleatorio
    def numero_aleatorio():
        return randint(1, 100)
    
    # task para executar a funcao 'numero_aleatorio'
    task_numero_aleatorio = PythonOperator(task_id='task_numero_aleatorio', python_callable=numero_aleatorio)

    def avalia_numero_aleatorio(**args):
        
        # obtem o resultado da task 'task_numero_aleatorio'
        # que é um PythonOperator que tá chamando a função 'numero_aleatorio' através do pyton_callable
        numero = args['task_instance'].xcom_pull(task_ids='task_numero_aleatorio')

        if numero % 2 == 0:
            return 'task_par'
        else:
            return 'task_impar'
        
    task_branch = BranchPythonOperator(
        task_id='task_branch',
        python_callable=avalia_numero_aleatorio,
        provide_context=True
    )

    task_par = BashOperator(task_id='task_par', bash_command='echo "PAR"')
    task_impar = BashOperator(task_id='task_impar', bash_command='echo "IMPAR"')

    task_numero_aleatorio >> task_branch
    task_branch >> task_par
    task_branch >> task_impar
