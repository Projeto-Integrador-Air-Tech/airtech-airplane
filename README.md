# Airtech-Airplane API

Bem-vindo ao projeto Airtech-Airplane API! Esta API foi desenvolvida em Python usando o framework Flask para fornecer operações CRUD para a gestão de aeronaves e modelos.

## Configuração do Ambiente

Antes de começar, certifique-se de ter o Python instalado em seu sistema. Além disso, utilize o arquivo `Pipfile` e `Pipfile.lock` para instalar as dependências do projeto. Se não tiver o Pipenv instalado, você pode instalá-lo usando:

```bash
pip install pipenv
```

Em seguida, instale as dependências:

```bash
pipenv install
```

## Configuração do Banco de Dados

O projeto utiliza um banco de dados PostgreSQL para armazenar os dados. Certifique-se de ter um servidor PostgreSQL em execução e ajuste as configurações no arquivo `.env` para refletir as informações do seu banco de dados.

```env
POSTGRESQL_HOST=seu-host
POSTGRESQL_PORT=sua-porta
POSTGRESQL_USER=seu-usuario
POSTGRESQL_PW=sua-senha
POSTGRESQL_DB=seu-banco-de-dados
```

## Executando a Aplicação

Com as dependências instaladas e o banco de dados configurado, você pode executar a aplicação com o seguinte comando:

```bash
pipenv run python app.py
```

A API estará disponível em `http://localhost:8040`.

## Rotas Disponíveis

- **GET /aircrafts**: Retorna a lista de aeronaves.
- **GET /aircrafts/{aircraft_id}**: Retorna detalhes de uma aeronave específica.
- **POST /aircrafts**: Cria uma nova aeronave.
- **PUT /aircrafts/{aircraft_id}**: Atualiza os detalhes de uma aeronave existente.
- **DELETE /aircrafts/{aircraft_id}**: Exclui uma aeronave.

- **GET /models**: Retorna a lista de modelos de aeronaves.
- **GET /models/{model_id}**: Retorna detalhes de um modelo de aeronave específico.
- **POST /models**: Cria um novo modelo de aeronave.
- **PUT /models/{model_id}**: Atualiza os detalhes de um modelo de aeronave existente.
- **DELETE /models/{model_id}**: Exclui um modelo de aeronave.

Certifique-se de consultar a documentação da API para obter detalhes adicionais sobre os parâmetros de cada rota.

## Contribuindo

Sinta-se à vontade para contribuir para este projeto. Abra uma issue para relatar problemas ou envie um pull request com melhorias.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
