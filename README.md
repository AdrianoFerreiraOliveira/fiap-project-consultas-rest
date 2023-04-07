<h1>Fiap Project API Django Rest Framework</h1> 

Eu e o [Rafael Feitosa](https://github.com/Rafeso) pensamos em um aplicativo que pudesse ajudar a área da saúde onde temos ganhos exponenciais para população, identificamos que um dos grandes problemas que poderíamos atacar hoje seria a falta de informação em consultas médicas, não existe um histórico de pacientes capaz de auxiliar os profissionais da saúde para tomada de decisão e prescrição de diagnósticos consistentes com seus verdadeiros e respectivos problemas.
Essa aplicação faz parte de uma atividade da faculdade [FIAP](https://www.fiap.com.br/)

<br />
<p align="center">
  <a href="https://fiapproject.pythonanywhere.com/api-medicos/">
    <img src="https://imgur.com/FT5bA6g" alt="Logo"> 
  </a>
  <h3 align="center">ClinicalTech</h3>
</p>

## Sumário

- [Tabela de Conteúdo](#tabela-de-conte%C3%BAdo)
- [Sobre o Projeto](#sobre-o-projeto)
- [Começando](#come%C3%A7ando)
  - [Instalação](#instala%C3%A7%C3%A3o)
  - [Tecnologias utilizadas](#tecnolog)
  - [Snippets](#snippets)
- [Contribuição](#contribui%C3%A7%C3%A3o)
- [Licença](#licen%C3%A7a)
- [Contato](#contato)

<br />

## Instalação ⚙

Para executar este projeto, siga os seguintes passos:

1º Clone este repositório em sua máquina local:

<code>git clone https://github.com/AdrianoFerreiraOliveira/fiap-project-consultas-rest.git</code>

2º Instale as dependências do projeto:

<code>pip install -r requirements.txt</code>

3º Execute as migrações do banco de dados:

<code>python manage.py migrate</code>

4º Execute as migrações do banco de dados:

<code>python manage.py runserver</code>

PS. Caso queira você pode acessar a aplicação usando esse link, o mesmo usa a biblioteca isAutenticatedh do Django Rest: <br />
<br />
Login: <strong>fiap</strong> <br />
Senha: <strong>123456</strong>


<br />

## Tecnologias utilizadas 👩‍💻

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Grappelli](https://grappelliproject.com/)
- [Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
- [Deploy in Pythonanywhere](https://www.pythonanywhere.com/)


## Rotas da aplicação 🚚
- [Médicos](https://fiapproject.pythonanywhere.com/api-medicos/)
- [Rota Principal](https://fiapproject.pythonanywhere.com/)
- [Pacientes](https://fiapproject.pythonanywhere.com/api-pacientes/)
- [Swagger-Documentação](https://fiapproject.pythonanywhere.com/swagger/)
