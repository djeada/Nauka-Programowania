/*
Tytul: Czy slowniki sa identyczne?
Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych. Listy sa nieuporzadkowane. Twoim zadaniem jest sprawdzenie, czy slowniki skladaja sie z tych samych par. Dwie listy uznajemy za identyczne, jesli zawieraja te same elementy, niezaleznie od kolejnosci, w jakiej sie one znajduja.
Dane wejsciowe: Dwa slowniki par: napis, lista liczb calkowitych.
Dane wyjsciowe: Wartosc boolowska.
Przyklad:
Dla otrzymanych slownikow:
{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4]}
Powinna zostac zwrocona wartosc logiczna: Prawda.
Dla otrzymanych slownikow:
{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4], 'c': [6, 7]}
Powinna zostac zwrocona wartosc logiczna: Falsz.

*/
package test;

import java.util.*;
import java.util.stream.Collectors;

public class Main {

  public static ArrayList<Character> policzPowtarzajaceSieZnakiV1(String slowo) {

    ArrayList<Character> listaZnakow = new ArrayList<Character>();

    if (slowo != null) {
      Map<Character, Integer> histo = new HashMap<>();

      for (char ch : slowo.toCharArray()) {

        histo.compute(ch, (k, v) -> (v == null) ? 1 : ++v);

        if (histo.get(ch) > 1 && !listaZnakow.contains(ch)) listaZnakow.add(ch);
      }
    }

    return listaZnakow;
  }

  public static ArrayList<Character> policzPowtarzajaceSieZnakiV2(String slowo) {
    ArrayList<Character> listaZnakow = new ArrayList<Character>();

    if (slowo != null) {
      Map<Character, Long> histo =
          slowo
              .chars()
              .mapToObj(c -> (char) c)
              .collect(Collectors.groupingBy(c -> c, Collectors.counting()));

      for (Map.Entry<Character, Long> para : histo.entrySet())
        if (para.getValue() > 1 && !listaZnakow.contains(para.getKey()))
          listaZnakow.add(para.getKey());
    }

    return listaZnakow;
  }

  public static boolean wektoryRowne(ArrayList<Character> v1, ArrayList<Character> v2) {
    Collections.sort(v1);
    Collections.sort(v2);
    return v1.equals(v2);
  }

  public static void test1() {
    String zdanie = "Halo nazywam sie Pan";
    ArrayList<Character> listaZnakow = new ArrayList<Character>(Arrays.asList('a', ' ', 'n'));

    assert wektoryRowne(policzPowtarzajaceSieZnakiV1(zdanie), listaZnakow);
  }

  public static void test2() {
    String zdanie = "Halo nazywam sie Pan";
    ArrayList<Character> listaZnakow = new ArrayList<Character>(Arrays.asList('a', ' ', 'n'));

    assert wektoryRowne(policzPowtarzajaceSieZnakiV1(zdanie), listaZnakow);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

