/*
ZAD-10 — Gra

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `kombinatoryka`

### Treść

W grze w każdym ruchu gracz zdobywa `3`, `5` albo `10` punktów. Gracz wygrywa, gdy uzbiera **dokładnie** `N` punktów.

Napisz rekurencyjną funkcję `liczba_sposobow(n, ruchy)`, która zwraca, na ile sposobów można uzbierać dokładnie `n` punktów, używając ruchów o wartościach z listy `ruchy`. Sposoby różniące się tylko kolejnością ruchów traktujemy jako ten sam sposób — liczy się tylko, ile razy gracz zdobył `3`, ile razy `5`, a ile razy `10` punktów.

Program wczytuje `N` i wypisuje liczbę sposobów wygrania gry.

### Wejście

Jedna liczba naturalna `N` (`N ≥ 1`).

### Wyjście

Jedna liczba naturalna — liczba sposobów (może wynosić `0`).

### Ograniczenia

* `1 ≤ N ≤ 100`

### Przykład

**Wejście:**

```
20
```

**Wyjście:**

```
4
```

Sposoby: $10 + 10$, $10 + 5 + 5$, $5 + 5 + 5 + 5$ oraz $5 + 3 + 3 + 3 + 3 + 3$.

### Uwagi

* Rozbij problem na dwa mniejsze: sposoby, w których **co najmniej raz** użyjemy pierwszego ruchu z listy (wtedy zostaje `n - ruchy[0]` punktów, a lista ruchów się nie zmienia), oraz sposoby, w których tego ruchu **nie użyjemy wcale** (te same `n` punktów, lista `ruchy[1:]`). Wynik to suma obu liczb.
* Przypadki bazowe: `n == 0` — znaleźliśmy jeden sposób; `n < 0` albo pusta lista ruchów — żadnego sposobu.

### Kod startowy

```python
def liczba_sposobow(n, ruchy):
    pass


n = int(input())
print(liczba_sposobow(n, [10, 5, 3]))
```

*/

function liczbaSposobowWygranej(n, minRuch = 3, memo = {}) {
  // Funkcja oblicza liczbę sposobów (nieuporządkowanych) osiągnięcia n punktów
  // Złożoność czasowa: O(n) z memoizacją
  // Złożoność pamięciowa: O(n)
  if (n === 0) return 1;
  if (n < 0) return 0;
  
  const klucz = `${n},${minRuch}`;
  if (klucz in memo) return memo[klucz];
  
  let sposoby = 0;
  
  // Aby uniknąć powtórzeń, używamy tylko ruchów >= minRuch
  if (minRuch <= 3 && n >= 3) {
    sposoby += liczbaSposobowWygranej(n - 3, 3, memo);
  }
  if (minRuch <= 5 && n >= 5) {
    sposoby += liczbaSposobowWygranej(n - 5, 5, memo);
  }
  if (minRuch <= 10 && n >= 10) {
    sposoby += liczbaSposobowWygranej(n - 10, 10, memo);
  }
  
  memo[klucz] = sposoby;
  return sposoby;
}

// Testy
function testLiczbaSposobowWygranej() {
  let n;
  let wynik;

  n = 6;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 1, "Test 1 nieudany"); // Tylko 3+3

  n = 10;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 2, "Test 2 nieudany");

  n = 20;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 4, "Test 3 nieudany");

  n = 25;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 5, "Test 4 nieudany");
}

testLiczbaSposobowWygranej();
console.log("Wszystkie testy zakończone sukcesem");

