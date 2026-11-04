# CineFlix — Projeto Integrado (DWS + POO + BD)

Catálogo de filmes com gêneros e avaliações de usuários.
Autora: Larah Garcia · Turma: 2º TIC

## Etapa 1 — Modelagem e banco de dados

- **Diagrama de Classes (UML):** `docs/diagrama_classes.png`
- **Estrutura das tabelas:** `database/schema.sql`
- **Dados iniciais:** `database/seed.sql`
- **Conexão com o banco:** `backend/database.py` (classe `Database`)
- **Classes (POO):** `backend/models/`

### Modelo

| Tabela | Descrição | Relacionamento |
|---|---|---|
| `genero` | Gêneros dos filmes | 1 gênero → N filmes |
| `filme` | Catálogo de filmes | pertence a 1 gênero |
| `usuario` | Usuários do sistema | 1 usuário → N avaliações |
| `avaliacao` | Nota e comentário de um usuário sobre um filme | liga `usuario` e `filme` (único por par) |

Mudanças em relação à AV2 (PHP): o campo texto `genero` virou a tabela `genero`
(chave estrangeira em `filme`), e foram adicionadas `usuario` e `avaliacao`.

### Como rodar o teste

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
python backend/testar_conexao.py
```

O script cria `database/cineflix.db`, carrega os dados e mostra as tabelas, as
contagens e uma consulta com JOIN.

## Estrutura

```
CineFlix/
├── backend/        config.py, database.py, models/, testar_conexao.py
├── database/       schema.sql, seed.sql
├── docs/           diagrama_classes.png / .svg / .dot
├── frontend/       HTML/CSS/JS da AV2 (será integrado na entrega final)
├── requirements.txt
└── README.md
```

## Próximas etapas
- Etapa 2 (13/11): DAOs e rotas Flask.
- Entrega final (17/11): front-end consumindo as rotas via Fetch.
