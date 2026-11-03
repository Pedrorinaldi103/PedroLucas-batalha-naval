
#ex7
frota = {}

navios =  {
    "porta-aviões" : [1,4],
    "navio-tanque": [2,3],
    "contratorpedeiro": [3,2],
    "submarino": [4,1],
}

for nome,listas in navios.items:
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