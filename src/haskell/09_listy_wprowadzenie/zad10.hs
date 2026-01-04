{-
ZAD-10 — Czy punkty mogą być wierzchołkami trójkąta?

\**Poziom:** ★★☆
\**Tagi:** `geometria`, `warunki`, `listy`

### Treść

Wczytaj współrzędne trzech punktów `A(xA, yA)`, `B(xB, yB)`, `C(xC, yC)`.
Wypisz `Tak`, jeśli punkty **nie są współliniowe** (mogą tworzyć trójkąt), w przeciwnym razie `Nie`.

### Wejście

Sześć liczb całkowitych (każda w osobnej linii):

1. `xA`
2. `yA`
3. `xB`
4. `yB`
5. `xC`
6. `yC`

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

\**Wejście:**

```
-3
-2
-3
1
-3
0
```

\**Wyjście:**

```
Nie
```

### Uwagi

\* Sprawdź pole trójkąta: jeśli równe `0`, punkty są współliniowe.

-}
main :: IO ()
main = do
  xA <- readLn :: IO Int
  yA <- readLn :: IO Int
  xB <- readLn :: IO Int
  yB <- readLn :: IO Int
  xC <- readLn :: IO Int
  yC <- readLn :: IO Int

  -- Punkty są współliniowe jeśli (yB-yA)*(xC-xA) == (yC-yA)*(xB-xA)
  let collinear = (yB - yA) * (xC - xA) == (yC - yA) * (xB - xA)

  if not collinear
    then putStrLn "Tak"
    else putStrLn "Nie"
