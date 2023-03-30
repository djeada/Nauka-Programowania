/*
Tytul: Pierwsze wystapienie klucza.
Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna jako klucz. Znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna jako klucz.
Dane wyjsciowe: Liczba calkowita oznaczajaca indeks pierwszego wystapienia klucza w liscie.
Przyklad:
Dla otrzymanej listy [2, 9, -1, 3, 8] oraz klucza -1 powinno zostac zwrocone 2.

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste skladajaca sie z ciagu liter A i B.
  // Litery A reprezentuja samochod jadacy na wschod, a
  // litery B jadacy na zachod.  Samochody jadace w przeciwna
  // stronw mijaja sie. Policz mijajace sie samochody.

  public static int policzSamochodyV1(ArrayList<Character> lista) {

    int licznik = 0;

    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i) == 'A') {
        for (int j = i + 1; j < lista.size(); j++) {
          if (lista.get(j) == 'B') {
            licznik++;
          }
        }
      } else if (lista.get(i) == 'B') {
        for (int j = i - 1; j > -1; j--) {
          if (lista.get(j) == 'A') {
            licznik++;
          }
        }
      }
    }

    return licznik / 2;
  }

  public static int policzSamochodyV2(ArrayList<Character> lista) {
    int licznik = 0;
    int pom = 0;

    for (var x : lista) {
      if (x == 'A') {
        pom++;
      } else if (x == 'B') {
        licznik += pom;
      }
    }

    return licznik;
  }

  public static void test1() {
    ArrayList<Character> lista = new ArrayList<Character>(Arrays.asList('A', 'B', 'A', 'B', 'B'));
    int wynik = 5;
    assert policzSamochodyV1(lista) == wynik;
    assert policzSamochodyV2(lista) == wynik;
  }

  public static void test2() {
    ArrayList<Character> lista =
        new ArrayList<Character>(
            Arrays.asList('A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A'));
    int wynik = 15;
    assert policzSamochodyV1(lista) == wynik;
    assert policzSamochodyV2(lista) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

