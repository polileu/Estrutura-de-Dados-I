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


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)
