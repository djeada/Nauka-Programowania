/*
Tytul: Suma liczb naturalnych mniejszych od N.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz sume liczb naturalnych mniejszych od N.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 10, powinna zostac zwrocona liczba: 55.

*/
import java.util.*;

public class Main {
  private static class Pair<T1, T2> {
    public T1 first;
    public T2 second;

    public Pair(T1 firstValue, T2 secondValue) {
      first = firstValue;
      second = secondValue;
    }

    @Override
    public boolean equals(Object o) {
      return (o instanceof Pair)
          && (this.first == ((Pair) o).first)
          && (this.second == ((Pair) o).second);
    }
  }

  public static void oblicz(int n, Pair<Integer, Integer> wyniki) {
    oblicz(n, wyniki, "AB");
  }

  private static String swapChars(String slowa, int i, int j) {
    StringBuilder sb = new StringBuilder(slowa);
    char l = sb.charAt(i), r = sb.charAt(j);
    sb.setCharAt(i, r);
    sb.setCharAt(j, l);
    return sb.toString();
  }

  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n) - rekurencja uzywa stosu
  public static void oblicz(int n, Pair<Integer, Integer> wyniki, String s) {

    if (n <= 0) {
      return;
    }

    if (n == 1 || n == 2 || n == 4) {

      if (s.charAt(0) == 'A') {
        wyniki.first += 1;
      } else {
        wyniki.second += 1;
      }

      return;
    } else {
      s = swapChars(s, 0, 1);

      oblicz(n - 1, wyniki, s);
      oblicz(n - 2, wyniki, s);
      oblicz(n - 4, wyniki, s);
    }
  }

  public static void test1() {

    Pair<Integer, Integer> wyniki = new Pair<Integer, Integer>(0, 0);

    oblicz(1, wyniki);
    assert wyniki.first == 1;
    assert wyniki.second == 0;
  }

  public static void test2() {

    Pair<Integer, Integer> wyniki = new Pair<Integer, Integer>(0, 0);

    oblicz(3, wyniki);
    assert wyniki.first == 0;
    assert wyniki.second == 2;
  }

  public static void test3() {

    Pair<Integer, Integer> wyniki = new Pair<Integer, Integer>(0, 0);

    oblicz(10, wyniki);
    assert wyniki.first == 33;
    assert wyniki.second == 27;
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

