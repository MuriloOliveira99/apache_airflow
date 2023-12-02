'''
- PythonOperator
    - Permite adicionar qualquer funcionalidade PYTHON ao AIRFLOW
        - Limpeza e tratamento dos dados
        - Transformações, resumos
        - Extração de fontes diversas
        - Machine Learning
    - Você pode usar qualquer módulo python

    - OBSERVAÇÃO
        - Incluir no arquivo 'docker-compose.yaml'
        - a seguinte linha de código:
        - ${AIRFLOW_PROJ_DIR:-.}/data:/opt/airflow/data
        - é o local q vai armazenar o arquivo de dados
'''

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
# import statistics as sts

with DAG(
    dag_id='python_operator',
    description='PythonOperator',
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False
) as dag:

    
    def limpa_dados():
        dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')

        dataset.columns = ['id', 'score', 'estado', 
                'genero', 'idade', 'patrimonio',
                'saldo', 'produtos', 'tem_cartao_credito',
                'ativo', 'salario', 'saiu']     
        
        dataset['salario'].fillna(dataset['salario'].median(), inplace=True)
        dataset['genero'].fillna('Masculino', inplace=True)
        dataset.loc[(dataset['idade'] < 18) | (dataset['idade'] > 120)] = dataset['idade'].median()
        dataset.drop_duplicates(subset='id', inplace=True)
        dataset.to_csv('/opt/airflow/data/Churn_clean.csv', sep=';', index=False)

    t1 = PythonOperator(task_id='t1', python_callable=limpa_dados)

    t1