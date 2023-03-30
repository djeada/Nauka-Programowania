/*
Tytul: Liczby spelniajace okreslone warunki.
Tresc: Dla pobranej liczby naturalnej wypisz:
a) wszystkie liczby naturalne mniejsze od pobranej, ktorych suma cyfr jest rowna 10,
b) wszystkie liczby naturalne dwucyfrowe wieksze od pobranej,
c) wszystkie liczby naturalne trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie,
d) wszystkie liczby naturalne trzycyfrowe podzielne przez sume cyfr pobranej liczby,
e) wszystkie liczby naturalne mniejsze od pobranej, skladajace sie wylacznie z parzystych cyfr.
Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.
Dane wyjsciowe: Kilka liczb naturalnych.
Przyklady
Dla pobranej liczby: 95:
a) wszystkie liczby naturalne mniejsze od pobranej, ktorych suma cyfr jest rowna 10: brak
b) wszystkie liczby naturalne dwucyfrowe wieksze od pobranej: 96, 97, 98, 99
c) wszystkie liczby naturalne trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie: brak
d) wszystkie liczby naturalne trzycyfrowe podzielne przez sume cyfr pobranej liczby: brak
e) wszystkie liczby naturalne mniejsze od pobranej, skladajace sie wylacznie z parzystych cyfr: 2, 4

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby n, wyswietl sume n
    // pierwszych wyrazow ciagu danego wzorem:
    System.out.print("Podaj liczbe\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    // a) mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10

    System.out.print("mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: \n");
    for (int i = 0; i < a; i++) {
      int pom = i;
      int suma = 0;

      while (pom > 0) {
        suma += (pom % 10);
        pom /= 10;
      }

      if (suma == 10) {
        System.out.print(i);
        System.out.print("\n");
      }
    }

    // b) dwucyfrowe mniejsze od pobranej liczby

    System.out.print("dwucyfrowe mniejsze od pobranej liczby: \n");
    for (int i = 10; i < 100 && i < a; i++) {
      System.out.print(i);
      System.out.print("\n");
    }

    // c) trzycyfrowe ktorych suma cyfr jest	rowna pobranej liczbie
    System.out.print("trzycyfrowe ktorych suma cyfr jest rowna pobranej liczbie\n");
    for (int i = 100; i < 1000; i++) {
      int pom = i;
      int suma = 0;

      while (pom > 0) {
        suma += (pom % 10);
        pom /= 10;
      }

      if (suma == a) {
        System.out.print(i);
        System.out.print("\n");
      }
    }

    // d) trzycyfrowe podzielne przez sume cyfr pobranej liczby
    System.out.print("trzycyfrowe podzielne przez sume cyfr pobranej liczby\n");

    int pom = a;
    int suma = 0;

    while (pom > 0) {
      suma += (pom % 10);
      pom /= 10;
    }

    for (int i = 100; i < 1000; i++) {

      if (i % suma == 0) {
        System.out.print(i);
        System.out.print("\n");
      }
    }

    // e) mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr
    System.out.print("mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr\n");

    for (int i = 0; i < a; i++) {
      pom = i;
      boolean flaga = true;
      while (pom > 0) {
        int cyfra = pom % 10;
        if (cyfra % 2 == 1) {
          flaga = false;
          break;
        }
        pom /= 10;
      }

      if (flaga) {
        System.out.print(i);
        System.out.print("\n");
      }
    }
  }
}

