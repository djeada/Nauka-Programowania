/*
Tytul: Suma elementow ciagu.
Tresc: Dla otrzymanej liczby naturalnej n, wypisz sume n pierwszych elementow ciagu danego wzorem:
$$a_n = n^2 + n + 1$$
$$a_n = n^2 + 5n$$
$$a_n = n + 2n$$
Wynik powinien zostac zaokraglony do najblizszej liczby naturalnej.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
* Dla otrzymanej liczby 2, w podpunkcie a) powinna zostac wypisana liczba 1.
* Dla otrzymanej liczby 2, w podpunkcie b) powinna zostac wypisana liczba 17.
* Dla otrzymanej liczby 2, w podpunkcie c) powinna zostac wypisana liczba 6.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby n, wyswietl sume n
    // pierwszych wyrazow ciagu danego wzorem:
    System.out.print("Podaj liczbe: \n");
    Scanner s = new Scanner(System.in);
    int n = Integer.parseInt(s.nextLine());

    // a_n = n/(n+1)
    float suma = (float) 0.0;
    for (float i = 1; i <= n; i++) {
      float a = i / (i + 1);
      suma += a;
    }
    System.out.printf("%.2f", suma);
    System.out.printf("\n");

    // a_n = (n^2+5)/n
    suma = (float) 0.0;
    for (float i = 1; i <= n; i++) {
      float a = (float) ((Math.pow(i, 2) + 5) / i);
      suma += a;
    }
    System.out.printf("%.2f", suma);
    System.out.printf("\n");

    // a_n = n + 2^n
    suma = (float) 0.0;
    for (int i = 1; i <= n; i++) {
      int a = (int) (i + Math.pow(2, i));
      suma += a;
    }

    System.out.printf("%.2f", suma);
    System.out.printf("\n");
  }
}

