# Mini-Curso-ENUCOMPI-ERCEMAP-2024

## Estrutura do Repositório

O repositório está estruturado para representar uma arquitetura MVC (Models, Views, Controllers) modificada para se aproximar de uma arquitetura limpa com base nas experiências do Autor [Mauricio Benjamin](https://github.com/mauriciobenjamin700)

- docs: documentação de funcionalidades e regras do sistema.
- images: imagens que a aplicação venha a usar dentro das views.
- src: todos os códigos do projeto.
  - models: modelos de dados e interação com o backend.
  - views: interação do usuário com o sistema.
    - animations: animações e efeitos da aplicação.
    - colors: paleta de cores da aplicação.
    - components: classes genéricas e/ou pouco modificáveis.
    - fonts: fontes da aplicação.
    - scripts: scripts de validação de entradas e/ou saída de dados.
    - templates: itens extremamente genéricos que se repetem na grande maioria das páginas.
  - controllers: responsáveis por manipular os models e views para garantir a consistência na interação com o usuário.
    - funcs: funções genéricas que os controllers possam usar com frequência.

## Dependencias do Projeto

O projeto foi constrido complemtante com python e suas bibliotecas, logo para executar deve-se ter o python 3.10 ou superior em sua maquina. Caso não tenha instale-o.  [Site oficial](https://www.python.org/downloads/source/)

Todas as dependencias serão gerenciadas pelo [Poetry](https://python-poetry.org/docs/) e estarão contidas no arquivo [pyproject.toml](pyproject.toml)

Passo a Passo para realizar a instalação:

- Instale o Poetry
- Execute o comando `poetry install`
- Ative o ambiente virtual usando `poetry shell`
- Prontinho, seu projeto está configurado e pronto para ser usado

Caso seja desenvolvedor, acesso o manual do desenvolvedor clicando [aqui](docs/developer.md)
