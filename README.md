# HelpDesk API 🎫

API REST para gerenciamento de chamados de suporte técnico, desenvolvida com **Python, Django REST Framework e PostgreSQL**.

O projeto foi criado como portfólio backend e demonstra conhecimentos em lógica de programação, APIs REST, banco de dados SQL, autenticação JWT e versionamento com Git/GitHub.

## Tecnologias

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT
- Django Filter
- Swagger / OpenAPI
- Git e GitHub
- Docker Compose

## Funcionalidades

- Login com JWT
- Renovação de token
- Consulta do usuário autenticado
- CRUD completo de chamados
- Categorias de chamados
- Prioridades
- Controle de status
- Busca por título e descrição
- Filtros por status, prioridade e categoria
- Ordenação
- Paginação
- Controle de acesso por usuário
- Área administrativa do Django
- Documentação Swagger
- Testes automatizados

## Regras de acesso

- Usuários autenticados podem criar chamados.
- Usuários comuns visualizam apenas seus próprios chamados.
- Usuários comuns só podem alterar ou excluir seus próprios chamados.
- Usuários `staff` podem visualizar e gerenciar todos os chamados.

## Estrutura do projeto

```text
helpdesk-api/
├── config/
├── tickets/
│   ├── migrations/
│   ├── admin.py
│   ├── filters.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── manage.py
├── README.md
└── requirements.txt
```

## Como executar

### 1. Clone o repositório

```bash
git clone SEU_LINK_DO_GITHUB
cd helpdesk-api
```

### 2. Crie o ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie:

```text
.env.example
```

para:

```text
.env
```

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

No Linux/macOS:

```bash
cp .env.example .env
```

## PostgreSQL

### Opção A — Docker

Com Docker instalado:

```bash
docker compose up -d
```

Isso inicia o PostgreSQL na porta `5432`.

### Opção B — PostgreSQL instalado localmente

Crie um banco e usuário com os valores definidos no `.env`.

Exemplo:

```sql
CREATE USER helpdesk_user WITH PASSWORD 'helpdesk_password';
ALTER USER helpdesk_user CREATEDB;
CREATE DATABASE helpdesk OWNER helpdesk_user;
```

## Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

## Criar usuário administrador

```bash
python manage.py createsuperuser
```

## Executar o servidor

```bash
python manage.py runserver
```

Aplicação:

```text
http://127.0.0.1:8000/
```

Swagger:

```text
http://127.0.0.1:8000/api/docs/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

## Autenticação

### Gerar token

`POST /api/auth/token/`

Body:

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Resposta:

```json
{
  "refresh": "TOKEN_REFRESH",
  "access": "TOKEN_ACCESS"
}
```

Nas demais requisições:

```text
Authorization: Bearer TOKEN_ACCESS
```

### Renovar token

`POST /api/auth/token/refresh/`

```json
{
  "refresh": "TOKEN_REFRESH"
}
```

### Usuário autenticado

`GET /api/auth/me/`

## Endpoints de chamados

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/tickets/` | Listar chamados |
| POST | `/api/tickets/` | Criar chamado |
| GET | `/api/tickets/{id}/` | Buscar chamado |
| PUT | `/api/tickets/{id}/` | Atualizar chamado |
| PATCH | `/api/tickets/{id}/` | Atualizar parcialmente |
| DELETE | `/api/tickets/{id}/` | Excluir chamado |

## Exemplo de chamado

```json
{
  "title": "Usuário sem acesso ao sistema",
  "description": "Usuário recebe erro ao realizar login.",
  "category": "ACCESS",
  "priority": "HIGH",
  "status": "OPEN"
}
```

## Filtros

```text
GET /api/tickets/?status=OPEN
GET /api/tickets/?priority=HIGH
GET /api/tickets/?category=NETWORK
```

Também é possível combinar filtros:

```text
GET /api/tickets/?status=OPEN&priority=HIGH
```

## Busca

```text
GET /api/tickets/?search=login
```

## Ordenação

```text
GET /api/tickets/?ordering=-created_at
```

## Testes

Execute:

```bash
python manage.py test
```

## Exemplo de commits

```text
feat: create Django project structure
feat: configure PostgreSQL database
feat: create ticket model
feat: implement ticket CRUD API
feat: add JWT authentication
feat: add filters and search
test: add ticket API tests
docs: add Swagger documentation
docs: update README
```

## Competências demonstradas

Este projeto demonstra conhecimento prático em:

- lógica de programação;
- Python;
- Django;
- Django REST Framework;
- SQL e PostgreSQL;
- modelagem de dados;
- APIs REST;
- autenticação JWT;
- testes de API;
- Git e GitHub.

## Autor

**Carlos Eduardo**

Projeto desenvolvido para estudos e portfólio na área de desenvolvimento backend.
