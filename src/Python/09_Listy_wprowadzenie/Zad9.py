import math

"""
Otrzymujesz listę liczb naturalnych. Usuń z niej 
wszystkie duplikaty. Tylko pierwsze wystąpienie danej 
liczby powinno zostać zachowane.
"""

def usun_duplikaty_v1(lista):
    lista_nowa = []
    for i in lista:
        if i not in lista_nowa:
            lista_nowa.append(i)
    return lista_nowa

def usun_duplikaty_v2(lista):
    return list(set(lista))

def test_usun_duplikaty_v1():
    assert usun_duplikaty_v1([]) == []
    assert usun_duplikaty_v1([1,1,1, 1, 1]) == [1]
    assert usun_duplikaty_v1([3, 5, 3, 3, 2) == [3, 5, 2]
    

if __name__ == "__main__":

    test_usun_duplikaty_v1()
    