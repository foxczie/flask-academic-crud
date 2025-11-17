🎯 Projeto: API para Gestão Escolar

Este repositório apresenta uma API REST desenvolvida em Flask, organizada seguindo o padrão MVC. Ela disponibiliza operações CRUD para Professores, Turmas e Alunos, utilizando SQLite como banco de dados por meio do SQLAlchemy. Além disso, conta com documentação automática via Swagger (Flasgger) e pode ser executada em ambiente Docker.

Para registrar uma turma é necessário já existir ao menos um professor, e para cadastrar um aluno é preciso que haja uma turma previamente criada.

🌸 Integrantes

Alessandra Shiguemori | 2404075

🛠️ Ferramentas utilizadas

Flask

Flask-SQLAlchemy

Flasgger / Swagger UI

SQLite

Docker

📂 Estrutura do Projeto (Padrão MVC)
/projeto
│── app.py                # Arquivo principal da aplicação
│── requirements.txt      # Lista de dependências
│── Dockerfile            # Configuração para gerar o container
│── /model                # Modelos e conexão (SQLAlchemy)
│    ├── database.py
│    ├── professor.py
│    ├── turma.py
│    └── aluno.py
│── /controller           # Lógica de negócio
│    ├── professor_controller.py
│    ├── turma_controller.py
│    └── aluno_controller.py
│── /routes               # Arquivos de rotas da API
│    ├── professor_routes.py
│    ├── turma_routes.py
│    └── aluno_routes.py
│── /static               # Arquivos bootstrap
│── /templates            # HTMLs utilizados
└── README.md             # Documento de referência

🚀 Passo a passo para executar o projeto
1. Clonar o repositório
git clone https://github.com/samea-jesus0/flask-academic-crud.git
cd flask-mvc-api

2. Criar e ativar o ambiente virtual (se optar por não usar Docker)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instalar as dependências
pip install -r requirements.txt

4. Executar a aplicação localmente (sem Docker)
flask run


A API ficará acessível em:
http://localhost:5000

5. Subir a aplicação via Docker 🐳
# Criar a imagem
docker build -t flask-mvc-api .

# Iniciar o container
docker run -p 5000:5000 flask-mvc-api

📖 Acesso à Documentação (Swagger)

Depois de iniciar a API, abra:
👉 http://localhost:5000/apidocs

Ali estarão listados todos os endpoints e suas descrições.

📌 Endpoints Principais
Professores (/professores)

GET /professores → Consulta todos os professores

POST /professores → Adiciona um novo professor

PUT /professores/{id} → Edita um professor existente

DELETE /professores/{id} → Exclui um professor

Turmas (/turmas)

GET /turmas → Retorna a lista de turmas

POST /turmas → Registra uma turma

PUT /turmas/{id} → Atualiza os dados de uma turma

DELETE /turmas/{id} → Remove uma turma

Alunos (/alunos)

GET /alunos → Lista todos os alunos cadastrados

POST /alunos → Cadastra um aluno novo

PUT /alunos/{id} → Altera os dados de um aluno

DELETE /alunos/{id} → Exclui um aluno