
#1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.


l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
l1 = []

def flatten(l):

    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            l1.append(i)

flatten(l)
print(l1)



#2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.


l = [[1, 2], [3, 4], [5, 6, 7]]

def new_list(l):
    for i in l:
        i.reverse()
    l.reverse()
    return(l)

print(l)

print(new_list(l))