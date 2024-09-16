# Sistema Residencial Seguro com Raspberry Pi Pico

Este repositório contém o código-fonte para um sistema residencial seguro, desenvolvido como parte de um artigo científico. O objetivo deste projeto é construir um sistema de automação residencial seguro, utilizando a teoria do eletromagnetismo e sistemas embarcados, com foco em soluções simples e de baixo custo.

## Descrição do Projeto

Este projeto utiliza uma **Raspberry Pi Pico** como microcontrolador central, um **módulo RFID RC522** para autenticação via cartão, e um **módulo ponte H** para controle de um motor DC que abre e fecha um cofre.

O sistema funciona da seguinte maneira:
1. O módulo RFID lê um cartão. Se o UID do cartão for válido, o motor será ativado para abrir o cofre.
2. Após um determinado tempo (configurável no código), o motor será acionado novamente no sentido contrário para fechar o cofre.
3. O projeto utiliza componentes baratos e fáceis de encontrar, sendo ideal para aplicações residenciais e de automação simples.

## Estrutura do Código

O projeto foi modularizado em três arquivos principais:

- `main.py`: Controla o fluxo geral do programa, gerenciando as funções do RFID e do motor.
- `motor.py`: Contém as funções que controlam a abertura e fechamento do cofre através da ponte H.
- `rfid.py`: Responsável pela leitura do cartão RFID e a verificação do UID.
- `mfrc522.py`: Biblioteca responsável pela configuração do RFID.

## Requisitos

### Hardware

- **Raspberry Pi Pico**
- **Módulo RFID RC522**
- **Módulo Ponte H (ex.: L298N)**
- **Motor DC construído no artigo**
- **Cartão RFID válido**
- **Jumpers e fonte de alimentação adequada**

### Software

- **Thonny IDE**: Utilizado para programar a Raspberry Pi Pico. [Download do Thonny](https://thonny.org/)
- **Bibliotecas Python**:
  - `machine`: Para controle de GPIO.
  - `mf_rc522`: Para leitura do módulo RFID RC522. Você pode instalar usando o gerenciador de pacotes do Thonny.

## Instruções de Execução

1. **Conecte a Raspberry Pi Pico ao seu computador**.
   - Certifique-se de que a Raspberry Pi Pico esteja em modo de programação (segure o botão `BOOTSEL` ao conectar).

2. **Abra o Thonny IDE**.
   - No Thonny, configure o ambiente para usar a Raspberry Pi Pico. No menu superior, vá em:
     - `Executar` -> `Selecionar Dispositivo` -> `Raspberry Pi Pico`

3. **Carregue os arquivos no Thonny**:
   - Faça o upload dos arquivos `main.py`, `motor.py`, `rfid.py` e `mfrc522` para a Raspberry Pi Pico.
   - Para isso, abra cada arquivo no Thonny, clique em `Arquivo` -> `Salvar Como` -> `Raspberry Pi Pico`.

4. **Execute o código**:
   - No Thonny, com o arquivo `main.py` aberto, clique no botão de "play" (`Executar`).
   - O sistema começará a funcionar, aguardando a leitura de um cartão RFID válido para abrir o cofre.

5. **Verifique o comportamento**:
   - Ao aproximar um cartão RFID válido, o motor será acionado para abrir o cofre.
   - Após o tempo configurado, o motor será acionado no sentido inverso para fechar o cofre.

## Estrutura do Projeto

```plaintext
projeto_cofre/
│
├── main.py          # Arquivo principal
├── motor.py         # Controle do motor
├── rfid.py          # Controle do motor
└── mfrc522.py       # Configuração do RFID
```

## Objetivo do Artigo

Este repositório é parte de um projeto acadêmico cujo objetivo é demonstrar a criação de um sistema de segurança residencial de baixo custo, utilizando conceitos de **eletromagnetismo** e **sistemas embarcados**. A ideia central é propor uma solução acessível e fácil de replicar, utilizando a Raspberry Pi Pico e componentes comuns, como leitores RFID, além de ensinar a criar um motor dc para a utilização do mesmo no projeto.

## Contribuições

Se você deseja contribuir com este projeto ou tem dúvidas, fique à vontade para abrir uma _issue_ ou enviar um _pull request_.

## Licença

Este projeto é licenciado sob a licença MIT.