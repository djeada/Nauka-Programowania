r"""
ZAD-08 — Indeks klucza w cyklicznie posortowanej liście

**Poziom:** ★★☆
**Tagi:** `binary search`, `rotacja`, `list`

### Treść

Lista liczb całkowitych była posortowana rosnąco, a następnie została **cyklicznie przesunięta** (jej początkowy fragment przeniesiono na koniec), np. `1 2 3 4 5 6` → `3 4 5 6 1 2`. Znajdź indeks (liczony od 0), pod którym w tej liście znajduje się podany klucz. Jeśli klucza nie ma w liście, wypisz `-1`.

### Wejście

* 1. linia: liczba elementów $N$
* 2. linia: $N$ liczb całkowitych oddzielonych spacjami — cyklicznie przesunięta lista rosnąca
* 3. linia: liczba całkowita $x$ — szukany klucz

### Wyjście

* 1. linia: indeks elementu równego $x$ albo `-1`

### Ograniczenia

* $1 \le N \le 1000$
* Wszystkie elementy listy są różne.
* Przesunięcie może wynosić 0 (lista jest wtedy po prostu posortowana).

### Przykład

**Wejście:**

```
6
3 4 5 6 1 2
4
```

**Wyjście:**

```
1
```

### Uwagi

* Zadanie da się rozwiązać w czasie $O(\log N)$ zmodyfikowanym wyszukiwaniem binarnym: po podziale przedziału na pół **co najmniej jedna** z połówek jest posortowana rosnąco — sprawdź, czy klucz mieści się w jej zakresie, i na tej podstawie wybierz połowę do dalszego przeszukiwania.
* To rozwinięcie zwykłego wyszukiwania binarnego — zob. zadanie „Wyszukiwanie binarne” z rozdziału 21.

"""


def znajdz_klucz(lista, klucz):
    lewo, prawo = 0, len(lista) - 1
    while lewo <= prawo:
        srodek = (lewo + prawo) // 2
        if lista[srodek] == klucz:
            return srodek
        if lista[lewo] <= lista[srodek]:
            # lewa połowa lista[lewo..srodek] jest posortowana
            if lista[lewo] <= klucz < lista[srodek]:
                prawo = srodek - 1
            else:
                lewo = srodek + 1
        else:
            # prawa połowa lista[srodek..prawo] jest posortowana
            if lista[srodek] < klucz <= lista[prawo]:
                lewo = srodek + 1
            else:
                prawo = srodek - 1
    return -1


if __name__ == "__main__":
    n = int(input())
    lista = [int(x) for x in input().split()]
    klucz = int(input())
    print(znajdz_klucz(lista, klucz))
