import random
#PRECISO DE 2 FORS, PARA PODER GERAR 1 LINHA DE NUMEROS E OUTRO PARA PODER ARMAZENAR ESSA LINHA GERADA NA MATRIZ POR N VEZES (N = QTD DE LINHAS)
def gerarMatriz(num_linhas, num_colunas):
    matriz = []
    #criar um for para linhas
    for i in range(num_linhas):
        linha = []
        #Quantas colunas serão geradas, assim como os número das linhas serão preenchidos
        for X in range(num_colunas): 
            rand = random.randint(1, 20)
            #armazeno na lista linha um numero aleatorio
            linha.append(rand)
        #armazeno em matriz a lista linha, PRECISO DE VARIAS LISTAS EM UMA LISTA PARA SER UMA MATRIZ 
        matriz.append(linha) 
    return matriz
    

'''linhas = int(input("Informe o numero de linhas da matriz: "))
colunas = int(input("Informe o numero de colunas da matriz: "))
matriz = gerarMatriz(linhas,colunas)
print(matriz) #assim imprimirá as listas em uma linha
for linha in matriz: #assim imprimirá cada lista em uma linha
    print(linha)'''


