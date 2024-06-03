'''Crie uma função que faça o print de qualquer matriz passada. Use essa
função para imprimir a matriz criada no item 1.'''
import random
#PRECISO DE 2 FORS, PARA PODER GERAR 1 LINHA DE NUMEROS E OUTRO PARA PODER ARMAZENAR ESSA LINHA GERADA NA MATRIZ POR N VEZES (N = QTD DE LINHAS)
while True:
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
    linhas = int(input("Informe o numero de linhas da matriz: "))
    colunas = int(input("Informe o numero de colunas da matriz: "))
    matriz = gerarMatriz(linhas,colunas)
    print("-="*30,"\n" )
    for l in range(0,linhas):
        for c in range(0,colunas):
            print(f"[{matriz[l][c]:^5}]", end="")
        print()
    print()
    

