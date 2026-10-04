{-
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

-}

import Control.Monad (unless)

-- Liczba sposobów uzbierania dokładnie n punktów ruchami z listy
-- (kolejność ruchów nie ma znaczenia): sposoby z co najmniej jednym
-- pierwszym ruchem z listy + sposoby bez tego ruchu.
-- Złożoność czasowa: wykładnicza względem n (dla małych n wystarczająca)
-- Złożoność pamięciowa: O(n) - przez stos rekurencji
liczbaSposobow :: Int -> [Int] -> Integer
liczbaSposobow 0 _ = 1
liczbaSposobow _ [] = 0
liczbaSposobow n ruchy@(r : reszta)
  | n < 0 = 0
  | otherwise = liczbaSposobow (n - r) ruchy + liczbaSposobow n reszta

gra :: Int -> Integer
gra n = liczbaSposobow n [10, 5, 3]

main :: IO ()
main = do
  let testy =
        [ gra 1 == 0,
          gra 10 == 2,
          gra 20 == 4,
          gra 50 == 14
        ]
  unless (and testy) $ error "Test nie przeszedl"
  putStrLn "Wszystkie testy zakonczone sukcesem"
