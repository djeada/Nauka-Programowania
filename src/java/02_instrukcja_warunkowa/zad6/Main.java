/*
Tytul: Maks z czterech liczb.
Tresc: Dla czterech pobranych liczb naturalnych, wypisz najwieksza z nich.
Dane wejsciowe: Cztery liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla pobranych liczb: 2, 5, 1 i 4, powinna zostac wypisana liczba: 5.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranych czterech liczb, znajdz najwieksza liczbe.

    System.out.print("podaj cztery liczby:");
    System.out.print("\n");

    int a;
    int b;
    int c;
    int d;

    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());
    c = Integer.parseInt(s.nextLine());
    d = Integer.parseInt(s.nextLine());

    int maksAB = a > b ? a : b;
    int maksCD = c > d ? c : d;
    int maks = maksAB > maksCD ? maksAB : maksCD;

    System.out.print(maks);
    System.out.print("\n");
  }
}

