# Mini-Curso

## Estrutura do Repositório

O repositório está estruturado para representar uma arquitetura MVC (Models, Views, Controllers) modificada para se aproximar de uma arquitetura limpa com base nas experiências do Autor [Mauricio Benjamin](https://github.com/mauriciobenjamin700)

- docs: documentação de funcionalidades e regras do sistema.
- images: imagens que a aplicação venha a usar dentro das views.
- src: todos os códigos do projeto.
  - models: modelos de dados e interação com o backend.
  - views: interação do usuário com o sistema.
  - controllers: responsáveis por manipular os models e views para garantir a consistência na interação com o usuário.
- tests: testes de funcionalidades críticas do sistema, visando garantir consistência nas execuções
- videos: material de exemplo para que a ferramenta possa ser testada

## Dependencias do Projeto

O projeto foi constrido complemtante com python e suas bibliotecas, logo para executar deve-se ter o python 3.10 ou superior em sua maquina. Caso não tenha instale-o.  [Site oficial](https://www.python.org/downloads/source/)

Todas as dependencias serão gerenciadas pelo [Poetry](https://python-poetry.org/docs/) e estarão contidas no arquivo [pyproject.toml](pyproject.toml), entretanto caso queira usar o `pip` basta obter as dependências pelo [requirements.txt](requirements.txt)

Passo a Passo para realizar a instalação com poetry:

- Instale o Poetry
- Abra o terminal na pasta do projeto
- Execute o comando `poetry install`
- Ative o ambiente virtual usando `poetry shell`
- Prontinho, seu projeto está configurado e pronto para ser usado

Passo a Passo para realizar a instalação com pip

- Abra o terminal
- execute o comando `python -m venv venv` no windows ou `python3 -m venv venv` caso esteja no linux
- Ative o ambiente virtual usando `venv/Scripts/Activate` no windows ou  `source venv/bin/activate` no linux
