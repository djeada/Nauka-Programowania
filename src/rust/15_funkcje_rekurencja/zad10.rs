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

fn liczba_sposobow(n: i32, ruchy: &[i32]) -> u64 {
    // Liczba sposobów uzbierania dokładnie n punktów ruchami z listy ruchy
    // (kolejność ruchów nie ma znaczenia).
    // Złożoność czasowa: wykładnicza względem n (dla małych n wystarczająca)
    // Złożoność pamięciowa: O(n) - przez stos rekurencji
    if n == 0 {
        return 1;
    }

    if n < 0 || ruchy.is_empty() {
        return 0;
    }

    // Sposoby z co najmniej jednym ruchem ruchy[0] + sposoby bez tego ruchu.
    liczba_sposobow(n - ruchy[0], ruchy) + liczba_sposobow(n, &ruchy[1..])
}

fn gra(n: i32) -> u64 {
    liczba_sposobow(n, &[10, 5, 3])
}

fn test_gra() {
    assert_eq!(gra(1), 0);
    assert_eq!(gra(10), 2);
    assert_eq!(gra(20), 4);
    assert_eq!(gra(50), 14);
}

fn main() {
    test_gra();
}
