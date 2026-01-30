# telegram-automate-job-filter

Ferramenta simples para filtrar e encaminhar mensagens de vagas e recados do Telegram com base em palavras-chave configuráveis.

## Visão geral

O projeto monitora mensagens recebidas via cliente/Bot do Telegram, aplica regras de correspondência (matching) e realiza ações configuráveis como armazenar, encaminhar ou sinalizar mensagens relevantes.

## Funcionalidades

- Filtros por palavras-chave em `config/keywords.py`
- Lógica de matching em `filters/matcher.py`
- Integração com a API do Telegram em `telegram/`
- Armazenamento mínimo em `db/`

## Requisitos

- Python 3.8 ou superior
- Dependências listadas em `requirements.txt`

## Instalação rápida

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

## Configuração

- Edite `config/settings.py` para configurar credenciais e opções gerais.
- Edite `config/keywords.py` para ajustar as palavras-chave e grupos de interesse.

Variáveis comuns (exemplo):

- `BOT_TOKEN` — token do bot/cliente Telegram
- `TARGET_CHAT_ID` — chat/usuário para encaminhar mensagens filtradas

## Execução

Execute o ponto de entrada:

```bash
python main.py
```

O processo exibirá logs no terminal. Para desenvolvimento, habilite opções de debug em `config/settings.py`.

## Estrutura do repositório

- `main.py` — ponto de entrada
- `config/` — `settings.py`, `keywords.py`
- `filters/` — `matcher.py` e regras de filtragem
- `telegram/` — cliente, listeners e integração com a API
- `db/` — armazenamento de mensagens/metadados

## Contribuição

- Abra issues para bugs ou melhorias.
- Envie pull requests com mudanças pequenas e descritas.

## Licença

Não há licença definida neste repositório — adicione um arquivo `LICENSE` com a licença desejada (por exemplo MIT) para explicitá-la.

---

Se quiser, posso:

- traduzir o README para inglês,
- adicionar um exemplo de `config/settings.py` (sem credenciais), ou
- criar um arquivo `LICENSE` (MIT/Apache). 

