# prefect-rick-and-morty-challenge

Crie um repositório publico utilizando GIT, e utilizando Python use a biblioteca Prefect (https://docs.prefect.io/latest/) para criar um projeto que consuma uma API externa (de sua preferencia) construindo tarefas (flow tasks) que consuma dados de pelo menos 2 endpoints relacionados, sumulando timeout em um deles e utilizando retry, continuar o fluxo. Armazene os dados obtidos em banco de dados com versionamento e exponha esses mesmos dados em formado CRUD utilizando RestAPI

 

O que será avaliado:

 

Padrão de codificação, utilização das melhores práticas e PEPs python.
Padrão e boas práticas de commit (não suba tudo em um commit só).
Estruturação de código.
Conhecimento de consumo de API’s
Construção de API’s
Questionamentos sobre padrões usadas e questões técnicas de python.
 

PS: Sugestões de API para serem usadas (não é obrigatório a utilização das API’s abaixo. Você pode construir uma se quiser):

https://developers.thecatapi.com/
https://rickandmortyapi.com
https://deckofcardsapi.com
https://publicapis.dev



Para executar o projeto:

1- Instale a venv:
 - python -m venv venv 
 - source venv/bin/activate  # No Windows: venv\Scripts\activate 
 - pip install -r requirements.txt

2- Entre no diretório src e execute:
 - python main.py
 - uvicorn api:app --reload (irá disponibilizar um link para as endpoints, 
adicione "\docs" no final da url no seu navegador)
 - Tema escolhido: https://rickandmortyapi.com/ 
 - API escolhida: {
  "characters": "https://rickandmortyapi.com/api/character",
  "episodes": "https://rickandmortyapi.com/api/episode"
}