/*
Tytul: Obliczanie wynikow operacji arytmetycznych.
Tresc zadania: Napisz program, ktory pobierze od uzytkownika dwie liczby naturalne i wypisze wyniki nastepujacych operacji arytmetycznych:
a) suma tych liczb
b) roznica pierwszej i drugiej liczby
c) iloczyn tych liczb
d) iloraz pierwszej liczby przez druga
e) reszta z dzielenia pierwszej liczby przez druga
f) pierwsza liczba podniesiona do potegi rownej drugiej liczbie
Dane wejsciowe: Dwie liczby naturalne dla wszystkich podpunktow.
Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
Przyklad:
* Jesli uzytkownik poda liczby 9 oraz 1, program powinien wypisac liczby: 10, 1, 9, 9, 0, 9.
* Jesli uzytkownik poda liczby 3 oraz 2, program powinien wypisac liczby: 5, 1, 6, 1, 1, 9.

*/
import java.util.*;

public class Main {

  public static void main(String[] args) {

    int x;
    int y;
    Scanner s = new Scanner(System.in);

    System.out.print("Podaj dwie liczby: \n");

    x = Integer.parseInt(s.nextLine());
    y = Integer.parseInt(s.nextLine());

    System.out.print("Suma " + x + " oraz " + y + " wynosi " + (x + y) + "\n");
    System.out.print("Roznica " + x + " i " + y + " wynosi " + (x - y) + "\n");
    System.out.print("Iloczyn " + x + " i " + y + " wynosi " + (x * y) + "\n");
    System.out.print("Iloraz " + x + " przez " + y + " wynosi " + (x / y) + "\n");
    System.out.print("Reszta z dzielenia " + x + " przez " + y + " wynosi " + (x % y) + "\n");
    System.out.print(x + " podniesione do " + y + " wynosi " + Math.pow(x, y) + "\n");
  }
}

