r"""
ZAD-07 — Prawa logiki (p, q, r)

**Poziom:** ★★☆
**Tagi:** `bool`, `logika`, `tabele prawdy`, `formatowanie`

### Treść

Wczytaj wartości logiczne `p`, `q` i `r` i sprawdź dla nich osiem praw logiki.
Każde prawo to równoważność lewej strony `L` i prawej strony `R`:

1. `Prawo wyłączonego środka` — `L = p or not p`, `R = True`
2. `Prawo niesprzeczności` — `L = not (p and not p)`, `R = True`
3. `Przemienność koniunkcji` — `L = p and q`, `R = q and p`
4. `Przemienność alternatywy` — `L = p or q`, `R = q or p`
5. `Pierwsze prawo de Morgana` — `L = not (p and q)`, `R = not p or not q`
6. `Drugie prawo de Morgana` — `L = not (p or q)`, `R = not p and not q`
7. `Rozdzielność koniunkcji względem alternatywy` — `L = p and (q or r)`, `R = (p and q) or (p and r)`
8. `Rozdzielność alternatywy względem koniunkcji` — `L = p or (q and r)`, `R = (p or q) and (p or r)`

Dla każdego prawa oblicz `L` i `R` dla wczytanych wartości i sprawdź instrukcją `if`, czy są równe.

### Wejście

* 1. linia: `p` — napis `True` albo `False`
* 2. linia: `q` — napis `True` albo `False`
* 3. linia: `r` — napis `True` albo `False`

### Wyjście

8 linii — po jednej dla każdego prawa, w kolejności z listy:

`<nazwa prawa>: L=<L> R=<R> -> równoważne`

gdy `L` jest równe `R`, albo `<nazwa prawa>: L=<L> R=<R> -> nierównoważne` w przeciwnym razie.
`<L>` i `<R>` to dosłownie `True` albo `False`. (Wszystkie prawa z listy są prawdziwe, więc poprawny program zawsze wypisze `równoważne` — różnić się będą wartości `L` i `R`).

### Przykład

**Wejście:**

```
False
True
False
```

**Wyjście:**

```
Prawo wyłączonego środka: L=True R=True -> równoważne
Prawo niesprzeczności: L=True R=True -> równoważne
Przemienność koniunkcji: L=False R=False -> równoważne
Przemienność alternatywy: L=True R=True -> równoważne
Pierwsze prawo de Morgana: L=True R=True -> równoważne
Drugie prawo de Morgana: L=False R=False -> równoważne
Rozdzielność koniunkcji względem alternatywy: L=False R=False -> równoważne
Rozdzielność alternatywy względem koniunkcji: L=False R=False -> równoważne
```

### Uwagi

* `input()` zwraca **napis**. Nie zamieniaj go przez `bool(...)` — `bool("False")` to `True` (każdy niepusty napis jest prawdziwy). Zamiast tego porównaj: `p = input() == "True"`.
* f-string wstawia wartość logiczną jako tekst: `f"L={True}"` daje `L=True`.

### Kod startowy

```python
p = input() == "True"
q = input() == "True"
r = input() == "True"

L = p or not p
R = True
if L == R:
    print(f"Prawo wyłączonego środka: L={L} R={R} -> równoważne")
else:
    print(f"Prawo wyłączonego środka: L={L} R={R} -> nierównoważne")

```

"""


def wiersz(nazwa, lewa, prawa):
    if lewa == prawa:
        wynik = "równoważne"
    else:
        wynik = "nierównoważne"
    return f"{nazwa}: L={lewa} R={prawa} -> {wynik}"


if __name__ == "__main__":
    p = input() == "True"
    q = input() == "True"
    r = input() == "True"

    print(wiersz("Prawo wyłączonego środka", p or not p, True))
    print(wiersz("Prawo niesprzeczności", not (p and not p), True))
    print(wiersz("Przemienność koniunkcji", p and q, q and p))
    print(wiersz("Przemienność alternatywy", p or q, q or p))
    print(wiersz("Pierwsze prawo de Morgana", not (p and q), not p or not q))
    print(wiersz("Drugie prawo de Morgana", not (p or q), not p and not q))
    print(
        wiersz(
            "Rozdzielność koniunkcji względem alternatywy",
            p and (q or r),
            (p and q) or (p and r),
        )
    )
    print(
        wiersz(
            "Rozdzielność alternatywy względem koniunkcji",
            p or (q and r),
            (p or q) and (p or r),
        )
    )
