#
## ----- GUSTAVO ROMÃO CUNHA
#
#
import random
import time
##############
##BACK - END##
##############
#GERANDO TODAS AS PEÇAS DO DOMINO
pecas = []
for numero1 in range(7):
    for numero2 in range(numero1, 7):
        pecas.append([numero1, numero2])
#DISTRUBIR AS PEÇAS ENTRE JOGADORES E DEFINIR PEÇAS DE COMPRA
def distribuir_pecas(pecas, num_jogadores):
    random.shuffle(pecas)
    #JOGADORES RECEBENDO 7 CARTAS CADA, IDENEPDENTE DO MODO
    num_pecas_por_jogador = 7
    jogadores = [pecas[i*num_pecas_por_jogador : (i+1)*num_pecas_por_jogador] for i in range(num_jogadores)]
    #PEÇAS RESTANTES NA MESA PARA COMPRAS
    pecas_disponiveis = pecas[num_jogadores*num_pecas_por_jogador:] 
    return jogadores, pecas_disponiveis
#FUNÇÃO PARA VERIFICAR SE A PEÇA PODE SER JOGADA EM ALGUM CANTO
def pode_jogar(peca, mesa):
    extremidades = [mesa[0][0], mesa[-1][1]]#EXTREMIDADES DA MESA
    numeros_peca = [peca[0], peca[1]]#NUMEROS QUE A PEÇA CONTEM
    if numeros_peca[0] in extremidades or numeros_peca[1] in extremidades:
        return True
    #VERIFICAR SE A 1 PARTE DA PEÇA É COMPATIVEL
    if numeros_peca[0] == extremidades[0] or numeros_peca[0] == extremidades[1]:
        return True
    #VERIFICAR SE A 2 PARTE DA PEÇA É COMPATIVEL
    if numeros_peca[1] == extremidades[0] or numeros_peca[1] == extremidades[1]:
        return True
    return False
#REMOVER A PEÇA DO DECK DO JOGADOR APÓS JOGAR
def remover_peca(deck, peca):
    if peca in deck:
        deck.remove(peca)
###############
##FRONT - END##
###############
print("----------------------------------------------")
print("                  D O M I N Óa                 ")
print("----------------------------------------------")
num_jogadores = int(input("Informe o número de jogadores (entre 2 e 4): "))
if num_jogadores < 2 or num_jogadores > 4:
    print("Número inválido, escolha de 2 a 4 jogadores!")
else:
    jogadores, pecas_disponiveis = distribuir_pecas(pecas, num_jogadores)
    if num_jogadores == 4:
        #SORTEAR PEÇA DO JOGADOR 1, NA OPÇÃO 4 JOGADORES
        mesa = jogadores[0][-1]
        jogadores[0] = jogadores[0][:-1]
        #COMEÇAR DO 2 JOGADOR QUANDO FOR 4 PLAYERS
        jogador_atual = 1
    else:
        #SELECIONAR PEÇA DA MESA PRINCIPAL DAS PEÇAS DISPONIVEIS (QUANDO É APENAS 2 OU 3 JOGADORES)
        mesa = random.choice(pecas_disponiveis)
        pecas_disponiveis.remove(mesa)
        jogador_atual = 0
    mesa_principal = [mesa]
    #MOSTRAR AS PEÇAS DISPONIVEIS PARA COMPRA
    print("Peças disponíveis para compra:", pecas_disponiveis)
    #MOSTRAR AS PEÇAS DE CADA JOGADOR
    for i, jogador in enumerate(jogadores):
        print(f"Jogador {i+1}: {jogador}")
    print("\n[!] - PEÇA DA MESA:", mesa)
####################
##INICIANDO RODADA##
####################
rodada = 1
while True:
    print(f"\n[!] - Rodada {rodada} - Vez do Jogador {jogador_atual + 1} - [!]")
    print("Suas peças:", jogadores[jogador_atual])
    print("Mesa:", mesa_principal)
    #VERIFICANDO SE O JOGADOR QUER COMPRAR UMA PEÇA
    comprar_peca = input("Pressione Enter para jogar ou digite qualquer coisa para comprar uma peça: ")
    if comprar_peca:
        #COMPRA DE PEÇA ADICIONAL
        if pecas_disponiveis:
            nova_peca = pecas_disponiveis.pop()
            jogadores[jogador_atual].append(nova_peca)
            print(f"Você comprou a peça {nova_peca}")
        else:
            print("Não há mais peças disponíveis para compra.")
    else:
        #PEDINDO AO JOGADOR PARA ESOCLHER UMA PEÇA
        while True:
            try:
                escolha = int(input("Escolha uma peça para jogar (digite o número): ")) - 1
                if 0 <= escolha < len(jogadores[jogador_atual]):
                    peça_escolhida = jogadores[jogador_atual][escolha]
                    if pode_jogar(peça_escolhida, mesa_principal):
                        remover_peca(jogadores[jogador_atual], peça_escolhida)
                        print("Você jogou a peça:", peça_escolhida)
                        if peça_escolhida[0] == mesa_principal[0][0]:
                            mesa_principal.insert(0, peça_escolhida)
                        else:
                            mesa_principal.append(peça_escolhida)
                    else:
                        print("Essa peça não pode ser jogada.")
                    break
                else:
                    print("Número de peça inválido. Escolha uma peça válida.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    #VERIFICAR SE O JOGADOR FICOU SEM PEÇAS E GANHOU A PARTIDA
    if len(jogadores[jogador_atual]) == 0:
        print(f"Jogador {jogador_atual + 1} foi o VENCEDOR !!!")
        break
    jogador_atual = (jogador_atual + 1) % num_jogadores
    rodada += 1
    #PAUSAR 2segundinhos ENTRE RODADAS
    time.sleep(2)