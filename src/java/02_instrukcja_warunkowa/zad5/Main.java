/*
Tytul: Posortowanie trzech liczb.
Tresc: Pobierz od uzytkownika trzy liczby naturalne i wypisz je w kolejnosci rosnacej.
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Trzy liczby naturalne.
Przyklad:
Dla pobranych liczb: 2, 1 oraz 4, powinny zostac wypisane liczby: 1, 2 i 4.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranych trzech liczb, wypisz je w kolejnosci rosnacej.

    System.out.print("podaj trzy liczby:");
    System.out.print("\n");

    int a;
    int b;
    int c;
    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());
    c = Integer.parseInt(s.nextLine());

    if (a >= b && a >= c) {
      if (b >= c) {
        System.out.print(c + "\n");
        System.out.print(b + "\n");
        System.out.print(a + "\n");
        System.out.print("\n");
      } else {
        System.out.print(b + "\n");
        System.out.print(c + "\n");
        System.out.print(a + "\n");
        System.out.print("\n");
      }
    } else if (c >= b && c >= a) {
      if (a >= b) {
        System.out.print(b + "\n");
        System.out.print(a + "\n");
        System.out.print(c + "\n");
        System.out.print("\n");
      } else {
        System.out.print(a + "\n");
        System.out.print(b + "\n");
        System.out.print(c + "\n");
        System.out.print("\n");
      }
    } else {
      if (a >= c) {
        System.out.print(c + "\n");
        System.out.print(a + "\n");
        System.out.print(b + "\n");
        System.out.print("\n");
      } else {
        System.out.print(a + "\n");
        System.out.print(c + "\n");
        System.out.print(b + "\n");
        System.out.print("\n");
      }
    }
  }
}

