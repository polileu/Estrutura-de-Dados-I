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

vect = [3,90,65,71,-2,22,30]
bubbleSort(vect)
print(vect)