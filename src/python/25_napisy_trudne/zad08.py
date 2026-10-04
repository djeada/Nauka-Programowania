r"""
ZAD-08 — Najdłuższy wspólny przedrostek

**Poziom:** ★★★
**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz `n` napisów. Znajdź ich **najdłuższy wspólny przedrostek**, czyli najdłuższy napis, od którego zaczynają się wszystkie podane napisy. Jeśli napisy nie mają wspólnego przedrostka (np. zaczynają się od różnych liter), wynikiem jest napis pusty — wypisz wtedy pustą linię.

### Wejście

* 1. linia: `n` — liczba napisów
* kolejne `n` linii: napisy (każdy w osobnej linii)

### Wyjście

Jedna linia: najdłuższy wspólny przedrostek (albo pusta linia).

### Ograniczenia

* `1 ≤ n ≤ 100`
* każdy napis ma od 1 do 100 znaków

### Przykład

**Wejście:**

```
3
Remolada
Remux
Remmy
```

**Wyjście:**

```
Rem
```

### Uwagi

* Przy jednym napisie wynikiem jest cały ten napis.
* Wygodnie jest zacząć od pierwszego napisu jako kandydata i skracać go, porównując po kolei z każdym kolejnym napisem.

"""


def najdluzszy_wspolny_przedrostek(napisy):
    """Zwraca najdłuższy przedrostek wspólny dla wszystkich napisów."""
    przedrostek = napisy[0]

    for napis in napisy[1:]:
        dlugosc = 0
        while (
            dlugosc < len(przedrostek)
            and dlugosc < len(napis)
            and przedrostek[dlugosc] == napis[dlugosc]
        ):
            dlugosc += 1
        przedrostek = przedrostek[:dlugosc]

    return przedrostek


if __name__ == "__main__":
    n = int(input())
    napisy = [input() for _ in range(n)]
    print(najdluzszy_wspolny_przedrostek(napisy))
