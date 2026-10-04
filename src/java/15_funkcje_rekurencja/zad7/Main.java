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

public class Main {

  public static int wyszukaj(int[] lista, int klucz) {
    return wyszukaj(lista, klucz, 0);
  }

  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n) - rekurencja uzywa stosu
  public static int wyszukaj(int[] lista, int klucz, int indeks) {
    // Zwraca indeks pierwszego wystapienia klucza (od pozycji indeks) albo -1.
    if (indeks >= lista.length) {
      return -1;
    }

    if (lista[indeks] == klucz) {
      return indeks;
    }

    return wyszukaj(lista, klucz, indeks + 1);
  }

  public static void test1() {
    assert wyszukaj(new int[] {1, 2, 2}, 2) == 1;
    assert wyszukaj(new int[] {4, 8, 15, 16, 23}, 4) == 0;
    assert wyszukaj(new int[] {4, 8, 15, 16, 23}, 23) == 4;
    assert wyszukaj(new int[] {10, 20, 30}, 25) == -1;
  }

  public static void main(String[] args) {

    test1();
  }
}
