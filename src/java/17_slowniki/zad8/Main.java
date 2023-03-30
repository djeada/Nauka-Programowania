/*
Tytul: Sortowanie wzgledem kluczy/wartosci
Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych. Twoim zadaniem jest wypisanie par posortowanych wzgledem napisow oraz wzgledem liczb.
Dane wejsciowe: Slownik par: napis, liczba calkowita.
Dane wyjsciowe: Lista par.
Przyklad:
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)].
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("c", 3), ("b", 4), ("x", 5)].

*/
import java.util.*;
import java.util.Map.Entry;

public class Main {

  public static Character najczesciejWystepujacyZnakV1(String slowo) {

    Map<Character, Integer> counter = new HashMap<>();

    for (Character ch : slowo.toCharArray()) {

      if (!Character.isWhitespace(ch)) {
        Integer n = counter.get(ch);

        if (n == null) counter.put(ch, 1);
        else counter.put(ch, ++n);
      }
    }

    int liczbaWystapien = Collections.max(counter.values());

    char znak = Character.MIN_VALUE;
    for (Entry<Character, Integer> entry : counter.entrySet())
      if (entry.getValue() == liczbaWystapien) znak = entry.getKey();

    return znak;
  }

  public static Character najczesciejWystepujacyZnakV2(String slowo) {

    int liczbaWystapien = -1;
    char znak = Character.MIN_VALUE;

    int[] kodyASCII = new int[256];

    for (Character ch : slowo.toCharArray()) {

      if (!Character.isWhitespace(ch)) {

        int code = (int) ch;
        kodyASCII[code]++;
        if (kodyASCII[code] > liczbaWystapien) {
          liczbaWystapien = kodyASCII[code];
          znak = ch;
        }
      }
    }

    return znak;
  }

  public static void main(String[] args) {

    String slowo = "konstantynopolitanczykowianeczka";
    Character wynik = 'n';

    assert najczesciejWystepujacyZnakV1(slowo).equals(wynik);
    assert najczesciejWystepujacyZnakV2(slowo).equals(wynik);
  }
}

