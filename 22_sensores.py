'''
- Sensores
    - Aguardam um evento ou disponibilidade de um serviço
    - Não executa nenhuma ação adicional
    - Por exemplo: verifica arquivo e outra task importa

- Principais
    - 1. FileSensor: aguarda a existência ou a ausência de um arquivo em um caminho específico.
    - 2. HttpSensor: aguarda a disponibilidade de uma URL.
    - 3. S3KeySensor: aguarda a existência ou a ausência de uma chave em um bucket S3.
    - 4. SqlSensor: aguarda a execução de uma consulta SQL em um banco de dados. 

- Parametros
    - 1. poke_interval: define o intervalo de tempo entre as verificações do sensor.
    - 2. timeout: define o tempo máximo que o sensor pode esperar antes de atingir o tempo limite.
    - 3. soft_fail: especifica se o sensor deve falhar silenciosamente (retornando "False") ou gerar uma exceção quando atinge o tempo limite.
    - 4. mode: especifica o modo de operação do sensor ("reschedule" para agendar novamente a tarefa ou "poke" para continuar verificando até que a condição seja atendida).
    - 5. poke_on_failure: especifica se o sensor deve continuar verificando quando ocorre uma falha na verificação anterior.

- Nosso Exemplo
    - HttpSensor
    - Vamos verificar a disponibilidade de uma API
    - https://api.publicapis.org/entries
    - Esta api é uma lista de APIs publicas
    - Um PythonOperator vai consultar a API caso disponível
    - Precisamos cadastrar a API como uma conexão.
'''

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime
import pandas as pd
import requests

with DAG(
    dag_id='http_sensores',
    description='HTTP Sensores',
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False
) as dag:

    def query_api():
        response = requests.get("https://api.publicapis.org/entries")
        print(response.text)

    check_api = HttpSensor(
        task_id="check_api",
        http_conn_id='conexao',
        endpoint='entries',
        poke_interval=5,
        timeout=20)
    
    process_data = PythonOperator(
        task_id="process_data",
        python_callable=query_api)

    check_api >> process_data
