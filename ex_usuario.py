import random
#função gerar matriz: parâmetros (numero de linhas, numero de colunas)
def gerarMatriz(nr_linhas,nr_colunas):
    matriz = []
    #criar um for para linhas
    for i in range(nr_linhas):
        linha = []
        for j in range(nr_colunas):
            rand = random.randint(1, 20)
            linha.append(rand)
        #Aqui o for de colunas acabou e a linha está pronta
        #alimenta a matriz
        matriz.append(linha)
    #Aqui a matriz está pronta
    return matriz


#Programa principal
linhas = int(input("Informe o numero de linhas da matriz:\n"))
colunas = int(input("Informe o numero de colunas da matriz:\n"))
matriz = gerarMatriz(linhas,colunas)

for linha in matriz:
    print(linha)
