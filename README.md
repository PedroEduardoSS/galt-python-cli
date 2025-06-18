# MathQuiz

## Como instalar

### Usando UV

1. Baixe o arquivo ZIP do projeto.

2. Instale o UV seguindo as instruções do [site oficial](http://docs.astral.sh/uv/getting-started/installation/#installation-methods)

3. Abra o projeto em um editor de código

4. Crie o ambiente de desenvolvimento com o comando `uv venv`

5. Sincronize o ambinete com o pyproject.toml com o comando `uv sync`

## Exemplos de uso

### Principais comandos

1. Rodar o arquivo principal padrão
    - `uv run main.py`

2. Rodar com todos os parâmetros
    - `uv run main.py --num 3 --ops =+-= --min 1.4 --max 5.8 --decimals --places 3`

3. Rodar o ruff para checar regras de lint
    - `uv run ruff check`

4. Rodar testes
    - `uv run pytest`
