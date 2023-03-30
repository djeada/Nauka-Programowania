/*
Tytul: Liczba cyfr.
Tresc: Dla otrzymanej od uzytkownika liczby naturalnej wypisz liczbe cyfr, z ktorych sie sklada.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby 342, powinna zostac wypisana liczba 3.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {
    // Dla pobranej od uzytkownika liczby,
    // zwroc liczbe cyfr pobranje liczby.

    System.out.print("Podaj liczbe\n");

    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    int licznik = 0;

    while (a > 0) {
      a = a / 10;
      licznik++;
    }

    System.out.print("Podana liczba sklada sie z " + licznik + " cyfr.\n");
  }
}

