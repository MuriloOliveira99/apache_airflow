# Apache Airflow 
É uma plataforma de open-source para agendar, monitorar e gerenciar fluxos de trabalho (workflows) em ambientes de processamento de dados. Para entender melhor alguns conceitos-chave:

#### DAG (Directed Acyclic Graph) 
- É um gráfico direcionado acíclico, representando um fluxo de trabalho. No contexto do Apache Airflow, uma DAG é composta por tarefas interconectadas que descrevem a ordem de execução e dependências entre elas.

##### Task (Tarefa)
- Uma tarefa em uma DAG do Apache Airflow é uma unidade de trabalho individual. Cada tarefa representa uma ação específica que deve ser executada, como executar um script, extrair dados de um banco de dados, enviar um email, etc.

##### Operators (Operadores)
- Os operadores são classes que definem como uma tarefa específica deve ser executada. O Airflow oferece vários operadores pré-construídos, como PythonOperator (para executar funções Python), BashOperator (para executar comandos Bash), e mais. Os operadores facilitam a criação de tarefas personalizadas, definindo como elas são executadas.

Em resumo, no Apache Airflow, uma DAG é uma representação visual e lógica de um fluxo de trabalho, composta por tarefas individuais que são definidas e executadas usando operadores específicos. Isso permite a automação de fluxos de trabalho complexos e o agendamento de tarefas de forma confiável.
