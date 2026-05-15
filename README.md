````markdown
# Alembic for Migrations

Projeto de estudo sobre gerenciamento de migrations com Alembic, SQLAlchemy e PostgreSQL.

O objetivo deste projeto é estudar:

* versionamento de schema
* autogenerate
* controle de revisões
* rollback
* organização profissional de migrations
* uso de `Base.metadata` como fonte da verdade
* sincronização entre código e banco
* troubleshooting em ambientes reais

---

# Arquitetura do projeto

```bash
.
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 2026
│           └── 05
│               ├── 03_2003_35_0893b3974670_create_account_table.py
│               ├── 03_2009_12_6fe8b1f53f88_add_a_column.py
│               └── 15_1328_15_695604cd776d_create_revision_autogenerate.py
├── alembic.ini
├── database
│   ├── base.py
│   ├── engine.py
│   └── __init__.py
├── key
│   ├── __init__.py
│   └── postgres.py
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

---

# Filosofia do projeto

Este projeto **não utiliza**:

```python
Base.metadata.create_all()
```

Toda evolução do banco é feita exclusivamente via:

```bash
alembic revision --autogenerate
alembic upgrade head
```

Benefícios:

✅ histórico completo
✅ rollback seguro
✅ rastreabilidade
✅ versionamento de schema
✅ deploy reproduzível
✅ sincronização entre ambientes
✅ auditoria técnica

---

# Diretório `database/`

Responsável pela infraestrutura de persistência.

---

## `database/base.py`

Define a classe base compartilhada por todos os modelos ORM.

Exemplo:

```python
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
```

Essa classe centraliza:

* metadata
* tabelas registradas
* constraints
* integração com Alembic

O Alembic utiliza:

```python
Base.metadata
```

como fonte da verdade.

---

## `database/engine.py`

Responsável pela criação da engine.

Exemplo:

```python
from sqlalchemy import create_engine
```

Responsabilidades:

* conexão com banco
* pooling
* controle de sessão
* isolamento transacional

---

# Diretório `alembic/`

Ambiente de migrations.

Responsável por:

* geração de revisões
* execução de upgrade
* execução de downgrade
* comparação entre banco e metadata
* versionamento incremental

---

# `alembic/env.py`

Arquivo central do ambiente de migrations.

Executado em comandos como:

```bash
alembic revision
alembic upgrade
alembic downgrade
```

---

## Fonte da verdade

No projeto:

```python
target_metadata = Base.metadata
```

Isso permite ao Alembic:

1. Ler o schema real do banco
2. Ler o metadata da aplicação
3. Comparar ambos
4. Gerar migrations automaticamente

Fluxo:

```text
Model ORM
   ↓
Base.metadata
   ↓
Alembic Autogenerate
   ↓
Migration
   ↓
Database
```

---

## Execução online

No modo online:

* cria engine
* abre conexão
* executa migrations diretamente no banco

---

## Execução offline

No modo offline:

* não abre conexão
* gera SQL puro

Útil para:

* auditoria
* revisão manual
* pipelines CI/CD

---

# `alembic/script.py.mako`

Template usado na geração das migrations.

Sempre que executamos:

```bash
alembic revision --autogenerate
```

esse template gera:

* `upgrade()`
* `downgrade()`

Exemplo:

```python
def upgrade():
    pass


def downgrade():
    pass
```

---

# `alembic/versions/`

Histórico das revisões.

Organização adotada:

```bash
versions/
└── ano/
    └── mês/
```

Exemplo:

```bash
versions/
└── 2026/
    └── 05/
```

---

## Vantagens

✅ organização cronológica
✅ fácil auditoria
✅ escalabilidade
✅ manutenção em projetos grandes
✅ rastreamento histórico

---

# Histórico atual de migrations

---

## `03_2003_35_0893b3974670_create_account_table.py`

Primeira migration.

Responsável por:

* criação da tabela `account`
* schema inicial

---

## `03_2009_12_6fe8b1f53f88_add_a_column.py`

Segunda migration.

Responsável por:

* evolução incremental do schema
* adição de coluna

---

## `15_1328_15_695604cd776d_create_revision_autogenerate.py`

Terceira migration.

Gerada com:

```bash
alembic revision --autogenerate -m "create revision autogenerate"
```

Responsável por:

* sincronização do ORM com banco
* validação do fluxo de autogenerate

---

# Diretório `key/`

Responsável pela configuração de conexão.

---

## `key/postgres.py`

Contém a URL de conexão.

Exemplo:

```python
DATABASE_URL = "postgresql://user:password@localhost/db"
```

---

# `alembic.ini`

Arquivo principal de configuração.

Responsável por:

* localização do ambiente Alembic
* logging
* comportamento global

Exemplo:

```ini
script_location = alembic
```

---

# `pyproject.toml`

Configuração do projeto Python.

Responsável por:

* dependências
* build system
* ferramentas auxiliares

---

# `uv.lock`

Arquivo gerado por `uv`.

Garante:

* builds reproduzíveis
* versões fixas
* ambientes consistentes

---

# Fluxo de trabalho

---

## 1. Alterar model

Exemplo:

```python
email = Column(String)
```

---

## 2. Garantir banco sincronizado

```bash
alembic upgrade head
```

---

## 3. Gerar migration

```bash
alembic revision --autogenerate -m "add email"
```

---

## 4. Revisar migration gerada

Sempre revisar:

* rename de tabelas
* rename de colunas
* constraints
* defaults
* indexes

---

## 5. Aplicar migration

```bash
alembic upgrade head
```

---

## 6. Reverter migration

```bash
alembic downgrade -1
```

---

# Fluxo mental profissional

```text
Alterar models
      ↓
upgrade head
      ↓
autogenerate
      ↓
revisar migration
      ↓
upgrade head
```

---

# Problemas reais encontrados durante os estudos

---

## Erro: Target database is not up to date

Mensagem:

```text
Target database is not up to date.
```

Causa:

Existe migration no código que ainda não foi aplicada no banco.

Correção:

```bash
alembic upgrade head
```

Depois:

```bash
alembic revision --autogenerate -m "nova revision"
```

---

## Warning: Collation version mismatch

Mensagem:

```text
database has a collation version mismatch
```

Causa:

Atualização do sistema operacional alterou a versão da `glibc`.

Correção:

```sql
REINDEX DATABASE postgres;
ALTER DATABASE postgres REFRESH COLLATION VERSION;
```

Esse warning não impede o Alembic de funcionar, mas deve ser tratado.

---

# Comandos úteis

---

## Revisão atual

```bash
alembic current
```

---

## Histórico completo

```bash
alembic history
```

---

## Mostrar heads

```bash
alembic heads
```

---

## Mostrar SQL sem executar

```bash
alembic upgrade head --sql
```

---

## Sincronizar banco existente

```bash
alembic stamp head
```

Usado quando o schema já existe e queremos entregar o controle ao Alembic.

---

# Observações importantes

O autogenerate do Alembic **não substitui revisão manual**.

Toda migration gerada deve ser revisada antes de aplicar em produção.

Principalmente em casos de:

* rename de tabela
* rename de coluna
* constraints complexas
* tipos especiais
* defaults de servidor
* índices compostos
* migrations destrutivas
