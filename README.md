# Sistema de Gestão de Tarefas - TechFlow Solutions

Este projeto consiste no desenvolvimento de uma aplicação web para gerenciamento de tarefas, proposta no contexto da disciplina de Engenharia de Software. A solução simula um ambiente real de desenvolvimento, priorizando clareza na arquitetura do código, uso de metodologias ágeis, versionamento com GitHub e aplicação de práticas de controle de qualidade.



## Escopo do Projeto

Desenvolvimento de uma aplicação web básica para gerenciamento de tarefas, com foco na implementação das funcionalidades essenciais de um sistema CRUD (Create, Read, Update e Delete) permitindo o cadastro, visualização, edição e exclusão de tarefas.

Além das funcionalidades principais, o projeto inclui a implementação de testes automatizados, com o objetivo de validar o correto funcionamento das regras básicas do sistema, estes executados de forma automatizada por meio de um pipeline de integração contínua, reforçando as práticas de controle de qualidade adotadas no desenvolvimento. O projeto prioriza a clareza, a funcionalidade e a aplicação prática dos conceitos de Engenharia de Software.



## Metodologia Utilizada

O desenvolvimento deste projeto segue os princípios das Metodologias Ágeis, priorizando a entrega contínua, adaptação às mudanças e transparência no processo de desenvolvimento. Portanto, permitindo que o projeto evolua de forma incremental, com melhorias constantes e maior controle sobre o progresso das atividades.

Como framework de apoio, foi adotado o Kanban, utilizando a ferramenta GitHub Projects para visualização e gerenciamento do fluxo deste projeto. O quadro Kanban composto pelas colunas A Fazer (To Do), Em Progresso (In Progress) e Concluído (Done), possibilita o acompanhamento em tempo real das tarefas, facilitando o gerenciamento e tomadas de decisões, permitindo então a priorização de atividades críticas e a identificação de gargalos no desenvolvimento.



## Tecnologias e ferramentas utilizadas

- Linguagem de programação Python.
- Framework Flask para criação de aplicação Web.
- Frontend HTML com Bootstrap.
- Pytest como ferramenta para testes automatizados.
- Visual Studio Code como ambiente de desenvolvimento.
- Git e GitHub como controle de versão.
- GitHub Projects para criação de Quadro Kanban
- GitHub Actions para integração contínua.



## Instruções para executar o sistema

1. Certifique-se de que possui Python instalado.

2. Clone o repositório do projeto:

```bash
git clone https://github.com/Lais-Cassiano/AplicacaoGestaoDeTarefas-UniFECAF.git
```

3. Acesse a pasta do projeto:

```bash
cd AplicacaoGestaoDeTarefas-UniFECAF
```

4. Instale as dependências necessárias:

```bash
pip install flask pytest
```

5. Execute a aplicação:

```bash
python src/main.py
```

6. Acesse no navegador:

```
http://127.0.0.1:5000/
```



## Instruções para executar os testes automatizados

Os testes garantem que as principais funcionalidades do sistema estejam operando corretamente. Para executá-los, utilizar o comando abaixo na raiz do projeto:

```bash
pytest -v
```

Foram implementados testes automatizados utilizando pytest e o cliente de testes do Flask. Os testes validam as principais operações do sistema (CRUD), garantindo que:

- As rotas respondam corretamente.
- Os formulários sejam processados adequadamente.
- As operações de criação, edição e exclusão funcionem como esperado.
- Alterações futuras no código não causem regressões.



## Arquitetura do Sistema

O sistema esta organizado de forma modular, separando responsabilidades entre a camada de aplicação, interface e testes, facilitando a manutenção, a compreensão do código e a evolução do projeto.

- **src/**  
  Diretório principal da aplicação, onde estão concentrados os arquivos de código-fonte do sistema.

- **main.py**  
  Arquivo principal da aplicação, responsável por inicializar o sistema web, definir as rotas e controlar o fluxo das operações do CRUD de tarefas, como criação, listagem, edição e exclusão.

- **templates/**  
  Contém os templates HTML utilizados na interface do sistema, responsáveis pela renderização das páginas da aplicação:
  - **base.html**: Template base que define a estrutura comum das páginas.
  - **index.html**: Página principal, onde as tarefas são listadas.
  - **criar.html**: Página responsável pelo cadastro de novas tarefas.
  - **editar.html**: Página utilizada para edição das tarefas existentes.

- **tests/**  
  Contém os testes automatizados do sistema, incluindo testes unitários e de integração, garantindo o correto funcionamento das funcionalidades principais da aplicação:
  - **test_app.py**: Arquivo responsável pelos testes das rotas e operações do CRUD de tarefas.



## Algoritmos e Estruturas de Dados Utilizadas

O sistema utiliza estruturas de dados em memória, especificamente listas e dicionários, para armazenar e manipular as tarefas durante a execução da aplicação. 

Cada tarefa é representada por um dicionário, contendo atributos como `id`, `titulo`, `descricao`, `prioridade` e `status`. O identificador (`id`) é gerado de forma incremental por meio de uma variável de controle, garantindo a unicidade das tarefas cadastradas.

As operações do CRUD são implementadas por meio de algoritmos simples de iteração e filtragem sobre a lista de tarefas, permitindo a criação, leitura, atualização e exclusão dos registros de forma eficiente para o escopo do projeto.



## Mudança de Escopo

Durante o desenvolvimento do projeto, identificou-se a necessidade de ampliar o escopo inicialmente definido, a partir da análise contínua do uso do sistema.

Como melhoria adicional, foi implementada a funcionalidade de filtro de tarefas por status, permitindo ao usuário visualizar tarefas específicas conforme seu estado (A Fazer, Em Progresso e Concluído), facilitando o acompanhamento do fluxo de trabalho e a priorização das atividades.

Essa adaptação reflete a aplicação prática da metodologia ágil, na qual o escopo não é rígido, mas ajustado de forma incremental conforme novas necessidades são identificadas ao longo do desenvolvimento. A mudança foi incorporada de maneira controlada, sem impacto nas funcionalidades já existentes, mantendo a estabilidade do sistema e a qualidade do código.

A gestão dessa alteração foi registrada no GitHub Projects, com a criação de um novo card no Kanban e a implementação da funcionalidade em um commit específico, garantindo rastreabilidade e transparência no processo de evolução do projeto.



## Considerações sobre Desempenho e Escalabilidade

Por utilizar estruturas de dados em memória, o sistema apresenta desempenho satisfatório para pequenas e médias quantidades de dados, sendo adequado ao contexto acadêmico e ao escopo proposto. As operações de listagem, edição e exclusão de tarefas são realizadas de forma direta, com baixa complexidade, proporcionando respostas rápidas ao usuário.

Em um cenário real de produção, o sistema poderia ser estendido para utilizar um banco de dados relacional ou não relacional, mantendo a mesma lógica de rotas, organização do código e estrutura de testes automatizados, permitindo maior robustez e suporte a volumes mais elevados de informações.



## Licença

- Este projeto está licenciado sob a licença MIT:

Copyright 2026 Lais

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
