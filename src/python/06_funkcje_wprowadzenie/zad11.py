r"""
ZAD-11 — Funkcja sprawdzona testami (assert)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `assert`, `testy`, `bool`

### Treść

Napisz funkcję `czy_przestepny(rok)`, która zwraca `True`, jeśli `rok` jest przestępny, a `False` w przeciwnym razie.

Rok jest przestępny, jeśli jest podzielny przez 4, ale nie przez 100 — albo jeśli jest podzielny przez 400.

Kod startowy zawiera pięć **testów** funkcji zapisanych instrukcją `assert`. Są wykonywane, zanim program zacznie wczytywać dane. Następnie program wczytuje `n` lat i dla każdego wypisuje `Tak` (rok przestępny) albo `Nie`.

### Wejście

* 1. linia: liczba lat `n`
* kolejne `n` linii: lata — po jednej liczbie naturalnej w linii

### Wyjście

`n` linii — dla każdego roku `Tak` albo `Nie`.

### Ograniczenia

* $n \ge 1$
* $1 \le \text{rok} \le 10000$

### Przykład

**Wejście:**

```
3
2024
1900
2000
```

**Wyjście:**

```
Tak
Nie
Tak
```

Rok 1900 jest podzielny przez 100, ale nie przez 400, więc nie jest przestępny.

### Uwagi

* `assert warunek` nie robi nic, jeśli warunek jest prawdziwy. Jeśli jest fałszywy, program **natychmiast się zatrzymuje** z błędem `AssertionError`. Dzięki temu od razu widać, że funkcja działa źle.
* Gdy test się nie powiedzie, zobaczysz komunikat w rodzaju:

  ```
  Traceback (most recent call last):
    File "main.py", line 9, in <module>
      assert czy_przestepny(1900) == False
  AssertionError
  ```

  Czytaj go od dołu: `AssertionError` mówi, że nie powiódł się test, a linia nad nim (i jej numer, zależny od Twojego kodu) pokazuje, który — tutaj funkcja zwróciła złą odpowiedź dla roku 1900. Popraw funkcję i uruchom program ponownie.
* Do testu możesz dopisać komunikat, który pojawi się przy błędzie: `assert czy_przestepny(1900) == False, "1900 nie jest przestępny"`.
* Nie usuwaj testów — możesz za to dopisać własne.

### Kod startowy

```python
def czy_przestepny(rok):
    pass


assert czy_przestepny(2024) == True
assert czy_przestepny(2023) == False
assert czy_przestepny(1900) == False
assert czy_przestepny(2000) == True
assert czy_przestepny(2100) == False

n = int(input())
for _ in range(n):
    rok = int(input())
    if czy_przestepny(rok):
        print("Tak")
    else:
        print("Nie")
```

"""


def czy_przestepny(rok):
    """Zwraca True, jeśli rok jest przestępny."""
    return (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0


if __name__ == "__main__":
    # Testy funkcji (część treści zadania).
    assert czy_przestepny(2024) == True
    assert czy_przestepny(2023) == False
    assert czy_przestepny(1900) == False
    assert czy_przestepny(2000) == True
    assert czy_przestepny(2100) == False

    n = int(input())
    for _ in range(n):
        rok = int(input())
        if czy_przestepny(rok):
            print("Tak")
        else:
            print("Nie")
