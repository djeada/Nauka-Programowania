/*
Tytul: Liczba zer i jedynek w reprezentacji binarnej.
Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej.
a) Oblicz, ile zer zawiera binarna reprezentacja otrzymanej liczby.
b) Oblicz, ile jedynek zawiera binarna reprezentacja otrzymanej liczby.
Dane wejsciowe: Liczba naturalna w obu podpunktach.
Dane wyjsciowe: Liczba naturalna w obu podpunktach.
Przyklad:
a) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 0.
b) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 2.

*/
public class Main {
  // Znajdz dlugosc najdluzszego ciagu zer w liczbie binarnej.

  public static int najdluzszyCiagZer(int liczba) {
    if (liczba == 0) {
      return 1;
    }

    int wynik = 0;
    int pom = 0;

    while (liczba != 0) {
      int reszta = liczba % 2;
      liczba /= 2;
      if (reszta == 1) {
        wynik = Math.max(wynik, pom);
        pom = 0;
      } else {
        pom++;
      }
    }
    return Math.max(wynik, pom);
  }

  public static void test1() {
    int liczba = 111;
    int wynik = 1;

    assert najdluzszyCiagZer(liczba) == wynik;
  }

  public static void test2() {
    int liczba = 8219;
    int wynik = 8;

    assert najdluzszyCiagZer(liczba) == wynik;
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

