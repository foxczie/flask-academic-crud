
# 🎯 **Projeto: API de Gerenciamento Escolar**

Este repositório apresenta uma **API REST** desenvolvida com **Flask**, estruturada no padrão **MVC**, oferecendo CRUD para Professores, Turmas e Alunos. A aplicação usa **SQLite** através do **SQLAlchemy**, possui documentação automática com **Swagger (Flasgger)** e pode ser executada em ambiente **Docker**.

Para criar uma turma é obrigatório existir pelo menos um professor.
Para cadastrar um aluno é necessário já haver uma turma criada.

---

# 🌸 **Integrante**

**Alessandra Shiguemori | 2404075**

---

# 🛠️ **Tecnologias utilizadas**

* **Flask**
* **Flask-SQLAlchemy**
* **Flasgger (Swagger UI)**
* **SQLite**
* **Docker**

---

# 📂 **Estrutura do Projeto (MVC)**

```txt
/projeto
│── app.py                # Arquivo principal da aplicação
│── requirements.txt      # Dependências
│── Dockerfile            # Configuração Docker
│── /model                # Modelos e banco de dados (SQLAlchemy)
│    ├── database.py
│    ├── professor.py
│    ├── turma.py
│    └── aluno.py
│── /controller            # Lógica e regras de negócio
│    ├── professor_controller.py
│    ├── turma_controller.py
│    └── aluno_controller.py
│── /routes                # Rotas da API
│    ├── professor_routes.py
│    ├── turma_routes.py
│    └── aluno_routes.py
│── /static                # Arquivos bootstrap
│── /templates             # Templates HTML
└── README.md              # Documentação
```

---

# 🚀 **Como rodar o projeto**

## **1. Clone o repositório**

```bash
git clone https://github.com/foxczie/flask-academic-crud.git
cd flask-mvc-api
```

## **2. Criar e ativar ambiente virtual (opcional, se não for usar Docker)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## **3. Instalar dependências**

```bash
pip install -r requirements.txt
```

## **4. Rodar a aplicação (sem Docker)**

```bash
flask run
```

A aplicação ficará disponível em:
**[http://localhost:5000](http://localhost:5000)**

## **5. Rodar a aplicação com Docker**

### **Build da imagem**

```bash
docker build -t flask-mvc-api .
```

### **Rodar o container**

```bash
docker run -p 5000:5000 flask-mvc-api
```

---

# 📖 **Documentação da API (Swagger)**

Após iniciar a aplicação, acesse:
👉 **[http://localhost:5000/apidocs](http://localhost:5000/apidocs)**

Lá você verá todos os endpoints organizados.

---

# 📌 **Endpoints Principais**

## **Professores (`/professores`)**

* **GET /professores** → Lista todos os professores
* **POST /professores** → Cria um professor
* **PUT /professores/{id}** → Atualiza um professor existente
* **DELETE /professores/{id}** → Remove um professor

## **Turmas (`/turmas`)**

* **GET /turmas** → Lista todas as turmas
* **POST /turmas** → Cria uma nova turma
* **PUT /turmas/{id}** → Atualiza informações da turma
* **DELETE /turmas/{id}** → Exclui uma turma

## **Alunos (`/alunos`)**

* **GET /alunos** → Lista todos os alunos
* **POST /alunos** → Cria um novo aluno
* **PUT /alunos/{id}** → Atualiza um aluno
* **DELETE /alunos/{id}** → Remove um aluno


