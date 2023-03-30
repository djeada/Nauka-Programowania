/*
Tytul: Cyfry liczby spelniajace okreslone warunki.
Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry tej liczby, ktore sa:
a) liczbami parzystymi,
b) mniejsze niz 5,
c) rozne od 0.
Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.
Dane wyjsciowe: Kilka liczb.
Przyklad:
a) Dla otrzymanej liczby 932, powinna zostac wypisana liczba 2.
b) Dla otrzymanej liczby 101, powinny zostac wypisane liczby 1, 0 i 1.
c) Dla otrzymanej liczby 650, powinny zostac wypisane liczby 6 i 5.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, powinny zostac zwrocone cyfry
    // liczby spelniajce nastepujacy warunek:

    System.out.print("Podaj liczbe\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    // a) Liczby parzyste;

    int pom = a;
    System.out.print("Cyfry liczby badace liczbami parzystymi: \n");

    while (pom > 0) {
      int cyfra = pom % 10;

      if (cyfra % 2 == 0) {
        System.out.print(cyfra + "\n");
      }

      pom /= 10;
    }

    // b) Mniejsze niz 5;

    pom = a;
    System.out.print("Cyfry liczby mniejsze niz 5: \n");

    while (pom > 0) {
      int cyfra = pom % 10;

      if (cyfra < 5) {
        System.out.print(cyfra + "\n");
      }

      pom /= 10;
    }

    // c) Rozne od 0;

    pom = a;
    System.out.print("Cyfry liczby rozne od 0: \n");

    while (pom > 0) {
      int cyfra = pom % 10;

      if (cyfra != 0) {
        System.out.print(cyfra + "\n");
      }

      pom /= 10;
    }
  }
}

