r"""
ZAD-10 — Maksymalna suma spójnego fragmentu (algorytm Kadane'a)

**Poziom:** ★★☆
**Tagi:** `list`, `kadane`, `dp`, `fragment`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź **niepusty spójny fragment** listy (kolejne elementy od indeksu `p` do indeksu `k` włącznie, $p \le k$) o **największej sumie**. Wypisz tę sumę oraz indeksy początku i końca fragmentu.

* Jeśli kilka fragmentów ma tę samą, największą sumę — wybierz ten o **najmniejszym indeksie początku** `p`, a jeśli nadal jest remis — **najkrótszy** (o najmniejszym `k`).
* Fragment musi mieć co najmniej jeden element, więc gdy wszystkie liczby są ujemne, wynikiem jest największa z nich (pierwsze jej wystąpienie).

### Wejście

* 1. linia: `n` — długość listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

* 1. linia: największa suma
* 2. linia: dwie liczby `p k` oddzielone spacją — indeksy (liczone od `0`) pierwszego i ostatniego elementu fragmentu

### Ograniczenia

* $1 \le n \le 10^5$
* elementy listy są z przedziału $[-10^4, 10^4]$

### Przykład

**Wejście:**

```
9
-2 1 -3 4 -1 2 1 -5 4
```

**Wyjście:**

```
6
3 6
```

Fragment od indeksu 3 do 6: $4 + (-1) + 2 + 1 = 6$.

### Przykład 2

**Wejście:**

```
5
4 -4 1 3 -1
```

**Wyjście:**

```
4
0 0
```

Sumę 4 mają fragmenty `0..0`, `0..3` i `2..3`. Najwcześniej zaczynają się dwa pierwsze, a z nich krótszy jest `0..0`.

### Uwagi

* Sprawdzanie wszystkich fragmentów to około $n^2/2$ par `(p, k)` — przy $n = 10^5$ to miliardy działań. **Algorytm Kadane'a** robi to w jednym przejściu, w czasie $O(n)$: idąc po liście, pamiętaj sumę najlepszego fragmentu **kończącego się** na bieżącym elemencie oraz jego początek. Jeśli ta suma przed dołożeniem nowego elementu jest ujemna, opłaca się zacząć nowy fragment od bieżącego elementu; w przeciwnym razie przedłużasz dotychczasowy.
* Remisy rozstrzygną się zgodnie z treścią, jeśli nowy fragment zaczniesz tylko przy sumie **ściśle ujemnej** (przy sumie `0` przedłużaj — początek zostaje wcześniejszy), a najlepszy wynik zmienisz tylko na **ściśle większy**.

### Kod startowy

```python
def maks_fragment(liczby):
    najlepsza, poczatek, koniec = liczby[0], 0, 0
    return najlepsza, poczatek, koniec


n = int(input())
liczby = [int(x) for x in input().split()]
suma, poczatek, koniec = maks_fragment(liczby)
print(suma)
print(poczatek, koniec)
```

"""


def maks_fragment(liczby):
    """Algorytm Kadane'a: zwraca (suma, początek, koniec) najlepszego spójnego fragmentu.

    Przy remisie wybiera fragment o najwcześniejszym początku, a potem najkrótszy.
    """
    suma = liczby[0]  # najlepsza suma fragmentu kończącego się na bieżącym indeksie
    poczatek = 0  # początek tego fragmentu
    najlepsza = liczby[0]
    najlepszy_poczatek, najlepszy_koniec = 0, 0

    for i in range(1, len(liczby)):
        if suma < 0:
            # Ujemny „ogon” tylko by przeszkadzał — zaczynamy nowy fragment.
            suma = liczby[i]
            poczatek = i
        else:
            suma += liczby[i]

        if suma > najlepsza:
            najlepsza = suma
            najlepszy_poczatek, najlepszy_koniec = poczatek, i

    return najlepsza, najlepszy_poczatek, najlepszy_koniec


if __name__ == "__main__":
    n = int(input())
    liczby = [int(x) for x in input().split()]
    suma, poczatek, koniec = maks_fragment(liczby)
    print(suma)
    print(poczatek, koniec)
