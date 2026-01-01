/*
ZAD-07 — Weryfikacja nazwy użytkownika i hasła

**Poziom:** ★★☆
**Tagi:** `funkcje`, `while`, `string`, `porównania`

### Treść

Napisz dwie funkcje:

1. `pobierz_dane()` — pobiera od użytkownika nazwę użytkownika i hasło i zwraca je (np. jako parę).
2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje login i hasło aż będą identyczne z przekazanymi. Po poprawnym wczytaniu wypisuje:
   `Dane poprawne. Dostęp przyznany.`

### Wejście

* `pobierz_dane()` wczytuje dwie linie:

  1. login
  2. hasło
* `sprawdz_dane(...)` wczytuje kolejne pary (login, hasło), po dwie linie na próbę.

### Wyjście

Jedna linia (tylko raz, po poprawnym dopasowaniu):

* `Dane poprawne. Dostęp przyznany.`

### Ograniczenia / gwarancje

* W pewnym momencie użytkownik poda poprawne dane.

### Uwagi o formatowaniu

* **Nie wypisuj promptów** typu „Podaj nazwę użytkownika:”.
* Porównanie jest czułe na wielkość liter.

*/
import java.util.*;

public class Main {
  // Napisz dwie funkcje. Pierwsza powinna porsic uzytkownika o podanie
  // nazwy i hasla oraz zwracac otrzymane dane.

  public static String[] pobierzDane() {
    Scanner s = new Scanner(System.in);
    String login = s.nextLine();
    String haslo = s.nextLine();
    return new String[] {login, haslo};
  }

  public static void sprawdzDane(String poprawnyLogin, String poprawneHaslo) {
    Scanner s = new Scanner(System.in);
    
    while (true) {
      String login = s.nextLine();
      String haslo = s.nextLine();
      
      if (login.equals(poprawnyLogin) && haslo.equals(poprawneHaslo)) {
        System.out.println("Dane poprawne. Dostęp przyznany.");
        break;
      }
    }
  }

  public static void main(String[] args) {
    String[] dane = pobierzDane();
    sprawdzDane(dane[0], dane[1]);
  }
}

