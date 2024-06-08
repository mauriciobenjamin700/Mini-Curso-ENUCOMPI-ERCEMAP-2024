# Mini-Curso-ENUCOMPI-ERCEMAP-2024

## Estrutura do Repositório

O repositório está estruturado para representar uma arquitetura MVC (Models, Views, Controllers) modificada para se aproximar de uma arquitetura limpa com base nas experiências do Autor [Mauricio Benjamin](https://github.com/mauriciobenjamin700)

- docs: documentação de funcionalidades e regras do sistema.
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
