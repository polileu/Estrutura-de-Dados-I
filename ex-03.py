import time
import random

# Função para criar vetores embaralhados
def cria_vetor_embaralhado(n):
    vetor = list(range(1, n+1))
    random.shuffle(vetor)
    return vetor

# Implementação do BubbleSort
def bubbleSort(v):
    i = 0
    v_len = len(v) - 1
    while i < v_len:
        j = 0
        while j < v_len - i:
            if v[j] > v[j+1]:
                tmp = v[j]
                v[j] = v[j + 1]
                v[j+1] = tmp
            j+=1
        i+=1

# Implementação do QuickSort
def particiona(v, a, b):
    x = v[a]
    while a < b:
        while v[a] < x:
            a += 1
        while v[b] > x:
            b -= 1
        if a <= b:
            troca(v, a, b)
    return a


def troca (v,a,b):
   temp = v[a]
   v[a] = v[b]
   v[b] = temp

def quickSort(v,a,b):
   if a < b:
       p = particiona(v,a,b)
       quickSort(v,a,p - 1)
       quickSort(v,p + 1,b)

# Implementação do mergeSort
def merge_sort(A):
    if len(A) <= 1:
        return A
    
    
    meio = len(A) // 2
    esquerda = merge_sort(A[:meio])
    direita = merge_sort(A[meio:])
    
    
    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i, j = 0, 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado


def main():
    tamanhos = [10, 100, 1000, 10000]
    for n in tamanhos:
        vetor1 = cria_vetor_embaralhado(n)
        vetor2 = vetor1.copy()
        vetor3 = vetor1.copy()

        # Bubble Sort
        tempo_inicial = time.time()
        bubbleSort(vetor1)
        bubble_time = time.time() - tempo_inicial

        # Quick Sort
        tempo_inicial = time.time()
        quickSort(vetor2, 0, n-1)
        quick_time = time.time() - tempo_inicial

        # Merge Sort
        tempo_inicial = time.time()
        merge_sort(vetor3)
        merge_time = time.time() - tempo_inicial

        # Impressão dos resultados para o tamanho atual do vetor
        print(f"\nResultados para vetor de tamanho {n}")
        print(f"Tempo para Bubble Sort: {bubble_time:.7f} segundos")
        print(f"Tempo para Quick Sort: {quick_time:.7f} segundos")
        print(f"Tempo para Merge Sort: {merge_time:.7f} segundos")

if __name__ == "__main__":
    main()