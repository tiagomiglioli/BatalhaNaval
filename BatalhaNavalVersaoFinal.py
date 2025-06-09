#importando os dicionários
import random
import os
import copy
import time
from colorama import init, Fore, Style
init(autoreset=True) #inicializa o cronograma

COR_PADRAO = Style.RESET_ALL
COR_AGUA = Fore.CYAN
COR_NAVIO = Fore.BLUE
COR_ACERTO = Fore.GREEN
COR_ERRO = Fore.RED
COR_AFUNDADO = Fore.MAGENTA

#Criação do dicionário, em que o a letra recebe uma tupla, a letra tem referência com o navio sendo a inicial
navios = {                              
    "E": ("Encouraçado", 5, 1), 
    "P": ("Porta-aviões", 4, 1),
    "C": ("Contratorpedeiro", 3, 2),
    "S": ("Submarino", 2, 2)
}

#limpar aqui a tela dar aquele clear ou cls dependendo se é mac ou windows/linux
def limparTela():
    try:
        os.system("clear" if os.name != "nt" else "cls")
    except:
        print("\n" * 100)

#aqui tem o modo de jogo com o tratamento de erro, a gente deixou em str pra ficar mais fácil de tratar
def modoJogo():
    modoJogo = input("Escolha 1 para jogar contra um computador:" "\n" 
                         "Escolha 2 para jogar contra um outro player:" "\n")
    while modoJogo not in ["1","2"]:
        print("Opção inválida.")
        modoJogo = input("Escolha 1 para jogar contra um computador:" "\n" 
                         "Escolha 2 para jogar contra um outro player:" "\n")

    return modoJogo

#aqui definimos os nomes dos jogadores
def setarJogadores(modoJogo: str):
    nomeJogador1 = input("Jogador 1, digite seu nome: ").strip()
    while not nomeJogador1:
        print("Nome não pode ser vazio.")
        nomeJogador1 = input("Jogador 1, digite seu nome: ").strip() ## checa se nome nao é vazio
    nomeJogador2 = ""
    if modoJogo == "2":
        nomeJogador2 = input("Jogador 2 digite seu nome: ")

    return nomeJogador1, nomeJogador2

#configuração do tabuleiro, indicando que uma função retorna uma lista
def configurarTabuleiro() -> list:
    tamanho = pegar_inteiro(input("Insira o tamanho do tabuleiro: "))
    while tamanho < 10 or tamanho > 20:
        print("Entrada inválida. Digite um número entre 10 e 20.")
        tamanho = pegar_inteiro(input("Insira o tamanho do tabuleiro (entre 10 e 20): "))
    
    tabuleiro = [["~"]*tamanho for i in range(tamanho)]

    return tabuleiro


def perguntarCoordenada(tabuleiro: list, automatico=False): #definimos automatico como falso para verificar se é IA ou não.
    posicionamento = " "
    possibilidade = False #definimos possibilidade como falso para fazer a verificar se a posição do tabuleiro é válida.

    if not automatico:
        while not possibilidade:
            posicionamento = input("Insira a letra e o número para o posicionamento do navio (Ex. A0): \nInsira a posição: ").lower().strip()
            if len(posicionamento) < 2:
                print("Coordenada inválida. Insira novamente.")
                continue ## ignora o resto do código dentro do while e repete.

            letra = posicionamento[0]
            numero = posicionamento[1:]

            if not letra.isalpha() or not numero.isdigit():
                print("Coordenada inválida. Insira novamente.")
                continue 
            
            linha = ord(letra) - ord('a')  ##tranforma a letra em numero baseado na tabela ascii
            coluna = int(numero)

            if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro):
                print("Coordenada inválida. Insira novamente.")
                continue

            possibilidade = True #se passou aqui,a coordeanada é valida
    else:
        linha = random.randint(0, len(tabuleiro) - 1)#se automatico for verdade, pula pra esse trecho do código e sorteia as coordenadas da IA
        coluna = random.randint(0, len(tabuleiro) - 1)


    return (linha, coluna)

def perguntarDirecao(jogador: str, automatico=False):#mesma lógica do automatico anterior, da verificação das coordenadas
    if not automatico:
        direcao = input("Direção (H para horizontal, V para vertical): ").upper().strip()
        while direcao not in ["H", "V"]:
            direcao = input("Direção inválida! Digite novamente(H para horizontal, V para vertical): ").upper().strip()
    else:
        direcao = random.choice(["H", "V"])

    return direcao

def verificarPossibilidade(tabuleiro: list, linha: int, coluna: int, direcao: str, tamanhoBarco: int, automatico=False):
    podeColocar = True #define uma variável booleana para fazer a verificação posterior.

    if direcao == "H":
        if coluna + tamanhoBarco > len(tabuleiro):
            podeColocar = False #caso exceda o tabuleiro, não pode colocar
        else:
            for j in range(tamanhoBarco):
                if tabuleiro[linha][coluna + j] != "~":
                    podeColocar = False
        if podeColocar:
            for j in range(tamanhoBarco):
                tabuleiro[linha][coluna + j] = "N"
        else:
            if not automatico: print("Navio não cabe na horizontal.")

        return podeColocar

    elif direcao == "V":
        if linha + tamanhoBarco > len(tabuleiro):
            podeColocar = False
        else:
            for j in range(tamanhoBarco):
                if tabuleiro[linha + j][coluna] != "~":
                    podeColocar = False
        if podeColocar:
            for j in range(tamanhoBarco):
                tabuleiro[linha + j][coluna] = "N"
        else:
            if not automatico: print("Navio não cabe na vertical.")
        
        return podeColocar

def configurarNavios(tabuleiro: list, jogador: str):
    listaBarcos = [navios[chave][0] for chave in navios for i in range(navios[chave][2])]
    ## enquanto tiver itens na lista barcos ele vai refazer 
    if jogador != "": #verifica o nome do jogador pra ver se é IA ou player
        while listaBarcos:
            print(f"Setando barcos do jogador {jogador.upper()}\n")
            print(f"Definindo a posição do barco: {listaBarcos[0]}")
            mostrarTabuleiro(tabuleiro)
            linha, coluna = perguntarCoordenada(tabuleiro)
            direcao = perguntarDirecao(jogador)
            colocado = verificarPossibilidade(tabuleiro, linha, coluna, direcao, navios[listaBarcos[0][0]][1])
            if colocado:
                limparTela()
                listaBarcos.pop(0) #a posição 0 passa a ser o barco seguinte já que o atual foi retirado: .pop(0) ESTILO FILA!!
            else:
                print("Tente novamente.")
    else:
        while listaBarcos: #se for uma IA, pular pra cá e define automatico como verdade
            linha, coluna = perguntarCoordenada(tabuleiro, automatico=True)
            direcao = perguntarDirecao(jogador, automatico=True)
            colocado = verificarPossibilidade(tabuleiro, linha, coluna, direcao, navios[listaBarcos[0][0]][1], automatico=True)
            if colocado:
                listaBarcos.pop(0) 

def mostrarTabuleiro(tabuleiro: list):
    numeros = " | ".join(f"{i:^2}" for i in range(len(tabuleiro))) #pra funcionar o join tem q ser lista inteira de string
    print(f"   {numeros}\n")

    for i, linha in enumerate(tabuleiro):#bloco percorre cada elemento e adiciona as cores 
        linha_exibida = []
        for j in range(len(tabuleiro)):
            celula = linha[j]
            caractere_exibido = celula
            cor = COR_PADRAO

            if celula == '~':
                cor = COR_AGUA
            elif celula == 'N':  
                cor = COR_NAVIO
            elif celula == 'X':  
                cor = COR_ACERTO
                caractere_exibido = 'X'
            elif celula == 'O':  
                cor = COR_ERRO
                caractere_exibido = 'O'
            elif celula == 'F': 
                cor = COR_AFUNDADO
                caractere_exibido = 'F'

            linha_exibida.append(f"{cor}{caractere_exibido:^2}{COR_PADRAO}") #fazer a coluna quando dois digitos parar formatar
        
        print(f"{chr(ord('A') + i):<2} {' | '.join(linha_exibida)}")

def verificarTiro(tabuleiro: list, linha: int, coluna: int):
    if tabuleiro[linha][coluna] in ["X", "O"]:
        return False
    else:
        return True
    
def verificarAcerto(tabuleiroAuxiliar: list,tabuleiroInimigo: list, linha: int, coluna: int):
    if tabuleiroInimigo[linha][coluna] == "N":
        tabuleiroAuxiliar[linha][coluna] = "X"
        tabuleiroInimigo[linha][coluna] = "X"
        return True
    else:
        tabuleiroAuxiliar[linha][coluna] = "O"
        tabuleiroInimigo[linha][coluna] = "O"
        return False

def realizarAtaque(tabuleiroProprio: list, tabuleiroAuxiliar: list,tabuleiroInimigo: list, jogador: str, acertos: int):
    possivel = False #variável que faz com que se o tiro for repetido, joga novamente
    if jogador != "":
        while not possivel:
            print(f"Tiro do jogador {jogador.upper()}!")
            mostrarTabuleiro(tabuleiroAuxiliar)
            print()
            mostrarTabuleiro(tabuleiroProprio)
            linha, coluna = perguntarCoordenada(tabuleiroAuxiliar)
            if not verificarTiro(tabuleiroAuxiliar, linha, coluna):
                print("Esse local já foi acertado!")
                delay()
                limparTela()
                continue #encontrar um tiro repetido, nada abaixo dele é executado naquele ciclo e o loop recomeça imediatamente

            possivel = True #local válido pro tiro
            limparTela()
            acertos+= 1 if verificarAcerto(tabuleiroAuxiliar,tabuleiroInimigo, linha, coluna) else 0
    else:
        delay()
        while not possivel:
            linha, coluna = perguntarCoordenada(tabuleiroAuxiliar, automatico=True)
            if not verificarTiro(tabuleiroAuxiliar, linha, coluna):
                continue
            possivel = True
            limparTela()
            acertos+= 1 if verificarAcerto(tabuleiroAuxiliar,tabuleiroInimigo, linha, coluna) else 0
    return acertos
        
def verificarVitoria(acertos: int):
    return acertos == 19 #numero de posições que os barcos somados ocupam
    
def delay():
    time.sleep(1)

def pegar_inteiro(numero: str):
    while not numero.isdigit():
        numero = input("Aceita somente números inteiros. Digite novamente: ")
    return int(numero)

def repetir():
    escolha = input("Deseja jogar novamente? (S/N): ").strip().upper()
    while escolha not in ("S", "N"):
        print("Opção inválida.")
        escolha = input("Deseja jogar novamente? (S/N): ").strip().upper()
    limparTela()
    return escolha == "S"

def mostrar_estatisticas_simples(tabuleiroAtaques):
    tiros_totais = 0
    acertos = 0

    for linha in tabuleiroAtaques:
        for celula in linha:
            if celula == 'X' or celula == 'O':
                tiros_totais += 1
            if celula == 'X':
                acertos += 1

    print(f"Tiros realizados: {tiros_totais}")
    print(f"Acertos:          {acertos}")

def menuInicial():
    print("Bem-vindo ao jogo: Batalha Naval!")

    modo_jogo = modoJogo()
    delay()
    limparTela()
    tabuleiro = configurarTabuleiro()
    limparTela()
    tabuleiroJogador1, tabuleiroJogador2, tabuleiroAuxiliar1, tabuleiroAuxiliar2 = copy.deepcopy(tabuleiro), copy.deepcopy(tabuleiro), copy.deepcopy(tabuleiro), copy.deepcopy(tabuleiro)#faz uma cópia dos tabuleiros

    jogador1, jogador2 = setarJogadores(modo_jogo)
    limparTela()
    acertosJogador1, acertosJogador2 = 0, 0
    configurarNavios(tabuleiroJogador1, jogador1)
    configurarNavios(tabuleiroJogador2, jogador2)

    vitoria = False #continua rodando até que o jogo termine
    vencedor = ""

    while not vitoria:
        acertosJogador1 = realizarAtaque(tabuleiroJogador1, tabuleiroAuxiliar1, tabuleiroJogador2, jogador1, acertosJogador1)
        limparTela()
        
        if verificarVitoria(acertosJogador1):
            vitoria = True
            vencedor = jogador1
            continue   
        acertosJogador2 = realizarAtaque(tabuleiroJogador2, tabuleiroAuxiliar2, tabuleiroJogador1, jogador2, acertosJogador2)
        limparTela() 
        if verificarVitoria(acertosJogador2):
            vitoria = True
            vencedor = jogador2

    if vencedor != "":
        print(f"Parabéns {vencedor.upper()} você venceu!")
    else: 
        print(f"Você perdeu, jogue novamente!")
    delay()
    limparTela()
    print("\n--- Estatísticas Finais ---")
    print("Jogador 1:")
    mostrar_estatisticas_simples(tabuleiroAuxiliar1)
    print("\nJogador 2 (ou IA):")
    mostrar_estatisticas_simples(tabuleiroAuxiliar2)

def main():
    jogar_novamente = True
    while jogar_novamente:
        menuInicial()      #chama a função que reinicia o jogo
        jogar_novamente = repetir()
    print("Até a próxima!")

if __name__ == "__main__":
    main()
