
## SELOEDU 
Este projeto foi construido usando Python e Flask, para  a implementação inicial, seguindo o especificado nas atividades.
---

# 1 atividade-desenvolvimento-web
```
Nesta atividade, você irá implementar as rotas iniciais da aplicação SELOEDU, iniciaremos  pelo gerenciamento de usuários.

A estrutura da tabela deve seguir a definição:        users = [{"id": "id","nome": "nome","email": "email", "perfil": "perfil","status": "status"}]

GET /                           Retorna uma mensagem de boas-vindas.
GET /users                      Lista todos os usuários.
GET /id_user/{id}               Retorna usuário pelo ID ou erro se não encontrado.
POST /add_user                  Adiciona um novo usuário.
DELETE /delete_user/{id}        Remove usuário pelo ID.
PUT /update_user/{id}           Atualiza os dados de um usuário existente.
```


Recife, 09 de Setembro de 2025

---

# 2 atividade-desenvolvimento-web
```
Nesta atividade, você deverá atualizar a aplicação para criar uma nova página users.html que exiba uma tabela com informações dos usuários. O foco é apenas na renderização dos dados, sem estilização nesta etapa. Para isso, siga as orientações:

users = [{"id": id, "nome": "nome", "email": "email", "perfil": "perfil", "status": "status"}]
Obs: A tabela users deve conter pelo menos 7 registros

SELOEDU/
 ├── app.py          
 └── templates/      
      └── index.html
Criar o arquivo users.html dentro da pasta templates/.
Definir no app.py uma rota /users que envie uma lista de dicionários com os usuários.
Renderizar a tabela no users.html para a exibindo os campos: .
Manter a organização da estrutura do projeto conforme já trabalhado em sala de aula.

```

Recife, 11 de Setembro de 2025

---

# 3 atividade-desenvolvimento-web
```
A DevwebSolutions está lançando a SELOEDU, uma aplicação web voltada para o gerenciamento de treinamentos. A equipe de desenvolvimento precisa estruturar as interfaces iniciais do sistema e a navegação entre elas, criando a base para futuras funcionalidades.

O sistema deverá conter:

Página inicial (home.html)

Exibir a mensagem de boas-vindas: "Bem-vindo ao SELOEDU – Seu gerenciador de aplicação de treinamentos."
Exibir a label "Faça login para acessar o painel."

Exibir um botão com a label "Entrar"

Página inicial (login.html)

Exibir o título Login.
Ter os campos E-mail e Senha.
Disponibilizar o botão Entrar, que ao ser acionado redireciona para a página inicial (simulação de login neste momento).

Requisitos

Criar as interfaces (HTML) com as definições acima.
Garantir a interação entre as telas: o botão da página inicial deve levar para o login, e o botão de login deve retornar para a home.
Usar apenas HTML, CSS e Flask para renderizar as páginas.
Não utilizar frameworks de estilização (Bootstrap, Tailwind, etc.).

Entrega

O projeto deve ser mantido no GitHub.
A entrega no Classroom será o link do repositório GitHub contendo a estrutura abaixo.

Estrutura do projeto

SELOEDU/
├── static/
│   └── custom.css  
├── templates/
│   ├── auth/
│   │   └── login.html
│   └── home.html
└── app.py

```
Recife, 17 de Setembro de 2025

---

# 4 atividade-desenvolvimento-web
```
Autenticação de usuários na aplicação SELOEDU

Descrição
Configure o LoginManager no arquivo extensions.py e registre-o em app.py.
Ajuste o modelo de usuário em models/user.py, implementando os métodos necessários para o Flask-Login.
Crie/atualize as rotas em routes/auth.py (login, logout) e proteja as rotas de usuários em routes/user.py
Implemente a lógica correspondente nas views: views/auth.py (validar credenciais e chamar login_user/logout_user) e views/users.py (operações de usuários autenticados).
Add em templates/auth/login.html com um formulário simples de autenticação(caso já tenha manter).
Add os arquivos base,home e dashboard.html em templates
No app deve se manter:
Registro das rotas(auth_bp e users_bp)
      A criação do usuario master no contexto de execução
            with app.app_context():
                  db.create_all()
                  if not User.query.filter_by(email="admin@seloedu.com").first():
                        master = User(
                        nome="Admin Master",
                        email="admin@seloedu.com",
                        role="master"
                        )
                  master.set_password("123456")  # senha inicial
                  db.session.add(master)
                  db.session.commit()
As demais dependencia para o init do login_manager
O usuário poderá realizar no sistema SELOEDU utilizando email e senha.
O acesso a áreas protegidas (ex.: , listagem de usuários) será permitido apenas após autenticação.
A sessão do usuário permanecerá ativa durante a navegação.
Será possível com segurança através da opção de logout.
Tentativas de acessar páginas restritas sem login redirecionarão automaticamente para a tela de autenticação.
A aplicação contará com um (admin@seloedu.com / senha 123456) para uso imediato do sistema.

Entrega

O projeto deve ser mantido no GitHub.
A entrega no Classroom será o link do repositório GitHub contendo a estrutura abaixo.

Estrutura do projeto

SELOEDU/
├── models/
│   ├── extensions.py
│   └── user.py
├── routes/
│   ├── auth.py
│   └── user.py
├── Static/
│   └── custom.css  
├── templates/
│   ├── auth/
│   │   └── login.html
│   ├── base.html
│   ├── dashboard.html
│   ├── home.html
│   └── users.html
├── views/
│   ├── auth.py
│   └── user.py
└── app.py

```
Recife, 04 de Outubro de 2025

Atividades: Prof° **Jose Mauricio Matapi da Silva** 

# Como rodar o projeto

Clone este repositório:

```
git clone https://github.com/<SEU_USUARIO>/seloedu-api.git
cd seloedu-api
```

# Crie e ative um ambiente virtual:

```
python -m venv aula
# Linux/Mac
source aula/bin/activate
# Windows
aula\Scripts\activate
```

# Instale as dependências:

```
pip install -r requirements.txt
```

# Rode o servidor:

```
python app.py ou
flask run
```

---


## A API estará disponível em:
 
http://127.0.0.1:5000





Recife, Outubro de 2025

**Antônio Macena** [LinkedIn](https://www.linkedin.com/in/antonio-macena/)