/*
Tytul: Maksimum i minimum z dwoch liczb.
Tresc: Pobierz od uzytkownika dwie liczby naturalne i wypisz najpierw wieksza, a potem mniejsza.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla pobranych liczb: 1 oraz 4, powinny zostac wypisane liczby: 4 i 1.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.

    System.out.print("podaj dwie liczby:\n");

    int a;
    int b;
    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());

    if (a > b) {
      System.out.print(a + "\n");
      System.out.print(b + "\n");
      System.out.print("pierwsza liczba jest wieksza od drugiej\n");

    } else {
      System.out.print(b + "\n");
      System.out.print(a + "\n");
      System.out.print("pierwsza liczba nie jest wieksza od drugiej\n");
    }
  }
}

