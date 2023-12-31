docker ps

# usar o id do server
docker exec -it ID_SERVER bash

############
# dags
# lista
airflow dags list

#report
airflow dags report

#jobs
airflow dags list-jobs

#proxima execução agendada
airflow dags next-execution email_test

#executar uma dag  

# primeiro listamos runs
airflow dags list-runs -d primeira_dag

# ativar a dag
airflow dags unpause primeira_dag

# executar
airflow dags trigger primeira_dag

# lista runs novamente
airflow dags list-runs -d primeira_dag

########
# tasks
airflow tasks list email_test

# testar uma task 
airflow tasks test email_test tsk1 2023-03-15

############
# config
airflow config list

airflow pools lis

airflow connections list

airflow variables list



















