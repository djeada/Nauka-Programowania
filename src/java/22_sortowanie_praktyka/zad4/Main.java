/*
Tytul: Sortowanie napisow w liscie wzgledem dlugosci.
Tresc: Masz dana liste napisow. Posortuj napisy w liscie wzgledem dlugosci.
Dane wejsciowe: Lista napisow.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla listy ["abcd", "ab", "a", "abc"] powinno zostac zwrocone ["a", "ab", "abc", "abcd"].

*/
import java.util.*;

public class Main {

  public static void sortujWzgledemDlugosci(ArrayList<String> lista) {
    Collections.sort(
        lista,
        new Comparator<String>() {
          @Override
          public int compare(final String o1, final String o2) {
            return o1.length() - o2.length();
          }
        });
  }

  public static void test1() {
    ArrayList<String> lista = new ArrayList<String>(Arrays.asList("abcd", "ab", "a", "abc"));
    ArrayList<String> oczekiwane = new ArrayList<String>(Arrays.asList("a", "ab", "abc", "abcd"));

    sortujWzgledemDlugosci(lista);

    assert lista.equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
  }
}

