"""
ZAD-05 — Pracownik z największym sumarycznym zyskiem

**Poziom:** ★☆☆
**Tagi:** `dict`, `sumowanie`

### Treść

Wczytaj `n` wpisów: `pracownik zysk`. Zsumuj zyski per pracownik i wypisz nazwę pracownika z największą sumą.
(Jeśli remis, wybierz tego, który pierwszy osiągnął tę maksymalną sumę podczas przetwarzania.)

### Wejście

* 1 linia: `n`
* następnie `n` linii: `imie_i_nazwisko zysk`

### Wyjście

* Jedna linia: `imie_i_nazwisko`

### Przykład

**Wejście:**

```
5
Barnaba_Barabash 120
Jon_Snow 100
Kira_Summer 300
Barnaba_Barabash 200
Bob_Marley 110
```

**Wyjście:**

```
Barnaba_Barabash
```

"""


def pracownik_z_najwiekszym_zyskiem(lista_par):
    """
    Funkcja zwraca napis reprezentujacy imie i nazwisko pracownika, ktory
    przyniosl firmie najwiecej zysku.
    """

    zyski = {}
    for para in lista_par:
        if para[0] in zyski:
            zyski[para[0]] += para[1]
        else:
            zyski[para[0]] = para[1]

    return max(zyski, key=zyski.get)


def test_pracownik_z_najwiekszym_zyskiem():

    assert (
        pracownik_z_najwiekszym_zyskiem(
            [
                ("Barnaba Barabash", 120),
                ("Jon Snow", 100),
                ("Kira Summer", 300),
                ("Barnaba Barabash", 200),
                ("Bob Marley", 110),
            ]
        )
        == "Barnaba Barabash"
    )


if __name__ == "__main__":

    test_pracownik_z_najwiekszym_zyskiem()
