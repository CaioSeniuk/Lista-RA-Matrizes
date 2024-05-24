'''Crie uma função que faça o print de qualquer matriz passada. Use essa
função para imprimir a matriz criada no item 1.'''
from ex1 import  gerarMatriz,linhas,colunas

matriz = gerarMatriz(linhas,colunas)
def imprime_matriz(matriz):
    for i in matriz:
        print(i)

