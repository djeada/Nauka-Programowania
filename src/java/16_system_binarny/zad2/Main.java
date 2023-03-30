/*
Tytul: Wybieranie minimum i maksimum.
Tresc: Otrzymujesz dwie liczby naturalne.
a) Zwroc mniejsza z nich. Zabronione jest uzycie instrukcji warunkowej oraz zewnetrznych bibliotek.
b) Zwroc wieksza z nich. Zabronione jest uzycie instrukcji warunkowej oraz zewnetrznych bibliotek.
Dane wejsciowe: Dwie liczby naturalne w obu podpunktach.
Dane wyjsciowe: Liczba naturalna w obu podpunktach.
Przyklad:
a) Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona liczba: 2.
b) Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona liczba: 3.

*/
public class Main {
  // Otrzymujesz liczbe, zamien ja na jej binarny odpowiednik jesli:

  // a) jest liczba parzysta.
  public static String naBin(int liczba) {

    String bin = "";

    while (liczba > 0) {
      bin = String.valueOf(liczba % 2) + bin;
      liczba /= 2;
    }

    return bin;
  }

  public static String zamienLiczbeParzysta(int liczba) {
    if (liczba % 2 == 0) {
      return naBin(liczba);
    }

    return "";
  }

  // b) jest liczba pierwsza.
  public static boolean czyPierwsza(int n) {

    if (n <= 1) {
      return false;
    }

    if (n % 2 == 0 && n != 2) {
      return false;
    }

    for (int i = 3; i <= Math.sqrt((double) n); i += 2) {
      if (n % i == 0) {
        return false;
      }
    }

    return true;
  }

  public static String zamienLiczbePierwsza(int liczba) {
    if (czyPierwsza(liczba)) {
      return naBin(liczba);
    }

    return "";
  }

  public static void test1() {
    int liczba = 3;
    String wynik = "";

    assert wynik.equals(zamienLiczbeParzysta(liczba));
  }

  public static void test2() {
    int liczba = 124;
    String wynik = "1111100";

    assert wynik.equals(zamienLiczbeParzysta(liczba));
  }

  public static void test3() {
    int liczba = 124;
    String wynik = "";

    assert wynik.equals(zamienLiczbePierwsza(liczba));
  }

  public static void test4() {
    int liczba = 3;
    String wynik = "11";

    assert wynik.equals(zamienLiczbePierwsza(liczba));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
    test4();
  }
}

