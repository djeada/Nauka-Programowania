/*
Tytul: Zamien A na B.
Tresc: Otrzymujesz dwie liczby naturalne. Oblicz, ile bitow nalezy odwrocic, aby zamienic liczbe A na liczbe B.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych liczb 34 i 73, powinna zostac zwrocona liczba 5.

*/
public class Main {
  // Zamien miejscami sasiadujace bity.
  public static int zamienSasiadow(int liczba) {
    int parzyste = (int) (liczba & 0xAAAAAAAA);
    int nieparzyste = liczba & 0x55555555;

    parzyste >>= 1;
    nieparzyste <<= 1;

    return parzyste | nieparzyste;
  }

  public static void test1() {
    int liczba = 9131;
    int wynik = 4951;

    assert zamienSasiadow(liczba) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

