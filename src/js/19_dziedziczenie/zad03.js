/*
ZAD-03 — Polimorfizm: Zwierz, Pies i Kot

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `override`

### Treść

Zaprojektuj klasy:

* **Zwierz** — metoda `odglos()` zwraca/drukuje ogólny dźwięk.
* **Pies** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.
* **Kot** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.

Program testowy:

* tworzy obiekty: `Zwierz`, `Pies`, `Kot`,
* umieszcza je w jednej kolekcji,
* iteruje i dla każdego wypisuje linię w formacie:
  `NazwaKlasy wydaje odgłos: ...`

### Wejście

Brak.

### Wyjście

Trzy linie, po jednej dla każdego obiektu.

### Przykład

**Wyjście:**

```
Zwierz wydaje odgłos: ...
Pies wydaje odgłos: Hau!
Kot wydaje odgłos: Miau!
```

*/
/*
Tytul: Polimorfizm. 

Tresc: Zaprojektuj klase Zwierz oraz klasy potomne Pies i Kot. Obie klasy potomne powinny nadpisywac metode 'odglos()' zdefiniowana w klasie bazowej. Napisz program testujacy te klasy, w ktorym umiescisz obiekty wszystkich trzech klas w jednej liscie i przejdziesz przez wszystkie elementy tej listy, wywolujac dla kazdego z nich funkcje 'odglos()'."
*/ // Klasa Zwierz (klasa bazowa)
class Zwierz {
  odglos() {
    console.log("Nieznany dzwiek");
  }
}

// Klasy potomne Pies i Kot
class Pies extends Zwierz {
  odglos() {
    console.log("Hau!");
  }
}

class Kot extends Zwierz {
  odglos() {
    console.log("Miau!");
  }
}

// Tworzymy liste obiektow klas Pies i Kot
const listaZwierzat = [new Pies(), new Kot(), new Pies(), new Kot()];

// Wywolujemy metode odglos() dla kazdego obiektu w liscie
listaZwierzat.forEach((zwierze) => {
  zwierze.odglos();
});

