r"""
ZAD-08 — Konto bankowe

**Poziom:** ★★☆
**Tagi:** `class`, `wyjątki`, `try-except`

### Treść

Zaprojektuj klasę `KontoBankowe`:

* konstruktor `__init__(self, saldo=0)` zapamiętuje saldo początkowe w atrybucie `saldo`,
* metoda `wplac(kwota)` zwiększa saldo o `kwota`. Jeśli $kwota \le 0$, metoda zgłasza wyjątek `ValueError("Kwota musi być dodatnia.")` i nie zmienia salda,
* metoda `wyplac(kwota)` zmniejsza saldo o `kwota`. Najpierw sprawdza, czy $kwota \le 0$ — wtedy zgłasza `ValueError("Kwota musi być dodatnia.")`, a następnie, czy kwota nie przekracza salda — jeśli przekracza, zgłasza `ValueError("Brak środków na koncie.")`. W obu przypadkach saldo się nie zmienia.

Metody **nie wypisują** komunikatów o błędach — tylko zgłaszają wyjątki. Wyjątki przechwytuje program główny (`try`/`except`) i wypisuje komunikat błędu.

Program tworzy konto z podanym saldem początkowym i wykonuje kolejne polecenia:

* `wplac K` — wpłaca kwotę $K$ i wypisuje `Wpłacono K. Saldo: S`,
* `wyplac K` — wypłaca kwotę $K$ i wypisuje `Wypłacono K. Saldo: S`,
* `saldo` — wypisuje `Saldo: S`,

gdzie $S$ to saldo po wykonaniu polecenia. Jeśli metoda zgłosi wyjątek, program zamiast tego wypisuje `Błąd: <komunikat wyjątku>`.

### Wejście

* 1. linia: saldo początkowe — liczba całkowita $\ge 0$
* 2. linia: liczba poleceń $n$
* kolejne $n$ linii: polecenie `wplac K`, `wyplac K` albo `saldo` ($K$ — liczba całkowita, może być ujemna lub równa 0)

### Wyjście

$n$ linii — po jednej dla każdego polecenia, w formacie opisanym w treści.

### Ograniczenia

* $1 \le n \le 100$
* $-10^6 \le K \le 10^6$, saldo początkowe nie przekracza $10^6$

### Przykład

**Wejście:**

```
100
5
wplac 50
wyplac 30
wyplac 500
wplac -20
saldo
```

**Wyjście:**

```
Wpłacono 50. Saldo: 150
Wypłacono 30. Saldo: 120
Błąd: Brak środków na koncie.
Błąd: Kwota musi być dodatnia.
Saldo: 120
```

### Uwagi

* Instrukcja `raise` zgłasza wyjątek i natychmiast przerywa działanie metody. Kod, który wywołał metodę, może wyjątek przechwycić w bloku `try`/`except`; zapis `except ValueError as e` daje dostęp do obiektu wyjątku, a `str(e)` (lub `{e}` w f-stringu) to jego komunikat:

  ```python
  def pierwiastek(x):
      if x < 0:
          raise ValueError("Liczba nie może być ujemna.")
      return x ** 0.5


  try:
      print(pierwiastek(-4))
  except ValueError as e:
      print(f"Błąd: {e}")      # Błąd: Liczba nie może być ujemna.
  ```

* Dzięki temu klasa tylko **sygnalizuje** problem, a o tym, co z nim zrobić (wypisać komunikat, zapytać ponownie, przerwać program), decyduje kod, który z niej korzysta.

### Kod startowy

```python
class KontoBankowe:
    def __init__(self, saldo=0):
        pass

    def wplac(self, kwota):
        pass

    def wyplac(self, kwota):
        pass


konto = KontoBankowe(int(input()))
n = int(input())
for _ in range(n):
    czesci = input().split()
    polecenie = czesci[0]
```

"""


class KontoBankowe:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def wplac(self, kwota):
        if kwota <= 0:
            raise ValueError("Kwota musi być dodatnia.")
        self.saldo += kwota

    def wyplac(self, kwota):
        if kwota <= 0:
            raise ValueError("Kwota musi być dodatnia.")
        if kwota > self.saldo:
            raise ValueError("Brak środków na koncie.")
        self.saldo -= kwota


def wykonaj(konto, czesci):
    polecenie = czesci[0]
    if polecenie == "saldo":
        return f"Saldo: {konto.saldo}"
    kwota = int(czesci[1])
    try:
        if polecenie == "wplac":
            konto.wplac(kwota)
            return f"Wpłacono {kwota}. Saldo: {konto.saldo}"
        konto.wyplac(kwota)
        return f"Wypłacono {kwota}. Saldo: {konto.saldo}"
    except ValueError as e:
        return f"Błąd: {e}"


if __name__ == "__main__":
    konto = KontoBankowe(int(input()))
    n = int(input())
    for _ in range(n):
        print(wykonaj(konto, input().split()))
