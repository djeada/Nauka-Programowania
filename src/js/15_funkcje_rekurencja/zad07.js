/*
ZAD-07 — Wyszukiwanie liniowe rekurencyjnie

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `listy`, `wyszukiwanie`

### Treść

Napisz rekurencyjną funkcję `wyszukaj(lista, klucz, indeks=0)`, która zwraca indeks **pierwszego** wystąpienia liczby `klucz` w liście, sprawdzając kolejne elementy od pozycji `indeks`. Jeśli klucz nie występuje w liście, funkcja zwraca `-1`.

Program wczytuje listę i klucz, wywołuje funkcję i wypisuje wynik.

### Wejście

* 1. linia: `n` — liczba elementów listy
* 2. linia: `n` liczb całkowitych oddzielonych spacjami
* 3. linia: `klucz` — liczba całkowita

### Wyjście

Jedna liczba całkowita — indeks pierwszego wystąpienia klucza (indeksy liczymy od `0`) albo `-1`, jeśli klucza nie ma w liście.

### Ograniczenia

* `1 ≤ n ≤ 100`
* elementy listy i klucz są z zakresu `-1000 … 1000`

### Przykład

**Wejście:**

```
3
1 2 2
2
```

**Wyjście:**

```
1
```

Liczba `2` występuje na pozycjach `1` i `2` — wypisujemy pierwszą z nich.

### Uwagi

* Przypadki bazowe: `indeks` wyszedł poza listę (klucza nie ma) albo `lista[indeks]` jest równe kluczowi. W przeciwnym razie szukaj dalej od pozycji `indeks + 1`.

### Kod startowy

```python
def wyszukaj(lista, klucz, indeks=0):
    pass


n = int(input())
lista = [int(x) for x in input().split()]
klucz = int(input())
print(wyszukaj(lista, klucz))
```

*/

function wyszukiwanieLinioweRekurencyjnie(lista, klucz) {
  if (lista.length === 0) {
    return -1;
  }
  if (lista[0] === klucz) {
    return 0;
  }
  var wynik = wyszukiwanieLinioweRekurencyjnie(lista.slice(1), klucz);
  if (wynik === -1) {
    return -1;
  }
  return wynik + 1;
}

function test() {
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 2) === 1,
    "Test 1 failed"
  );
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 3) === -1,
    "Test 2 failed"
  );
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 1) === 0,
    "Test 3 failed"
  );
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 4) === -1,
    "Test 4 failed"
  );
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 0) === -1,
    "Test 5 failed"
  );
}

test();

