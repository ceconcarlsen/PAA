
# ====================================================================================================================  #

#  TRABALHO PRÁTICO DA DISCIPLINA DE PROJETO E ANÁLISE DE ALGORÍTIMOS - 2020/2021 - CÓDIGO FONTE                        #
#  Bacharelado em Ciência da Computação, Faculdade de Ciências e Tecnologia - UNESP. Campus de Presidente Prudente, SP  #
#  Alunos:                                                                                                              #
#  Pedro Henrique Zago Costa - R.A.: 181257084 - e-mail institucional: pedro.zago@unesp.br                              #
#  David Jr. Rodrigues - R.A.: 181257629 - e-mail institucional: david.junior@unesp.br                                  #                                                            #
#  Gabriel Cecon Carlsen - R.A.: 181250969 - e-mail institucional: cecon.carlsen@unesp.br                               #
#  Professor: Danilo Medeiros Eler                                                                                      #
#  Linguagem Escolhida: Python 3                                                                                        #

# ====================================================================================================================  #


# ====================================================================================================================  #
#  -> FUNCIONAMENTO <-                                                                                                  #
#  O Terminal fará três perguntas bem simples:                                                                          #
#  I. Algoritmo: Aqui é inserido qual algoritmo de ordenação se deseja usar. As opções são (insira o número):           #
#    1- Bubblesort                                                                                                      #
#    2- Bubblesort com Melhorias                                                                                        #
#    3- Quicksort com o Pivô no início da lista                                                                         #
#    4- Quicksort com o Pivô no centro da lista                                                                         #
#    5- Insertionsort                                                                                                   #
#    6- Shellsort                                                                                                       #
#    7- Selectionsort                                                                                                   #
#    8- Heapsort                                                                                                        #
#    9- Mergesort                                                                                                       #
#  II. Entradas: Aqui é inserido quantas entradas (números a serem ordenados) teremos.                                  # 
#    - Testamos com os valores 1.000, 5.000, 10.000, 15.000 e 25.000; porém qualquer entrada é válida             #
#  III. Modo: Aqui é inserido de que modo os valores serão inseridos nos algoritmos de ordenação. Podem ser:            #
#    1- Normal (padrão, aleatório, caso médio)                                                                          #
#    2- Ordenado (melhor caso, ideal)                                                                                   #
#    3- Ordenado Inversamente (pior caso)                                                                               #
# ====================================================================================================================  #


import random
import time
import numpy as np
import matplotlib.pyplot as plt

import sys # Aumentando o limite de chamadas recursivas que serao usadas nas funcoes quicksort
sys.setrecursionlimit(1500)


def modo(vetor, dim, opcao):     # Ordena os dados em modo crescente ou decrescente para testar o melhor ou pior caso #
    if opcao == 1:
        pass
        #print(" Caso Médio -", end = '')
    elif opcao == 2:
        selectionsort(vetor, dim)
        #print(" Melhor Caso -", end = '')
    else:
        i = 0
        while i < (dim - 1):
            maior = i
            j = (i + 1)
            while j < dim:
                if vetor[j] > vetor[maior]:
                    maior = j
                j += 1
            if vetor[i] != vetor[maior]:
                vetor[i], vetor[maior] = vetor[maior], vetor[i]
            i += 1
        #print(" Pior Caso -", end = '')


def bubblesort(vetor, dim):     # Algoritmo Bubblesort #
    i = 1 
    j = 0
    while i < dim:
        while j < (dim - i):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
            j += 1
        j = 0
        i += 1


def bubblesort2(vetor, dim):     # Algoritmo Bubblesort Melhorado #   
    troca = True
    i = 0
    j = 0
    while i < (dim - 1) and troca == True:
        troca = False
        while j < (dim - i - 1):
            if vetor[j] > vetor[j + 1]:
                troca = True
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
            j += 1
        j = 0
        i += 1     

def quicksort(vetor, dim):     # Algoritmo Quicksort com Pivô no início da lista #
    if dim == 1:
        return
    if dim == 2:
        if vetor[0] > vetor[1]:
            vetor[0], vetor[1] = vetor[1], vetor[0]
    else:
        pilha = []
        pilha.append(0)
        tamanho = int(len(vetor))
        pilha.append(tamanho)
        while pilha:
            lim_dir = pilha.pop()
            lim_esq = pilha.pop()
            if (lim_dir - lim_esq >= 2):
                pivo = auxiliar_quick_1(vetor, lim_esq, lim_dir)
                pilha.append(pivo + 1)
                pilha.append(lim_dir)
                pilha.append(lim_esq)
                pilha.append(pivo)

def auxiliar_quick_1(vetor, inicio, fim):
    pivo = vetor[inicio]
    i = fim
    j = fim - 1
    while j > inicio:
        if vetor[j] > pivo:
            i -= 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
        j -= 1
    while j != (i - 1):
        vetor[j] = vetor[j + 1]
        j += 1
    vetor[i - 1] = pivo
    return (i - 1)


def quicksort2(vetor, dim):     # Algoritmo Quicksort com Pivô no centro da lista #
    if dim == 1:
        return
    if dim == 2:
        if vetor[0] > vetor[1]:
            vetor[0], vetor[1] = vetor[1], vetor[0]
    else:
        pilha = []
        pilha.append(0)
        tamanho = int(len(vetor))
        pilha.append(tamanho - 1)
        while pilha:
            lim_dir = pilha.pop()
            lim_esq = pilha.pop()
            if (lim_esq < lim_dir):
                esquerda, direita = auxiliar_quick_2(vetor, lim_esq, lim_dir)
                pilha.append(esquerda)
                pilha.append(lim_dir)
                pilha.append(lim_esq)
                pilha.append(direita)

def auxiliar_quick_2(vetor, inicio, fim):
    pivo = vetor[int((inicio + fim) / 2)]
    esquerda = inicio
    direita = fim
    while esquerda <= direita:
        while vetor[esquerda] < pivo:
            esquerda += 1
        while vetor[direita] > pivo:
            direita -= 1
        if esquerda <= direita:
            vetor[esquerda], vetor[direita] = vetor[direita], vetor[esquerda]
            esquerda += 1
            direita -= 1
    return esquerda, direita


def insertionsort(vetor, dim):     # Algoritmo Insertionsort #
    i = 1
    while i < dim:
        x = vetor[i]
        j = (i - 1)
        while j >= 0 and vetor[j] > x:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = x
        i += 1


def shellsort(vetor, dim):     # Algoritmo Shellsort #
    h = 1
    while h < dim:
        h = 3 * h + 1
    while h > 1:
        h = int(h / 3)
        i = h
        while i < dim:
            aux = vetor[i]
            j = i - h
            while j >= 0 and aux < vetor[j]:
                vetor[j + h] = vetor[j]
                j -= h
            vetor[j + h] = aux
            i += 1


def selectionsort(vetor, dim):     # Algoritmo Selectionsort #
    i = 0
    while i < (dim - 1):
        menor = i
        j = (i + 1)
        while j < dim:
            if vetor[j] < vetor[menor]:
                menor = j
            j += 1
        if vetor[i] != vetor[menor]:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
        i += 1


def heapsort(vetor, dim):     # Algoritmo Heapsort #
    i = int(dim / 2)
    while i >= 0:
        auxiliar_heap(vetor, i, dim - 1)
        i -= 1
    i = dim - 1
    while i >= 1:
        vetor[0], vetor[i] = vetor[i], vetor[0]
        auxiliar_heap(vetor, 0, i - 1)
        i -= 1

def auxiliar_heap(vetor, raiz, fundo):
    ok = False
    while (raiz * 2) <= fundo and ok != True:
        if (raiz * 2) == fundo:
            maximo = raiz * 2
        elif vetor[(raiz * 2)] > vetor[(raiz * 2) + 1]:
            maximo = raiz * 2
        else:
            maximo = (raiz * 2) + 1
        
        if vetor[raiz] < vetor[maximo]:
            vetor[raiz], vetor[maximo] = vetor[maximo], vetor[raiz]
            raiz = maximo
        else:
            ok = True


def mergesort(vetor):     # Algoritmo Mergesort #
    if len(vetor) > 1:
        mid = int(len(vetor) / 2)
        esquerda = vetor[:mid]
        direita = vetor[mid:]
        mergesort(esquerda)
        mergesort(direita)
        i = 0
        j = 0
        k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1


# Main
valido = 0
while valido == 0:
    print('')
    print(' (1) para realizar calculos e (2) para calcular tempo: ', end = '')
    opc = int(input())
    if opc >= 1 and opc <= 2:
        valido = 1
    else:
        print(" Por favor, insira um valor válido (entre 1 e 2). ")
        print("")

if opc == 1: # Calculando 
    valido = 0
    while valido == 0:
        print("")
        print(" Algoritmo: ", end = '')     # Escolhendo o algoritmo desejado #
        alg = int(input())
        if alg >= 1 and alg <= 9:
            valido = 1
        else:
            print(" Por favor, insira um valor válido (entre 1 e 9). ")
            print("")
    valido = 0
    while valido == 0:        
        print(" Entradas: ", end = '')     # Escolhendo o número de entradas desejado #
        ent = int(input())
        if ent > 0:
            valido = 1
        else:
            print(" Por favor, insira um valor válido (maior que zero). ")
            print("")
    valido = 0
    while valido == 0:
        print(" Modo: ", end = '')     # Escolhendo o modo desejado (normal, melhor ou pior caso)#
        mod = int(input())
        if mod >= 1 and mod <= 3:
            valido = 1
            if mod == 1:
                print(" Caso Médio -", end = '')
            elif mod == 2:
                print(" Melhor Caso -", end = '')
            elif mod == 3:
                print(" Pior Caso -", end = '')
        else:
            print(" Por favor, insira um valor válido (entre 1 e 3). ")
            print("")


    elementos = []
    for j in range(0, ent):
        i = random.randint(0, 25000)
        elementos.append(i)


    Dim = len(elementos)
    modo(elementos, Dim, mod)


    clock_start = time.time()
    if alg == 1:
        print(" Bubblesort ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        bubblesort(elementos, Dim)
    elif alg == 2:
        print(" Bubblesort Melhorado ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        bubblesort2(elementos, Dim)
    elif alg == 3:
        print(" Quicksort com Pivô no início da lista ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        quicksort(elementos, Dim)
    elif alg == 4:
        print(" Quicksort com Pivô no centro da lista ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        quicksort2(elementos, Dim)
    elif alg == 5:
        print(" Insertionsort ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        insertionsort(elementos, Dim)
    elif alg == 6:
        print(" Shellsort ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        shellsort(elementos, Dim)
    elif alg == 7:
        print(" Selectionsort ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        selectionsort(elementos, Dim)
    elif alg == 8:
        print(" Heapsort ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        heapsort(elementos, Dim)
    else:
        print(" Mergesort ")
        print("")
        if Dim <= 20:
            print(" pré-ordenação: ", elementos)
        mergesort(elementos)

    clock_end = time.time()
    if Dim <= 20:
        print(" pós-ordenação: ", elementos)
    print(" tempo de execução: ",(clock_end - clock_start), " segundos.")
    print("")
    print(" Pedro Henrique Zago Costa, David Jr. Rodrigues e Gabriel Cecon Carlsen. ")
    print("")


elif opc == 2: # impressao da tabelas com o devido tempo
    valido = 0
    while valido == 0:        
        print(" Entradas: ", end = '')     # Escolhendo o número de entradas desejado #
        ent = int(input())
        if ent > 0:
            valido = 1
        else:
            print(" Por favor, insira um valor válido (maior que zero). ")
            print("")
    valido = 0
    while valido == 0:
        print(" Modo: ", end = '')     # Escolhendo o modo desejado (normal, melhor ou pior caso)#
        mod = int(input())
        if mod >= 1 and mod <= 3:
            valido = 1
        else:
            print(" Por favor, insira um valor válido (entre 1 e 3). ")
            print("")

    height = []
    count = 0
    while count <= 8:
        elementos = []
        for j in range(0, ent):
            i = random.randint(0, 25000)
            elementos.append(i)
        Dim = len(elementos)
        modo(elementos, Dim, mod)
        if count == 0:
            clock_start = time.time()
            bubblesort(elementos, Dim)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print("\n Algoritmo   | tempo")
            print(" BubbleSort  | ",(clock_end - clock_start), " seg.")
        elif count == 1:
            clock_start = time.time()
            bubblesort2(elementos, Dim)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print(" BubbleSort 2| ",(clock_end - clock_start), " seg.")
        elif count == 2:
            clock_start = time.time()
            quicksort(elementos, Dim)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print(" Quicksort   | ",(clock_end - clock_start), " seg.")
        elif count == 3:
            clock_start = time.time()
            quicksort2(elementos, Dim)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print(" Quicksort 2 | ",(clock_end - clock_start), " seg.")
        elif count == 4:
            clock_start = time.time()
            insertionsort(elementos, Dim)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print(" Insertion   | ",(clock_end - clock_start), " seg.")
        elif count == 5:
            clock_start = time.time()
            shellsort(elementos, Dim)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print(" Shellsort   | ",(clock_end - clock_start), " seg.")
        elif count == 6:
            clock_start = time.time()
            selectionsort(elementos, Dim)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print(" Selection   | ",(clock_end - clock_start), " seg.")
        elif count == 7:
            clock_start = time.time()
            heapsort(elementos, Dim)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print(" Heapsort    | ",(clock_end - clock_start), " seg.")
        else:
            clock_start = time.time()
            mergesort(elementos)
            clock_end = time.time()
            height.append(clock_end - clock_start)
            print(" Mergesort   | ",(clock_end - clock_start), " seg.\n")

        count += 1

    # Plotando grafico
    bars = ('BS', 'BS2', 'QC', 'QC2', 'IS', 'SL', 'SE', 'HP', 'MG')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))

    # Inserindo os devidos nomes das barras
    plt.xticks(y_pos, bars, color='red', rotation=45, fontweight='bold', fontsize='17', horizontalalignment='right')
 
    # Titulo do eixo Y
    plt.ylabel('Tempo em segundos', fontweight='bold', color = 'red', fontsize='17', horizontalalignment='center')

    # Exibe o grafico desenvolvido acima
    plt.show()



# ========================================================================= #
#  Pedro Henrique Zago Costa - David Jr. Rodrigues - Gabriel Cecon Carlsen  #
# ========================================================================= #
