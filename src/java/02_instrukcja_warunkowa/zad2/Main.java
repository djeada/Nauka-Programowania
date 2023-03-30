/*
Tytul: Porownanie ze zmienna.
Tresc: Pobierz od uzytkownika dwie liczby naturalne i sprawdz, czy sa one identyczne. Wypisz odpowiedni komunikat.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla pobranych liczb: 7 i 4, powinien zostac wypisany komunikat, ze liczby sa rozne.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla dwoch pobranych liczb, sprawdz czy pobrane liczby sa identyczne.

    System.out.print("podaj dwie liczby:\n");
    int a;
    int b;
    Scanner s = new Scanner(System.in);

    a = Integer.parseInt(s.nextLine());
    b = Integer.parseInt(s.nextLine());

    if (a == b) {
      System.out.print("liczby sa jednakowe\n");
    } else {
      System.out.print("liczby sa rozne\n");
    }
  }
}

