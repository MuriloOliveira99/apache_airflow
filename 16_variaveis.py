'''
- Variáveis no AIRFLOW
    - Permitem armazenar e compartilhar informações entre DAGs
        - Credenciais de API
        - URLs
        - Chaves de Autenticação
    - Podem ser criadas na UI ou na CLI

- Variáveis vs. XCom
    - Variáveis
        - Informações estáticas e globais
        - Usadas em todo o pipeline
    - XCom
        - Informações dinâmicas
        - Entre as tarefas

- Como criar variáveis via UI no AIRFLOW?
    - No menu 'Admin', clique em 'Variables'
    - Key: Nome da variável
    - Val: Local da variavel (C:\airflow\dags)
'''

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

with DAG(
    dag_id='variavel',
    description='Variavel AIRFLOW',
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False
) as dag:
    

    # funcao pra ler a variavel do airflow
    def print_variavel(**context):
        minha_var = Variable.get('minha_var')
        print(f'O valor da variavel é {minha_var}')

    task1 = PythonOperator(task_id='tsk1', python_callable=print_variavel)

    task1

