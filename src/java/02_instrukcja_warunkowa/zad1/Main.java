/*
Tytul: Porownanie ze stala.
Tresc: Pobierz od uzytkownika liczbe naturalna. Jesli ta liczba jest wieksza niz 5, wypisz ja.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna lub brak danych wyjsciowych.
Przyklad:
Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Wypisz pobrana od uzytkownika liczbe, jesli jest wieksza od 5.

    System.out.print("podaj liczbe:\n");

    Scanner s = new Scanner(System.in);
    int x = Integer.parseInt(s.nextLine());

    if (x > 5) {
      System.out.print(x);
      System.out.print("\n");
    }
  }
}

