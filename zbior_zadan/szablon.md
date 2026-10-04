# Rozdział N: Tytuł rozdziału

Krótki opis rozdziału: czego uczą zadania i jakie zasady obowiązują we wszystkich zadaniach.

**Konwencje wspólne:**

* Każde zadanie (i każdy podpunkt) to osobny program: czyta **standardowe wejście** i wypisuje wynik na **standardowe wyjście**.
* Program nie wypisuje komunikatów typu „Podaj liczbę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.

---

## ZAD-01 — Tytuł zadania

**Poziom:** ★☆☆
**Tagi:** `petle`, `listy`

### Treść

Jasne polecenie. Wzory zapisuj w LaTeX-u między znakami dolara, np. $a^2 + b^2 = c^2$
albo $\frac{a}{b}$. Nazwy zmiennych i fragmenty kodu zapisuj w `backtickach`.

Zadanie o funkcjach: „Napisz funkcję `suma(a, b)`, która zwraca … Program wczytuje `a` i `b`,
wywołuje funkcję i wypisuje wynik.”

### Wejście

* 1. linia: `n` — liczba całkowita (`n ≥ 0`)
* 2. linia: `n` liczb całkowitych oddzielonych spacjami

### Wyjście

Jedna linia: suma liczb.

### Ograniczenia

* `0 ≤ n ≤ 1000`

### Przykład

**Wejście:**

```
3
1 2 3
```

**Wyjście:**

```
6
```

Opcjonalne wyjaśnienie przykładu (zwykły tekst pod blokami kodu).

### Uwagi

* Opcjonalne wskazówki, zasady formatowania, pułapki.

### Kod startowy

```python
def suma(liczby):
    # Uzupełnij funkcję.
    pass


n = int(input())
liczby = [int(x) for x in input().split()]
print(suma(liczby))
```

---

<!--
Zasady (sprawdzane przez scripts/md_to_json.py):

* Nagłówek zadania: "## ZAD-NN — Tytuł" lub "## ZAD-NNA — Tytuł" dla podpunktów.
* Dozwolone sekcje: Treść, Wejście, Wyjście, Ograniczenia, Przykład (Przykład 2, …),
  Uwagi (Uwagi o …), Kod startowy. Treść, Wejście, Wyjście i co najmniej jeden Przykład są obowiązkowe.
* Przykład składa się ze znaczników **Wejście:** i **Wyjście:**, po każdym blok ``` ```.
  Brak wejścia: "**Wejście:** *(brak)*". Brak wyjścia: "**Wyjście:** *(brak)*".
* Zadania na plikach: przykład zaczyna się od "**Pliki przed:**" z blokiem ``` ``` opisującym pliki
  (ścieżka w linii, treść w kolejnych liniach z prefiksem "| ", "katalog/" = pusty katalog,
  "plik (rozmiar: 12000 B)" = plik o danym rozmiarze), a po **Wyjście:** może mieć "**Pliki po:**"
  ("stary.txt (usunięty)" = plik ma nie istnieć).
* Kod startowy jest opcjonalny (domyślnie strona generuje prosty szkielet).
* Testy zadania dopisz w zbior_zadan_tests/<rozdział>.json pod kluczem "ZAD-NN".
-->
