from funcoes import *

#ex7
frota = {}

navios =  {
    "porta-aviões" : [1,4],
    "navio-tanque": [2,3],
    "contratorpedeiro": [3,2],
    "submarino": [4,1],
}

for nome,listas in navios.items():
    qtd = listas[0]
    tamanho = listas[1]

    for i in range(qtd):
        verifica = False
        while verifica == False:
            
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            
            if nome != "submarino":
                orientacao = int(input("[1] Vertical [2] Horizontal >")) 
                if orientacao == 1:
                    orientacao = "vertical"
                elif orientacao == 2:
                    orientacao = "horizontal"
            else:
                orientacao = "horizontal"

            verifica = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if verifica == False:
                print("Esta posição não está válida!")

        posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)
        if nome not in frota:
            frota[nome] = []
        frota[nome].append(posicao_navio)
# print(frota)
#ex8
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_do_oponente = posiciona_frota(frota_oponente)
tabuleiro_do_jogador = posiciona_frota(frota)
imprime = True
jogando=True    
while jogando==True:
    if imprime == True:
        print(monta_tabuleiros(tabuleiro_do_jogador, tabuleiro_do_oponente))
    linha_ataque=int(input("Jogador, qual linha deseja atacar? "))
    while linha_ataque>9 or linha_ataque<0:
        print("Linha inválida!")
        linha_ataque=int(input("Jogador, qual linha deseja atacar? "))
    coluna_ataque=int(input("Jogador, qual coluna deseja atacar? "))
    while coluna_ataque>9 or coluna_ataque<0:
        print('Coluna inválida!')
        coluna_ataque=int(input("Jogador, qual coluna deseja atacar? "))
    
    if tabuleiro_do_oponente[linha_ataque][coluna_ataque]=="X" or tabuleiro_do_oponente[linha_ataque][coluna_ataque]=="-":
        print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
        imprime = False
    else:
        faz_jogada(tabuleiro_do_oponente,linha_ataque,coluna_ataque)
        imprime = True
    if afundados(frota_oponente , tabuleiro_do_oponente)==10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando=False


    





