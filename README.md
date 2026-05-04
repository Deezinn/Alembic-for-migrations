# Alembic for Migrations

Projeto de estudo sobre gerenciamento de migrações de banco de dados utilizando :contentReference[oaicite:0]{index=0} com :contentReference[oaicite:1]{index=1} e :contentReference[oaicite:2]{index=2}.

---

# Estrutura do projeto

```bash
.
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       └── 2026/
│           └── 05/
│               ├── 03_2003_35_0893b3974670_create_account_table.py
│               └── 03_2009_12_6fe8b1f53f88_add_a_column.py
│
├── alembic.ini
├── key/
│   ├── __init__.py
│   └── postgres.py
│
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

---

# Arquivos e diretórios

## `alembic/`

Diretório principal do ambiente de migração.

Responsável por armazenar:

- configuração de execução
- templates
- histórico de revisões
- scripts de migração

---

## `alembic/env.py`

Arquivo central do Alembic.

Executado sempre que algum comando de migração é chamado.

### Responsabilidades

- criar conexão com banco
- configurar engine do SQLAlchemy
- carregar metadados dos modelos
- executar migrations online ou offline

### Pode ser customizado para

- múltiplos bancos
- schemas separados
- logging customizado
- importação dinâmica de models

---

## `alembic/script.py.mako`

Template usado na geração automática de migrations.

Toda vez que executamos:

```bash
alembic revision --autogenerate
```

esse template é usado para gerar:

- `upgrade()`
- `downgrade()`

Exemplo gerado:

```python
def upgrade():
    pass


def downgrade():
    pass
```

---

## `alembic/versions/`

Histórico das migrations.

No seu projeto, as migrations estão organizadas por:

- ano
- mês
- timestamp

Estrutura:

```bash
versions/
└── 2026/
    └── 05/
```

### Vantagens dessa organização

✔ melhor rastreabilidade
✔ organização cronológica
✔ facilita projetos grandes
✔ evita centenas de arquivos no mesmo diretório

---

## Exemplo de migration

### `03_2003_35_0893b3974670_create_account_table.py`

Migration responsável pela criação da tabela de contas.

### `03_2009_12_6fe8b1f53f88_add_a_column.py`

Migration responsável por adicionar nova coluna.

---

## `alembic.ini`

Arquivo principal de configuração do Alembic.

Contém:

- localização dos scripts
- logging
- conexão com banco
- configurações globais

Exemplo:

```ini
script_location = alembic
```

---

## `pyproject.toml`

Arquivo de configuração do projeto Python.

Usado para:

- dependências
- build system
- configuração do projeto
- integração com ferramentas modernas

---

## `uv.lock`

Arquivo de lock gerado pelo :contentReference[oaicite:3]{index=3}.

Garante:

- reprodutibilidade
- versões fixas
- builds consistentes

---

## `key/`

Pacote responsável pela configuração de conexão com banco.

---

## `key/__init__.py`

Transforma o diretório em um pacote Python.

---

## `key/postgres.py`

Módulo com configurações do :contentReference[oaicite:4]{index=4}.

Pode conter:

- URL de conexão
- engine
- credenciais
- helpers de conexão

Exemplo:

```python
DATABASE_URL = "postgresql://user:password@localhost/db"
```

---

## `LICENSE`

Licença do projeto.

Define:

- permissões de uso
- distribuição
- modificação

---

# Comandos úteis

## Criar migration

```bash
alembic revision --autogenerate -m "create account table"
```

---

## Aplicar migrations

```bash
alembic upgrade head
```

---

## Reverter migration

```bash
alembic downgrade -1
```

---

## Ver histórico

```bash
alembic history
```

---

## Ver revisão atual

```bash
alembic current
```

---

