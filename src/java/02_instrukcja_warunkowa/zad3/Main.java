/*
Tytul: Znak liczby.
Tresc: Pobierz liczbe naturalna od uzytkownika i sprawdz, czy liczba jest ujemna, dodatnia, czy jest zerem. Wypisz odpowiedni komunikat.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla pobranej liczby: 2, powinien zostac wypisany komunikat, ze liczba jest dodatnia.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest zerem.

    System.out.print("podaj liczbe:\n");

    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    if (a < 0) {
      System.out.print("liczba jest ujemna\n");
    } else if (a > 0) {
      System.out.print("liczba jest dodatnia\n");
    } else {
      System.out.print("liczba jest zerem\n");
    }
  }
}

