def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = [[linha,coluna]]
    if orientacao == "vertical":
        for i in range(tamanho - 1):
            linha += 1
            posicao.append([linha,coluna])
    elif orientacao == "horizontal":
        for k in range(tamanho - 1):
            coluna += 1
            posicao.append([linha,coluna])
    return posicao

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posiçao=define_posicoes(linha, coluna, orientacao, tamanho)
    for a in range(len(posiçao)):
        if posiçao[a][0]>9 or posiçao[a][1]>9 or posiçao[a][0]<0 or posiçao[a][1]<0:
            return False

    for nome in frota:
        l=frota[nome]
        for i in range(len(l)):
                for j in range(len(l[i])):
                    for a in range(len(posiçao)):
                        if l[i][j]==posiçao[a]:
                            return False
    return True

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
print(frota)1