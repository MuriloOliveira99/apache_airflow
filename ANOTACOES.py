'''
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

'''

