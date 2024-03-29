/*
Tytul:  Konwersja warunkowa.
Tresc: Otrzymujesz liczbe naturalna. Zwroc reprezentacje binarna otrzymanej liczby, jesli:
a) Otrzymana liczba jest liczba parzysta.
b) Otrzymana liczba jest liczba pierwsza.
Dane wejsciowe: Liczba naturalna w obu podpunktach.
Dane wyjsciowe: Liczba naturalna w obu podpunktach.
Przyklad:
a) Dla otrzymanej liczby: 7, nie powinna zostac zwrocona zadna liczba.
b) Dla otrzymanej liczby: 7, powinna zostac zwrocona liczba: 111.

*/
public class Main {
  // Policz ile bitow nalezy odwrocic,
  // aby zamien liczbe A w liczbe B.

  public static int bityDoZmiany(int liczbaA, int liczbaB) {

    int n = liczbaA ^ liczbaB;

    int licznik = 0;
    while (n != 0) {
      n &= (n - 1);
      licznik++;
    }

    return licznik;
  }

  public static void test1() {
    int liczbaA = 34;
    int liczbaB = 73;
    int wynik = 5;

    assert bityDoZmiany(liczbaA, liczbaB) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

