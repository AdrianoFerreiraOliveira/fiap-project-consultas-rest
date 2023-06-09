<h1 align="center">Fiap Project API Django Rest Framework</h1> 



<br />

<p align="center">
 <img alt="Made by Adriano" src="https://user-images.githubusercontent.com/105682437/230727723-dbc30407-696e-4a90-b58b-e0d6e030c578.png" width="40%">
</p>

<h4 align="center"> 
	✔  Clinical Tech 🚀 Concluído  ✔
</h4>

<div style="display: flex; gap: 0.5rem;"> 
  <a href="https://fiapproject.pythonanywhere.com/api-medicos/">
    <img alt="Made by Rafeso and Adriano" src="https://img.shields.io/badge/Acessar%20%20-Web-%2304D361">
  </a>
</div>

## Sumário 📝


- [Sobre o Projeto](#sobre-o-projeto)
- <a href="#-como-executar-o-projeto">Como executar</a> • 
- <a href="#acesso">Acesso a Aplicação</a> •
- <a href="#funcionalidades">Funcionalidades</a> •
- <a href="#-tecnologias">Tecnologias</a> • 
- [Rotas](#rotas) •
- <a href="#telas">Telas</a> •
- <a href="#-autor">Autor</a> • 

<br />

## Sobre o Projeto

Eu e o [Rafael Feitosa](https://github.com/Rafeso) pensamos em um aplicativo que pudesse ajudar a área da saúde onde temos ganhos exponenciais para população, identificamos que um dos grandes problemas que poderíamos atacar hoje seria a falta de informação em consultas médicas, não existe um histórico de pacientes capaz de auxiliar os profissionais da saúde para tomada de decisão e prescrição de diagnósticos consistentes com seus verdadeiros e respectivos problemas.
Essa aplicação faz parte de uma atividade da faculdade [FIAP](https://www.fiap.com.br/)

## Como executar o projeto ⚙

Para executar este projeto, siga os seguintes passos:

1º Clone este repositório em sua máquina local:

<code>git clone https://github.com/AdrianoFerreiraOliveira/fiap-project-consultas-rest.git</code>

2º É altamente recomendado que você utilize um ambiente virtual para rodar o projeto, caso queria saber um pouco mais sobre
basta clicar [aqui](https://docs.python.org/pt-br/3/library/venv.html)

3º Criando o ambiente virtual
- 3.1 Após abrir a pasta onde esta seu arquivo acesse o terminal, no nosso caso usamos o  visual studio code e siga os passos abaixo
- 3.2 <code>pip install virtualvenv</code>
- 3.3 <code>virtualenv venv</code>
- 3.4 <code>venv/Scripts/Activate</code> <strong>(Atenção a ésse código pois ele pode variar de acordo com o seu sistema operacional)</strong>.

![2023-04-08 18-02-40](https://user-images.githubusercontent.com/105682437/230742811-bc82dc75-f0f6-49f3-a0b0-a1a877a9dfbb.gif)


4º Instale as dependências do projeto:

<code>pip install -r requirements.txt</code>

5º Execute as migrações do banco de dados:

<code>python manage.py migrate</code>

6º Execute as migrações do banco de dados:

<code>python manage.py runserver</code>

## Acesso a Aplicação 🔐

PS. Caso queira você pode acessar a aplicação usando esse link, o mesmo usa a biblioteca isAutenticatedh do Django Rest: <br />
<br />
Login: <strong>fiap</strong> <br />
Senha: <strong>123456</strong>

<br />

## Funcionalidades
- [x] Cadastrar um novo médico
- [x] Cadastrar uma Nova Consulta
- [x] Gerenciar dados
- [x] Incluir foto do Médico
<br />

## Tecnologias <img align="center" alt="Adriano-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Grappelli](https://grappelliproject.com/)
- [Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
- [Deploy in Pythonanywhere](https://www.pythonanywhere.com/)
<br />

## Rotas 🚚
- [Médicos](https://fiapproject.pythonanywhere.com/api-medicos/)
- [Rota Principal](https://fiapproject.pythonanywhere.com/)
- [Pacientes](https://fiapproject.pythonanywhere.com/api-pacientes/)
- [Swagger-Documentação-API](https://fiapproject.pythonanywhere.com/swagger/)
- [Grappeli Admin](https://fiapproject.pythonanywhere.com/controle/)

## Telas

<div>
Home
  <img width="1090" alt="Home" src="https://user-images.githubusercontent.com/105682437/230730177-8014d421-5e5d-4a26-b8eb-d3d335f42be5.PNG">  
</div>

Pacientes
<div>
  <img width="593" alt="Pacientes" src="https://user-images.githubusercontent.com/105682437/230730221-2dbb07bb-e787-458c-9379-52d07e354d14.PNG">
</div>

Swagger
<div>
  <img width="748" alt="Swagger" src="https://user-images.githubusercontent.com/105682437/230730233-36e48cc1-05b3-4018-b579-286f16ece317.PNG">
</div>  

Admin
<div>
  <img width="637" alt="Admin" src="https://user-images.githubusercontent.com/105682437/230730254-2753ef53-14ae-40db-aa77-857baafa19e8.PNG">
</div>

## Demo 🎮
![2023-04-08 12-00-16 (1)](https://user-images.githubusercontent.com/105682437/230729906-742f65e7-c11b-4de5-b8b6-32f4e778dfba.gif)

---
## 🦸 Autor

<div>
<a href="https://github.com/Rafeso">
 <img 
 <br />
 <sub><b>Rafael Feitosa</b></sub></a> <a href="#">☕</a>
 <br />
 
 [![Linkedin Badge](https://img.shields.io/badge/-Rafael-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rafael-feitosa-618472241/)](https://www.linkedin.com/in/rafael-feitosa-618472241/) 
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat-squarew&logo=github&logoColor=white%link=https://github.com/Rafeso)](https://github.com/Rafeso)
</div>

<div>
<a href="https://github.com/AdrianoFerreiraOliveira">
 <img 
 <br />
 <sub><b>Adriano Oliveira</b></sub></a> <a href="#">😁</a>
 <br />
 
 [![Linkedin Badge](https://img.shields.io/badge/-Adriano-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://https://www.linkedin.com/in/adriano-ferreira-oliveira)](https://www.linkedin.com/in/adriano-ferreira-oliveira/) 
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat-squarew&logo=github&logoColor=white%link=https://github.com/Adriano)](https://github.com/AdrianoFerreiraOliveira)
</div>

## Explicação do Projeto:
[Youtube](https://youtu.be/YEyAGzOR8ps)





