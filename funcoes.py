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
        for i in (tamanho - 1):
            coluna += 1
            posicao.append([linha,coluna])
    elif orientacao == "horizontal":
        for k in (tamanho - 1):
            linha += 1
            posicao.append([linha,coluna])
    return posicao
  
    