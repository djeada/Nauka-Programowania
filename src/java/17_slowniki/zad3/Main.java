/*
ZAD-03 — Biblioteka: baza wypożyczeń

**Poziom:** ★☆☆
**Tagi:** `dict`, `list`, `pętle`, `string`

### Treść

Utrzymuj słownik: `imię -> lista wypożyczonych książek`.
Obsługuj komendy (każda w osobnej linii) aż do `koniec`:

* `dodaj [imię] [tytuł]`
* `zwróć [imię] [tytuł]`
* `lista [imię]`

Po `lista [imię]` wypisz:

* jeśli lista niepusta: `Książki wypożyczone przez [imię]: t1, t2, ...`
* jeśli brak książek (lub brak czytelnika): `Książki wypożyczone przez [imię]: brak`

### Wejście

Wiele linii z komendami, koniec po słowie `koniec`.

### Wyjście

Tylko po komendach `lista ...`.

### Przykład

**Wejście:**

```
dodaj Jan Hobbit
dodaj Anna "Duma i uprzedzenie"
dodaj Jan "Władca Pierścieni"
lista Jan
zwróć Jan Hobbit
lista Jan
lista Anna
koniec
```

**Wyjście:**

```
Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
Książki wypożyczone przez Jan: Władca Pierścieni
Książki wypożyczone przez Anna: Duma i uprzedzenie
```

*/
import java.util.*;

public class Main {
  // Zbuduj prosta baze danych dla biblioteki oparta o slownik w ktorym kluczami
  // sa imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek.
  // Baza danych powinna umozliwiac:
  // a) dodanie wypozyczonej ksiazki do danego czytelnika;
  
  // Zlozonosc Czasowa: O(1) - srednia dla HashMap
  // Zlozonosc Pamieciowa: O(1)
  public static void dodajKsiazke(
      HashMap<String, ArrayList<String>> lista, final String uzytkownik, final String ksiazka) {
    if (lista.containsKey(uzytkownik)) {
      ArrayList<String> ksiazki = lista.get(uzytkownik);

      if (!ksiazki.contains(ksiazka)) {
        ksiazki.add(ksiazka);
        lista.put(uzytkownik, ksiazki);
      } else {
        System.out.println("Uzytkownik juz wypozyczyl ta ksiazke.");
      }
    } else {
      ArrayList<String> ksiazki = new ArrayList<String>(Arrays.asList(ksiazka));
      lista.put(uzytkownik, ksiazki);
    }
  }

  // b) usuniecie wypozyczonej ksiazki z listy odpowiadajacej czytelnikowi;
  public static void usunKsiazke(
      HashMap<String, ArrayList<String>> lista, final String uzytkownik, final String ksiazka) {

    if (!lista.containsKey(uzytkownik)) {
      System.out.println("Podany uzytkownik nie znajduje sie w liscie.");
      return;
    }

    ArrayList<String> ksiazki = lista.get(uzytkownik);

    if (ksiazki.contains(ksiazka)) {
      while (ksiazki.remove(ksiazka)) {}
      lista.put(uzytkownik, ksiazki);
    } else {
      System.out.println("Uzytkownik nie wypozyczyl tej ksiazki.");
    }
  }

  // c) wyswietlenie aktualnej listy ksiazek dla konkretnego czytelnika oraz
  // dla wszystkich czytelnikow;
  public static void wyswietlKsiazki(
      HashMap<String, ArrayList<String>> lista, final String uzytkownik) {

    if (!lista.containsKey(uzytkownik)) {
      System.out.println("Podany uzytkownik nie znajduje sie w liscie.");
      return;
    }

    System.out.print("Uzytkownik ");
    System.out.print(uzytkownik);
    System.out.println(" wypozyczyl nastepujace ksiazki: ");

    for (var ksiazka : lista.get(uzytkownik)) {
      System.out.println(ksiazka);
    }
  }

  public static void wyswietlWszystkieKsiazki(HashMap<String, ArrayList<String>> lista) {

    for (String klucz : lista.keySet()) {
      wyswietlKsiazki(lista, klucz);
      System.out.print("\n");
    }
  }

  public static void main(String[] args) {

    HashMap<String, ArrayList<String>> lista = new HashMap<String, ArrayList<String>>();

    dodajKsiazke(lista, "Pan T", "Duma i uprzedzenie – Jane Austen");
    dodajKsiazke(lista, "Pan T", "Zabic drozdad – Harper Lee");
    dodajKsiazke(lista, "Pan T", "Biblia");
    dodajKsiazke(lista, "Pan T", "Buszujacy w zbozu – JD Salinger");
    dodajKsiazke(lista, "Pan T", "Rok 1984 – George Orwell");
    dodajKsiazke(lista, "Pan T", "Wedy");

    dodajKsiazke(lista, "Elzbieta", "Wielkie nadzieje – Charles Dickens");
    dodajKsiazke(lista, "Elzbieta", "Hobbit – JRR Tolkien");
    dodajKsiazke(lista, "Elzbieta", "Harry Potter – JK Rowling");

    wyswietlWszystkieKsiazki(lista);

    usunKsiazke(lista, "Elzbieta", "Hobbit – JRR Tolkien");
    usunKsiazke(lista, "Pan T", "Zabic drozdad – Harper Lee");
    usunKsiazke(lista, "Pan T", "Rok 1984 – George Orwell");

    wyswietlWszystkieKsiazki(lista);
  }
}

