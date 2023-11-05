
# Projeto Credit Card FastAPI com Arquitetura Hexagonal

Este é um projeto que tem o propósito de armazenar informações de cartões em um banco de dados, permitindo que você as acesse posteriormente.
## Configuração

#### Configuração das Variáveis de Ambiente

Antes de executar o projeto, você precisará configurar as seguintes variáveis de ambiente:

- `DB_URL`: URL de conexão com o banco de dados PostgreSQL.
- `SECRET_KEY`: Chave secreta para segurança da aplicação.
- `ALGORITHM`: Algoritmo para geração de tokens de autenticação.
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tempo de expiração dos tokens de acesso.
- `DB_URL_ALEMBIC`: URL de conexão com o banco de dados PostgreSQL para Alembic.


#### Instale as Dependências

Use Poetry para instalar as dependências do projeto:

```shell
poetry install
```
Este projeto requer a instalação do pacote `python-creditcard`. No entanto, devido a problemas de compatibilidade com o Poetry devemos fazer isso pelo pip, certifique-se de que esta biblioteca esteja incluída no seu Dockerfile também.


Você pode fazer isso usando o seguinte comando:

```bash
pip install python-creditcard
```

#### Execute o Servidor de Desenvolvimento

```shell
poetry run uvicorn src.adapters.inbound.rest.main:app --host 0.0.0.0 --port 8000 --reload

````

#### Acesse a Aplicação

Abra um navegador da web e acesse http://localhost:8000/redoc. Você deve ver a documentação da API gerada automaticamente pelo FastAPI.


#### Empacotando a Aplicação em um Contêiner (Opcional)

já irá subir o postgres junto com a Aplicação

```shell 
docker-compose up -d
```


## Estrutura de Diretórios

- `src`: Este é o diretório principal da aplicação.
    - `adapters`: Contém os adaptadores da aplicação.
        - `outbound`: Aqui criamos os adaptadores de saída da aplicação.
        - `inbound`: Aqui criamos os adaptadores de entrada da aplicação.
    - `domain`:
        - `use_cases`: Contém os casos de uso da aplicação.
        - `entities`: Define as entidades de domínio da aplicação.
        - `value_objects`: Aqui definimos objetos de valor usados nas entidades.
        - `factories`: Este diretório contém as fábricas que criam objetos dentro do domínio.
        - `ports`: Define as portas (interfaces/protocols) da aplicação para separar as camadas.
            - `outbound`: Aqui criamos as portas de saída da aplicação.
            - `inbound`: Aqui criamos as portas de entrada da aplicação.
    - `tests`: Contém testes automatizados para a aplicação.

Aqui tentamos separa as camadas da aplicação, para ficar fácil as mudanças 
![hexagonal](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NfFzI7Z-E3ypn8ahESbDzw.png)

## Documentação da API

#### Retorna todos credit cards

```http
  GET /credit-cards/
```


#### Retorno em lista 

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `identification`      | `string` | O ID do item que você quer |
| `exp_date`      | `string` | data de expiração, no seguinte formato ->  mm/yyyy | 
| `holder`      | `string` | Nome que se encontra no cartão | 
| `cvv`      | `int` | Código de segurança|
| `brand`      | `string` | Bandeira do cartão|

#### Busca um credit card específico 

```http
  GET /credit-cards/{identification}
```



| Parâmetro de inserção  | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `identification` | `string` | **Obrigatório**.  Este é o ID que foi gerado na criação do credit card |

#### Retorno 

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `identification`      | `string` | O ID do item que você quer  |
| `exp_date`      | `string` | data de expiração, no seguinte formato ->  mm/yyyy | 
| `holder`      | `string` | Nome que se encontra no cartão | 
| `cvv`      | `int` | Código de segurança|
| `brand`      | `string` | Bandeira do cartão|




#### Criar um novo credit card

```http
  POST /credit-cards/{identification}
```



| Parâmetro de inserção  | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `exp_date`      | `string` | data de expiração, no seguinte formato ->  mm/yyyy | 
| `holder`      | `string` | Nome que se encontra no cartão | 
| `cvv`      | `int` | Código de segurança|

#### Retorno 

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `identification`      | `string` | O ID do item que você quer  |
| `exp_date`      | `string` | data de expiração, no seguinte formato ->  yyyy-mm-dd | 
| `holder`      | `string` | Nome que se encontra no cartão |
| `cvv`      | `int` | Código de segurança|
| `brand`      | `string` | Bandeira do cartão|

## Referência

 - [FastApi](https://fastapi.tiangolo.com/)
 - [Sqlalchemy](https://www.sqlalchemy.org/)
 - [Netflix using hexagonal architecture](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749)
 - [Livro sobre DDD em python](https://www.cosmicpython.com/)

## Contribuindo

Contribuições são sempre bem-vindas!

Sinta-se à vontade para contribuir com este projeto. Você pode enviar problemas, solicitações de recebimento (pull requests) e melhorias.

