/*
Tytul: Liczba pi.
Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi tyle razy, ile wynosi ta liczba, z dokladnoscia do tylu miejsc po przecinku, ile wynosi otrzymana liczba.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby 2, powinno zostac wypisane:
3,14
3,14

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, wyswietl liczbe Pi tyle razy
    // ile wynosi pobrana liczba, z dokladnoscia do tylu
    // miejsc po przescinku ile wynosi pobrana liczba.

    System.out.print("Podaj liczbe: \n");
    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    for (int i = 0; i < n; i++) {
      System.out.printf("%f", 3.14);
      System.out.printf("%f", " ");
    }
  }
}

