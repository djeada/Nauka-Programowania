/*
Tytul: Obliczenie iloczynu wielomianu przez skalar.
Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe x. Oblicz wspolczynniki wielomianu, ktory jest wynikiem pomnozenia otrzymanego wielomianu przez liczbe x.
Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.
Dane wyjsciowe: Lista liczb naturalnych.
Przyklad:
Dla listy wspolczynnikow [4, -3, 2] i liczby x = -2, zostanie zwrocona lista [-8, 6, -4].

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste n wspolczynnikow wielomianu postaci
  // a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe x.
  // Oblicz wartosc wspolczynnikow wielomianu po
  // przemnozeniu przez liczbe x.
  public static ArrayList<Integer> iloczyn(ArrayList<Integer> lista, int x) {

    ArrayList<Integer> wynik = new ArrayList<Integer>();

    for (var liczba : lista) {
      wynik.add(liczba * x);
    }

    return new ArrayList<Integer>(wynik);
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 2, 1));
    int x = 2;
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 4, 2));
    assert wynik.equals(iloczyn(lista, x));
  }

  public static void main(String[] args) {

    test1();
  }
}

