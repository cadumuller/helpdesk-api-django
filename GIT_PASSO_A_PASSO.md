# Como subir este projeto no GitHub

Dentro da pasta do projeto:

```bash
git init
git add .
git commit -m "feat: create HelpDesk API with Django REST Framework"
git branch -M main
git remote add origin COLE_AQUI_A_URL_DO_REPOSITORIO
git push -u origin main
```

## Sugestão

Antes de subir, confirme que o arquivo `.env` NÃO aparece no Git.

Execute:

```bash
git status
```

O `.env` deve ficar ignorado pelo `.gitignore`.

O arquivo `.env.example` deve ser enviado normalmente.
