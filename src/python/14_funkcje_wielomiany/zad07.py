r"""
ZAD-07 — Upraszczanie bez skutków ubocznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `listy`, `skutki uboczne`

### Treść

Zapis wielomianu może zaczynać się od zbędnych zer, np. lista `[0, 0, 3, 0, 1]` oznacza ten sam wielomian co `[3, 0, 1]`, czyli $3x^2 + 1$. W tym zadaniu (wyjątkowo) dane mogą więc zaczynać się od zer.

Napisz funkcję `uprosc(w)`, która zwraca **nową** listę współczynników bez zer wiodących. Wielomian zerowy (same zera) upraszczamy do listy `[0]`. Funkcja **nie może zmieniać** otrzymanej listy `w` — program po wywołaniu funkcji wypisuje także oryginalną listę, żeby to sprawdzić.

### Wejście

* 1. linia: `k` — liczba współczynników (`k ≥ 1`)
* 2. linia: `k` liczb całkowitych — współczynniki od najwyższej potęgi (mogą zaczynać się od zer)

### Wyjście

Dwie linie, liczby oddzielone spacją:

* 1. linia: współczynniki uproszczonego wielomianu (dla wielomianu zerowego: `0`),
* 2. linia: oryginalna lista po wywołaniu funkcji — musi być identyczna z wczytaną.

### Ograniczenia

* `1 ≤ k ≤ 20`
* `-100 ≤ a_i ≤ 100`

### Przykład

**Wejście:**

```
5
0 0 3 0 1
```

**Wyjście:**

```
3 0 1
0 0 3 0 1
```

Usuwamy tylko zera z początku — zero w środku zapisu (przy $x^1$) zostaje.

### Uwagi

* Funkcja **czysta** tylko oblicza i zwraca wynik. Funkcja ze **skutkiem ubocznym** zmienia coś poza sobą — np. listę, którą dostała jako argument.
* Lista przekazana do funkcji **nie jest kopiowana**: parametr `w` i zmienna `wspolczynniki` w programie to ta sama lista. Dlatego poniższa funkcja zwraca dobry wynik, ale psuje listę wywołującego (druga linia wyjścia byłaby `3 0 1`):

  ```python
  def uprosc_zle(w):
      while len(w) > 1 and w[0] == 0:
          w.pop(0)  # usuwa element z ORYGINALNEJ listy!
      return w
  ```

* Zamiast usuwać elementy, znajdź indeks `i` pierwszego niezerowego współczynnika i zwróć wycinek `w[i:]` — wycinek to nowa lista, a oryginał zostaje nietknięty.

### Kod startowy

```python
def uprosc(w):
    pass


k = int(input())
wspolczynniki = [int(s) for s in input().split()]
wynik = uprosc(wspolczynniki)
print(*wynik)
print(*wspolczynniki)
```

"""


def uprosc(w):
    """Zwraca nową listę współczynników bez zer wiodących ([0] dla wielomianu zerowego).

    Lista w nie jest zmieniana (funkcja nie ma skutków ubocznych).
    """
    i = 0
    while i < len(w) - 1 and w[i] == 0:
        i += 1
    return w[i:]  # wycinek tworzy nową listę


if __name__ == "__main__":
    k = int(input())
    wspolczynniki = [int(s) for s in input().split()]
    wynik = uprosc(wspolczynniki)
    print(*wynik)
    print(*wspolczynniki)
