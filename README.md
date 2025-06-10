# Batalha Naval em Python
**Autores:** Tiago Miglioli e Felipe Krupa

Projeto desenvolvido como exercício prático para consolidar conhecimentos em **lógica de programação**, **estruturas de dados** e **boas práticas de desenvolvimento em Python**.  
O jogo é totalmente interativo no terminal e permite jogar contra outro jogador ou contra a IA.

---

## Sumário

- [Objetivos do projeto](#objetivos-do-projeto)
- [Estrutura do código](#estrutura-do-código)
  - [Definição dos navios](#definição-dos-navios)
  - [Configuração do jogo](#configuração-do-jogo)
  - [Posicionamento dos navios](#posicionamento-dos-navios)
  - [Loop de jogo](#loop-de-jogo)
  - [Visualização](#visualização)
  - [Estatísticas finais](#estatísticas-finais)
  - [Repetição do jogo](#repetição-do-jogo)
- [Boas práticas e diferenciais](#boas-práticas-e-diferenciais)
- [Conclusão](#conclusão)

---

## Objetivos do projeto

- Praticar conceitos de **funções** e **controle de fluxo**
- Trabalhar com **listas bidimensionais (matrizes)**
- Aplicar **estruturas de dados (dicionário)** para representar os navios
- Implementar **tratamento robusto de entrada de dados**
- Utilizar **modularização** para organizar o código
- Criar uma **experiência visual interativa** com a biblioteca `colorama`
- Implementar **estatísticas finais** para análise de desempenho dos jogadores

---

## Estrutura do código

### Definição dos navios

Os navios são definidos em um **dicionário**, contendo:
- Nome
- Tamanho
- Quantidade

### Configuração do jogo

- `modoJogo()` → seleção do modo de jogo
- `setarJogadores()` → definição dos nomes dos jogadores com verificação
- `configurarTabuleiro()` → criação de tabuleiros de tamanho personalizado (10x10 a 20x20)

### Posicionamento dos navios

- `configurarNavios()` → posicionamento dos navios manual ou automático (IA)
- `verificarPossibilidade()` → verifica se um navio pode ser colocado em determinada posição
- `perguntarDirecao()` e `perguntarCoordenada()` → captura e valida as entradas do jogador

### Loop de jogo

- `realizarAtaque()` → jogadores (ou IA) realizam ataques em cada rodada
- `verificarVitoria()` → verifica se um jogador venceu a partida

### Visualização

- `mostrarTabuleiro()` → exibe o tabuleiro com as seguintes cores:
    - Água: Ciano
    - Navio: Azul
    - Acerto: Verde
    - Erro: Vermelho
    - Navio Afundado: Magenta

### Estatísticas finais

- `mostrar_estatisticas_simples()` → exibe o total de tiros e acertos de cada jogador ao final do jogo

### Repetição do jogo

- `repetir()` → permite que o jogador escolha se deseja iniciar uma nova partida

---

## Boas práticas e diferenciais

- Código **modularizado**, com funções bem definidas e reutilizáveis
- **Separação de responsabilidades** clara, com o `main()` apenas organizando a execução geral
- **Tratamento robusto de entrada**, garantindo a integridade dos dados
- Uso adequado de **dicionários** e **matrizes**
- Implementação de uma interface visual simples com a biblioteca `colorama`
- Implementação de **estatísticas finais** para aprimorar a experiência do usuário
- Código limpo e legível, fácil de manter e expandir

---

## Conclusão

Este projeto demonstra:
- Domínio de **lógica de programação**
- Aplicação de boas práticas em **desenvolvimento em Python**
- Capacidade de criar um jogo interativo completo e extensível
- Atenção à **qualidade da experiência do usuário** e à organização do código

---

Se você gostou do projeto, star no repositório é muito bem-vinda.  
Fique à vontade para contribuir ou dar sugestões.
