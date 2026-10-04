r"""
ZAD-09 — Rozdziel informacje o pracowniku

**Poziom:** ★☆☆
**Tagi:** `napisy`, `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika: imię, nazwisko, miejsce urodzenia, zawód i zarobki — w tej kolejności, oddzielone średnikami `;`.
Wypisz każdą informację w osobnej linii, poprzedzoną etykietą.

### Wejście

* 1. linia: dane w formacie `Imię; Nazwisko; Miejsce urodzenia; Zawód; Zarobki;`
  * przed średnikiem i po nim mogą (ale nie muszą) stać spacje,
  * linia zawsze kończy się średnikiem,
  * pojedyncze pole może zawierać spacje (np. `Nowy Sącz`).

### Wyjście

Pięć linii w formacie:

```
Imię: …
Nazwisko: …
Miejsce urodzenia: …
Zawód: …
Zarobki: …
```

Wartości wypisz bez spacji na początku i na końcu.

### Przykład

**Wejście:**

```
Jan; Kowalski; Warszawa; Programista; 1000;
```

**Wyjście:**

```
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Warszawa
Zawód: Programista
Zarobki: 1000
```

### Uwagi

* Po `split(";")` usuń spacje z brzegów każdego pola metodą `strip()`.
* Końcowy średnik daje na końcu listy pusty element — pomiń go.

"""

ETYKIETY = ["Imię", "Nazwisko", "Miejsce urodzenia", "Zawód", "Zarobki"]


def rozdziel_informacje(linia):
    pola = []
    for pole in linia.split(";"):
        pole = pole.strip()
        if pole:
            pola.append(pole)
    return pola


if __name__ == "__main__":
    linia = input()
    informacje = rozdziel_informacje(linia)
    for etykieta, wartosc in zip(ETYKIETY, informacje):
        print(f"{etykieta}: {wartosc}")
