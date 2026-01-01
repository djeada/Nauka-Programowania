/*
ZAD-09 — Rozdziel informacje o pracowniku

**Poziom:** ★☆☆
**Tagi:** `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika rozdzielonymi średnikami `;`:

1. Imię, 2) Nazwisko, 3) Miejsce urodzenia, 4) Stanowisko, 5) Zarobki

Wypisz każdą informację w osobnej linii z etykietą.

### Wejście

* 1. linia: dane w formacie `Imię; Nazwisko; Miasto; Zawód; Zarobki;`

### Wyjście

Pięć linii w formacie:

* `Imię: ...`
* `Nazwisko: ...`
* `Miejsce urodzenia: ...`
* `Zawód: ...`
* `Zarobki: ...`

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

* Po `split(';')` usuń ewentualne spacje z brzegów pól (np. `strip()`).
* Ostatni średnik może powodować pusty element na końcu — zignoruj go.

*/
import java.util.*;

public class Main {
  // Otrzymujesz rekord z bazy danych reprezentujacy dane pracownika.
  // Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki.
  // Informacje rozdzielone sa srednikami. Zapisz je w osobnych zmiennych
  // i wypisz wraz z komunikatem.

  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n)
  public static void wypiszDane(String napis) {

    ArrayList<String> wynik = new ArrayList<String>();
    // Podziel po srednikach i usun puste elementy
    for (String pole : napis.split(";")) {
      String trimmed = pole.trim();
      if (!trimmed.isEmpty()) {
        wynik.add(trimmed);
      }
    }
    
    assert wynik.size() == 5;

    System.out.print("Imie: " + wynik.get(0) + "\n");
    System.out.print("Nazwisko: " + wynik.get(1) + "\n");
    System.out.print("Miejsce urodzenia: " + wynik.get(2) + "\n");
    System.out.print("Zawod: " + wynik.get(3) + "\n");
    System.out.print("Zarobki: " + wynik.get(4) + "\n");
  }

  public static void main(String[] args) {
    String napis = "Jan; Kowalski; Warszawa; Programista; 1000";
    wypiszDane(napis);
  }
}

