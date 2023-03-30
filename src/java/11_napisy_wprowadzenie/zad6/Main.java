/*
Tytul: Slowa ze zdania jako osobne elementy listy.
Tresc: Otrzymujesz napis reprezentujacy zdanie. Zwroc liste slow zdania. Znaki interpunkcyjne nie sa liczone jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu: “Ala ma kota”, powinna zostac zwrocona lista: [“Ala”, “ma”, “kota”].

*/
public class Main {
  // Otrzymujesz napis. Zamien litery a na znaki zapytania.
  public static String zamienV1(String napis) {

    String wynik = "";

    for (var znak : napis.toCharArray()) {
      if (znak == 'a') {
        wynik += '?';
      } else {
        wynik += znak;
      }
    }

    return wynik;
  }

  public static String zamienV2(String napis) {
    return napis.replaceAll("a", "?");
  }

  public static void test1() {
    String napis = "pacZka!";
    String wynik = "p?cZk?!";

    assert zamienV1(napis).equals(wynik);
  }

  public static void test2() {
    String napis = "pacZka!";
    String wynik = "p?cZk?!";

    assert zamienV2(napis).equals(wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

