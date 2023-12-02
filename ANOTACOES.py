'''
PRINCIPAIS PARÂMETROS DE UMA TAG:

1. dag_id: Um identificador único para a DAG na cluster.
2. description: Descrição da DAG.
3. schedule_interval: O intervalo de tempo no qual a DAG será executada.
4. star_date: A data e hora em que a DAG deve comecar a ser executada.
5. end_date: a datra e hora em que a DAG não deve mais ser executada
6. catchup: Determina se a DAG deve executar todas as tarefas que deveriam ter sido executadas desde a 
data de start_date até o momento atual. Padrão é TRUE
7. default_view: Visualização padrão da interface do Airflow para esta DAG. Por exemplo, 'graph'
8. max_active_runs: Máximo de execuções ativas da DAG permitidas
9. concurrency: Máximo de tarefas que podem ser executadas simultaneamente
10. tags: uma lista de tags para marcar a DAG e suas execuções
11. default_args: dicionario de argumentos padrão que serão aplicados a todas as tarefas
da DAG, a menos que sejam especificamente substituidos.
12. depends_on_past: Só inicia se no passaado executou com sucesso. Padrão é TRUE
13. email: Endereco de email para failure ou retry
14. email_on_failure: True/False
15. email_on_retry: True/False
16. retries: Número padrão de novas tentavias
17. retry_delay: timedelta(minutes=5)


PRINCIPAIS OPERADORES:

1. BashOperator: Executa um comando de shell ou script.
2. PythonOperator: Executa uma função Python.
3. DummyOperator: Não faz nada e é útil para fins de organização
4. EmailOperator: Envia um e-mail.
5. SQLOperator: Executa uma consulta SQL.
6. FileSensor: Aguarda até que um arquivo seja criado ou modificado
7. HttpSensor: Aguarda até que uma solicitação HTTP seja bem-sucedida.
8. TriggerDagRunOperator: Executa uma DAG de outra DAG


TRIGGER RULE:

1. all_sucess(default): A tarefa é executada se todas as tarefas anteriores
foram concluídas com sucesso.
2. all_failed: A tarefa é executada se todas as tarefas anteriores falharam.
3. all_done: A tarefa é executada quando todas as tarefas anteriores foram concluídas,
independentemente do status.
4. one_success: A tarefa é executada se pelo menos uma das tarefas anteriores
foi concluída com sucesso.
5. one_failed: A tarefa é executada se pelo menos uma das tarefas anteriores falhou
6. none_failed: A tarefa se nenhuma das tarefas anteriores falhou.
7. none_skipped: A tarefa é executada se nenhuma das tarefas anteriores foi pulada.
8. dummy: A tarefa é sempre executada, independentemente do status das anteriores.


XCOM: TROCA DE DADOS ENTRE TASKS

1. ti (task instance) é um objeto que representa a instância da tarefa sendo executada
2. xcom_push() é usada para DEFINIR o valor
3. xcom_pull() é usada para RECUPERAR o valor
'''

