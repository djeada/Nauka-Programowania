r"""
ZAD-09 — Cena końcowa (argumenty domyślne i nazwane)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `argumenty domyślne`, `argumenty nazwane`, `float`

### Treść

Napisz funkcję `cena_koncowa(netto, vat=23, rabat=0)`, która zwraca cenę brutto towaru po rabacie:

* najpierw od ceny `netto` odejmujemy rabat — `rabat` procent ceny netto,
* potem do tak obniżonej ceny doliczamy podatek VAT — `vat` procent.

Czyli funkcja zwraca $\text{netto} \cdot \left(1 - \frac{\text{rabat}}{100}\right) \cdot \left(1 + \frac{\text{vat}}{100}\right)$ — bez zaokrąglania.

Parametry `vat` i `rabat` mają **wartości domyślne** (23 i 0), więc przy wywołaniu można je pominąć.

Program wczytuje cenę netto oraz rabat i wywołuje funkcję czterema sposobami:

1. `cena_koncowa(netto)` — domyślny VAT 23% i brak rabatu,
2. `cena_koncowa(netto, 8)` — VAT 8% (drugi argument trafia do parametru `vat`), brak rabatu,
3. `cena_koncowa(netto, rabat=rabat)` — domyślny VAT 23% i wczytany rabat,
4. `cena_koncowa(netto, rabat=rabat, vat=5)` — VAT 5% i wczytany rabat.

### Wejście

* 1. linia: cena netto — liczba rzeczywista
* 2. linia: rabat w procentach — liczba całkowita

### Wyjście

Cztery linie — wyniki wywołań 1–4 w tej kolejności, każdy z dokładnością do **dwóch** miejsc po przecinku.

### Ograniczenia

* $\text{netto} \ge 0$
* $0 \le \text{rabat} \le 100$

### Przykład

**Wejście:**

```
100
10
```

**Wyjście:**

```
123.00
108.00
110.70
94.50
```

Np. trzecie wywołanie: $100 \cdot 0.9 = 90$, a $90 \cdot 1.23 = 110.7$.

### Uwagi

* **Argument domyślny** to wartość parametru podana w nagłówku funkcji (`vat=23`). Jeśli przy wywołaniu nie podasz tego argumentu, parametr dostanie wartość domyślną.
* **Argument nazwany** podajesz w postaci `nazwa=wartość`, np. `cena_koncowa(100, rabat=10)`. Dzięki temu możesz pominąć `vat`, a ustawić `rabat`. Kolejność argumentów nazwanych jest dowolna: `cena_koncowa(100, rabat=10, vat=5)` to to samo co `cena_koncowa(100, vat=5, rabat=10)`.
* Argumenty podane bez nazwy (pozycyjne) trafiają do parametrów po kolei: w `cena_koncowa(100, 8)` liczba `8` to `vat`.

### Kod startowy

```python
def cena_koncowa(netto, vat=23, rabat=0):
    pass


netto = float(input())
rabat = int(input())
print(f"{cena_koncowa(netto):.2f}")
print(f"{cena_koncowa(netto, 8):.2f}")
print(f"{cena_koncowa(netto, rabat=rabat):.2f}")
print(f"{cena_koncowa(netto, rabat=rabat, vat=5):.2f}")
```

"""


def cena_koncowa(netto, vat=23, rabat=0):
    """Zwraca cenę brutto: netto pomniejszone o rabat (%), powiększone o VAT (%)."""
    po_rabacie = netto * (1 - rabat / 100)
    return po_rabacie * (1 + vat / 100)


if __name__ == "__main__":
    netto = float(input())
    rabat = int(input())
    print(f"{cena_koncowa(netto):.2f}")
    print(f"{cena_koncowa(netto, 8):.2f}")
    print(f"{cena_koncowa(netto, rabat=rabat):.2f}")
    print(f"{cena_koncowa(netto, rabat=rabat, vat=5):.2f}")
