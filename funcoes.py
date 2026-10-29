#ex1
grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
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

#ex2
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista= define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio]= [lista]
    else:
        frota[nome_navio].append(lista)
    return frota

#ex3
tabuleiro = [
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 0:
         tabuleiro[linha][coluna]='-'  
    if tabuleiro[linha][coluna] == 1:
         tabuleiro[linha][coluna]="X"
    return tabuleiro

#ex4
def posiciona_frota(frota):
    tabuleiro = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for nome in frota:
        lista=frota[nome]
        for i in range(len(lista)):
            for k in range(len(lista[i])):
                linha=lista[i][k][0]
                coluna=lista[i][k][1]
                tabuleiro[linha][coluna]=1        
    resultado=tabuleiro
    return resultado
# ex5
def afundados(frota , tabuleiro):
    lista=[]
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j]=="X":
                lista1=[i,j]
                lista.append(lista1)
    resultado=0
    for nome in frota:
        l=frota[nome]
        for i in range(len(l)):
            contador=0
            for j in range(len(l[i])):
                if l[i][j] in lista:
                    contador+=1
            if contador>=len(l[i][j]):
              resultado+=1
    return resultado


                
            
                
    
    

                
            
            
        
      