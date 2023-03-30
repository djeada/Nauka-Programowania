/*
Tytul: Zamiana kolejnosci liczb.
Tresc zadania: Napisz program, ktory pobierze od uzytkownika dwie liczby naturalne i wypisze je w odwroconej kolejnosci.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Jesli uzytkownik poda liczby -7 oraz 4, program powinien wypisac liczby: 4 i -7.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    int a;
    int b;

    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());

    System.out.print(b);
    System.out.print("\n");
    System.out.print(a);
    System.out.print("\n");
  }
}

