# BackEndChallengeSpaceFlight - Desafio challenge by coodesh

Este repositório refere-se ao desafio back-end Python
Consiste  em 7 tarefas, sendo 3 obrigatórias e 4 diferenciais.
Necessário adaptar o modelo de dados de acordo com o API Space Flight News.
Listadas abaixo.

Obrigatório  - C.R.U.D em articles - Concluído

Obrigatório 2 - Para alimentar o seu banco de dados você deve criar um script para armazenar os dados de todos os artigos na Space Flight News API. - Concluído

Obrigatório 3 - Além disso você precisa desenvolver um CRON para ser executado diariamente às 9h e armazenar em seu os novos artigos ao seu banco de dados. (Para essa tarefa você poderá alterar o seu modelo de dados) - Concluído

Diferencial 1 Configurar Docker no Projeto para facilitar o Deploy da equipe de DevOps; Concluído

Diferencial 2 Configurar um sistema de alerta se houver algum falha durante a sincronização dos artigos; Concluído

Diferencial 3 Descrever a documentação da API utilizando o conceito de Open API 3.0; - Concluído

Diferencial 4 Escrever Unit Tests para os endpoints da API; - Concluído

Para entender melhor o projeto, este vídeo de 5 minutos mostra alguns pontos importantes (https://www.loom.com/share/41b3c91e63764266abab99a0a195aed5)

Tecnologias utilizadas: 

Python 3.9.7, FastAPI, Postgress, SQLAlchemy

Requisitos para rodar o projeto:

Você pode usar Linux, ou dar build no DockerFile, e criar um container com a imagem agora disponível.
A string de conexão com o banco não necessita ser mudada, mas fica a seu critério, caso queira criar outro BD no Heroku;


Instruções para rodar no Linux:
1 - clone o repositório e entre na pasta /src

2 - instale as depedências com pip3 install -r requirements.txt

3 - para rodar a aplicação: uvicorn main:app --reload

Fique a vontade para testar quaiqueres endepoints. (documentação disponível em localhost:8000/docs

Instruções para usar em um container docker

0 - Instale o docker na sua máquina (https://docs.docker.com/engine/reference/commandline/start/)

0.1 - Clone o repositório

1 - Acesse a raiz do projeto

2 - Execute ->  docker build -t fastapi-challenge .

3 - Execute -> docker build -t fastapi-challenge .
4 - Execute -> docker ps                  veja agora que já existe um container criado por você mesmo!!
5 - Execute -> curl localhost:8000        a resposta deve ser "menssagem":"Back-end Challenge 2021 🏅 - Space Flight News"}


Me contate em igsantos1996@gmail.com


