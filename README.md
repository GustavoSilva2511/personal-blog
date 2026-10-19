# Blog Pessoal

Blog pessoal desenvolvido com Django e Tailwind CSS como solução do desafio [Personal Blog](https://roadmap.sh/projects/personal-blog) do roadmap.sh.

A aplicação permite listar artigos, visualizar o conteúdo completo de cada post e gerenciar as publicações pelo painel administrativo do Django.

Link do desafio: https://roadmap.sh/projects/personal-blog

## Funcionalidades

- Página inicial com a lista de artigos publicados, data e prévia do conteúdo.
- Página de detalhe de cada artigo.
- Layout responsivo com Tailwind CSS.
- Gerenciamento de posts pelo Django Admin.
- Integração do Tailwind CSS via `django-tailwind` usando o binário standalone (não exige Node.js).

## Stack

- **Python 3.12+**
- **Django 6.1.2**
- **SQLite** como banco de dados padrão
- **Tailwind CSS v4** com `django-tailwind 4.6.0`
- **pytailwindcss** para o binário standalone do Tailwind
- **honcho** para rodar o Django e o Tailwind simultaneamente

## Estrutura do projeto

```text
personal-blog/
├── core/                       # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── personal_blog/              # App principal do blog
│   ├── migrations/
│   ├── templates/personal_blog/
│   │   ├── home.html
│   │   ├── post_detail.html
│   │   └── create_post.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── theme/                      # App de tema e configuração do Tailwind
│   ├── static/css/dist/        # CSS compilado
│   ├── static_src/src/styles.css
│   └── templates/base.html
├── manage.py
├── Procfile.tailwind           # Comandos usados por `tailwind dev`
└── db.sqlite3                  # Banco local (gerado ao migrar)
```

## Como rodar

### Pré-requisitos

- Python 3.12 ou superior
- Git

Não é necessário ter Node.js instalado: o `django-tailwind` usa o binário standalone do Tailwind.

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd personal-blog
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install "Django==6.1.2" "django-tailwind[honcho,reload]==4.6.0"
```

### 4. Aplique as migrações

```bash
python manage.py migrate
```

### 5. Instale o Tailwind e compile o CSS

```bash
python manage.py tailwind install
```

Esse comando baixa o binário do Tailwind e gera o CSS em `theme/static/css/dist/styles.css`.

### 6. Crie um usuário administrador

```bash
python manage.py createsuperuser
```

### 7. Inicie a aplicação

Opção A — Django e Tailwind em um único comando (Linux/macOS):

```bash
python manage.py tailwind dev
```

Opção B — dois terminais separados:

```bash
# Terminal 1: servidor Django
python manage.py runserver

# Terminal 2: watcher do Tailwind
python manage.py tailwind start
```

### Acesse

- Blog: http://127.0.0.1:8000/blog/
- Admin: http://127.0.0.1:8000/admin/

> A raiz do site (`/`) não possui rota. Acesse o blog pelo caminho `/blog/`.

## Uso

1. Acesse o admin em `/admin/` com o superusuário criado.
2. Cadastre um novo `BlogPost`.
3. Os posts aparecerão automaticamente na página inicial do blog.

## Rotas

| Rota              | Descrição                          | Nome da URL   |
| ----------------- | ---------------------------------- | ------------- |
| `/blog/`          | Lista todos os artigos             | `home`        |
| `/blog/<id>/`     | Exibe um artigo pelo ID            | `post_detail` |
| `/admin/`         | Painel administrativo do Django    | —             |

## Modelo de dados

`BlogPost` (`personal_blog/models.py`):

| Campo        | Tipo            | Descrição                            |
| ------------ | --------------- | ------------------------------------ |
| `title`      | `CharField(200)`| Título do artigo                     |
| `content`    | `TextField`     | Conteúdo completo                    |
| `created_at` | `DateTimeField` | Data de criação (automática)         |
| `updated_at` | `DateTimeField` | Data da última atualização (automática) |

## Comandos úteis

```bash
python manage.py runserver            # Inicia o servidor Django
python manage.py migrate              # Aplica migrações
python manage.py makemigrations       # Cria novas migrações
python manage.py createsuperuser      # Cria usuário admin
python manage.py test                 # Executa os testes
python manage.py tailwind start       # Watcher do Tailwind em desenvolvimento
python manage.py tailwind build       # Compila o CSS para produção
python manage.py tailwind dev         # Django + Tailwind juntos (Linux/macOS)
```

## Observações

- O projeto está configurado com `DEBUG = True` e uma `SECRET_KEY` de desenvolvimento. Para produção, mova esses valores para variáveis de ambiente e ajuste `ALLOWED_HOSTS`.
- O formulário e o template de criação de posts (`forms.py` e `create_post.html`) já existem, mas ainda não estão conectados a uma view/URL. A publicação é feita pelo Django Admin.
- O arquivo `.env` não é utilizado atualmente pela aplicação.
