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


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista= define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio]= [lista]
    else:
        frota[nome_navio].append(lista)
    return frota
frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)