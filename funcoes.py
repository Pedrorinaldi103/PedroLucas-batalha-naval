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

frota = {
    "porta-aviões":[
      [[1,5],[1,6],[1,7],[1,8]]
    ],
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista= define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio]=lista
    return frota
