/*
Tytul: Cyfry liczby.
Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry, z ktorych sie sklada, zaczynajac od cyfry jednosci.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczby.
Przyklad:
Dla otrzymanej liczby 8214, powinny zostac wypisane cyfry 4, 1, 2 i 8.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, powinny zostac zwrocone
    // cyfry pobranej liczby poczynajac od cyfry jednosci.

    System.out.print("Podaj liczbe\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    while (a > 0) {
      System.out.print(a % 10);
      System.out.print("\n");
      a = a / 10;
    }
  }
}

