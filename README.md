# Documentação DuckAi


## Tecnologias utilizadas

- [VueJS](https://vuejs.org/)
- [Tailwind](https://tailwindcss.com/)
- [Yarn](https://yarnpkg.com/)
- [Typescript](https://www.typescriptlang.org/)
- [Django](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [PDM](https://pdm-project.org/latest/)
- [Docker](https://www.docker.com/)
- [Swagger](https://swagger.io/)
- [Postman](https://www.postman.com/)

## Documentação da API

O serviço de IA oferece funcionalidades específicas com base nos parâmetros fornecidos na URL. Os parâmetros `ai=` e `type=` são essenciais para personalizar a saída da API.

### URL Base

http://localhost:8000/ai/

### Parâmetros
- **ai:** Define o modelo de IA a ser utilizado.
  - `1` para GPT
  - `2` para Llama
  - `3` para Hercai

Exemplo:

http://localhost:8000/ai/?ai=1 -  Está selecionando o GPT3.5.

- **type:** Especifica o tipo de operação a ser executada pelo modelo escolhido.
  - `1` para Questão e Resposta
  - `2` para Tradução
  - `3` para Resumo Nível
  - `4` para Palavras-chave
  - `5` para Resumos em Palavras

Exemplo:

http://localhost:8000/ai/?ai=1&type=2 -  Está selecionando o tipo Tradução.

## Exemplo de Uso

### GPT/LLAMA/HERCAI - Questão e Resposta

- **Descrição**: Este endpoint permite fazer perguntas abertas para a IA.
- **Método**: POST
- **URL**: `http://localhost:8000/ai/?ai={1, 2, 3}&type=1`
- **Corpo da Requisição**:

```json
{
  "user_id": 1,
  "text": "teste"
}
```

### GPT/LLAMA/HERCAI - Tradução

- **Descrição**: Este endpoint permite fazer traduções de frases.
- **Método**: POST
- **URL**: `http://localhost:8000/ai/?ai={1, 2, 3}&type=2`
- **Corpo da Requisição**:

```json
{
  "user_id": 2,
  "text": "Por que o céu é azul?",
  "from_lang": "pt-BR",
  "to_lang": "en-US"
}
```

### GPT/LLAMA/HERCAI - Resumo Nível

- **Descrição**: Este endpoint permite fazer resumos em 3 nívels('pouco', 'médio' e 'muito' resumido).
- **Método**: POST
- **URL**: `http://localhost:8000/ai/?ai={1, 2, 3}&type=3`
- **Corpo da Requisição**:

```json
{
  "user_id": 2,
  "text": "Uma versão puramente ponto-a-ponto de dinheiro eletrónico permitiria o envio de pagamentos interativos diretamente de um interveniente para outro sem passar por uma instituição financeira. Assinaturas digitais proporcionam parte da solução, mas os principais benefícios perdem-se se continuar a ser necessária uma terceira entidade de confiança para evitar gastos duplos... "
  "amount": 2
}
```

### GPT/LLAMA/HERCAI - Palavras-chave

- **Descrição**: Este endpoint permite fazer perguntas abertas para a IA.
- **Método**: POST
- **URL**: `http://localhost:8000/ai/?ai={1, 2, 3}&type=4`
- **Corpo da Requisição**:

```json
{
  "user_id": 1,
  "text": "Uma versão puramente ponto-a-ponto de dinheiro eletrónico permitiria o envio de pagamentos interativos diretamente de um interveniente para outro sem passar por uma instituição financeira. Assinaturas digitais proporcionam parte da solução, mas os principais benefícios perdem-se se continuar a ser necessária uma terceira entidade de confiança para evitar gastos duplos...",
  "keyNum": 3
}
```

### GPT/LLAMA/HERCAI - Resumos em Palavras

- **Descrição**: Este endpoint permite fazer perguntas abertas para a IA.
- **Método**: POST
- **URL**: `http://localhost:8000/ai/?ai={1, 2, 3}&type=5`
- **Corpo da Requisição**:

```json
{
  "user_id": 1,
  "text": "Uma versão puramente ponto-a-ponto de dinheiro eletrónico permitiria o envio de pagamentos interativos diretamente de um interveniente para outro sem passar por uma instituição financeira. Assinaturas digitais proporcionam parte da solução, mas os principais benefícios perdem-se se continuar a ser necessária uma terceira entidade de confiança para evitar gastos duplos...",
  "words": 5
}
```



