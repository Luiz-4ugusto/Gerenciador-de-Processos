
# sistema gerenciamento de eventos pessoais

Este sistema foi desenvolvido com o propósito de oferecer aos usuários uma forma simples e eficiente de criar e receber notificações sobre os seus próprios eventos utilizando interfaces gráficas e integração com bibliotecas do pyhton, além do uso de modelagem de software para garantir uma estrutura sólida, facilitando a manutenção, escalabilidade e eficiência no desenvolvimento da aplicação





## Descrição do projeto

Este projeto tem como objetivo o desenvolvimento de um sistema de gerenciamento de processos e lembretes, permitindo ao usuário organizar e acompanhar tarefas de forma prática e eficiente. O sistema oferece funcionalidades como cadastro, visualização e controle de lembretes, além do envio de notificações automáticas para alertar o usuário no momento programado.

A aplicação foi desenvolvida utilizando a linguagem Python com Tkinter para a interface gráfica, proporcionando uma interação simples e intuitiva. O sistema também utiliza bibliotecas auxiliares para gerenciamento de tempo e notificações, garantindo que os lembretes sejam exibidos corretamente durante a execução do programa. A estrutura do projeto foi organizada de forma modular, facilitando a manutenção, atualização e expansão de novas funcionalidades.



## Documentação

- [Documentação do projeto](https://drive.google.com/file/d/1wZsGwSC3Ql6lmkhgZZNQ5by36ZcKsKV3/view?usp=sharing)

## Requisitos Funcionais (RNG)

RN01. Um evento deve possuir obrigatoriamente um Título e uma descrição.

RN02. O usuário deve definir um tempo para a notificação do evento.

RN03. Um evento pode ser editado ou excluído pelo usuário.

RN04 O sistema deve permitir que um evento seja notificado mais de uma vez, caso o usuário configure repetições.

RN05. Os eventos cadastrados devem ser armazenados na lista de eventos do usuário.



## Requisitos Funcionais (RF)
RF01. O sistema deve permitir ao usuário cadastrar um novo evento.

RF02. O sistema deve exibir uma lista com todos os eventos cadastrados que ainda estão ativos.

RF03. O sistema deve permitir que o usuário altere as informações de um evento existente.

RF04. O sistema deve permitir que o usuário edite e exclua produtos previamente cadastrados.

RF05. O sistema deve enviar uma notificação ao usuário quando chegar o horário definido.

## Requisitos Não Funcionais (RNF)

RNF01. O sistema deve possuir uma interface simples e intuitiva para facilitar o uso pelo usuário.

RNF02. O sistema deve enviar a notificação do evento no tempo definido pelo usuário.

RNF03. O sistema deve funcionar em computadores com sistema operacional Windows.

RNF04. O sistema não deve perder eventos cadastrados durante a execução.

RNF05. O sistema deve poder ser executado como aplicação Python ou arquivo executável (.exe).

## Tecnologias utilizadas
- Python
- Tkinter
- Plyer
- PyInstaller
  
## Ferramentas

| Ferramentas | Finalidade |
|-------------|------------|
| Python 3 | Linguagem de programação utilizada no desenvolvimento da aplicação |
| Tkinter | Biblioteca utilizada para a criação da interface gráfica |
| Plyer | Biblioteca utilizada para o envio de notificações no sistema |
| PyInstaller | Ferramenta utilizada para gerar o arquivo executável (.exe) |



## ▶️ Como executar 

1. No vscode instale as dependências:

pip install plyer

2. Execute o programa:

python Gerenciador_main.py


## Download do projeto

Baixe a última versão: https://github.com/Luiz-4ugusto/Gerenciador-de-Processos/releases/tag/v1.0 
  

## Licença

Este projeto está sob a licença MIT.



