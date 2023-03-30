/*
Tytul: Klucz to imie, wartosc lista wypozyczonych ksiazek.
Tresc: Zbuduj prosta baze danych dla biblioteki oparta o slownik, w ktorym kluczami sa imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek. Baza danych powinna umozliwiac:
1. Dodanie wypozyczonej ksiazki do danego czytelnika.
2. Zwrocenie wypozyczonej ksiazki przez czytelnika.
3. Wypisanie aktualnej listy wypozyczonych ksiazek dla danego czytelnika.

*/
import java.util.*;

public class Main {

  public static List<String> sortujWzgledemKluczyV1(Map<String, Integer> slownik) {

    List<String> lista = new ArrayList<String>();

    for (String key : slownik.keySet()) lista.add(key);

    Collections.sort(lista);

    return lista;
  }

  public static List<Integer> sortujWzgledemWartosciV1(Map<String, Integer> slownik) {

    List<Integer> lista = new ArrayList<Integer>();

    for (String key : slownik.keySet()) lista.add(slownik.get(key));

    Collections.sort(lista);

    return lista;
  }

  private static void test1() {
    Map<String, Integer> slownik =
        new HashMap<String, Integer>() {
          {
            put("c", 3);
            put("x", 5);
            put("a", -2);
            put("b", 4);
          }
        };

    List<Integer> wynik = Arrays.asList(-2, 3, 4, 5);

    assert sortujWzgledemWartosciV1(slownik).equals(wynik);
  }

  private static void test2() {
    Map<String, Integer> slownik =
        new HashMap<String, Integer>() {
          {
            put("c", 3);
            put("x", 5);
            put("a", -2);
            put("b", 4);
          }
        };

    List<Integer> wynik = Arrays.asList(-2, 3, 4, 5);

    assert sortujWzgledemWartosciV1(slownik).equals(wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

