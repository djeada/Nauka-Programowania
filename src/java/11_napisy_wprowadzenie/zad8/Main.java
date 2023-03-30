/*
Tytul: Konwersja listy na napis
Tresc: Otrzymujesz liste liczb naturalnych. Zamie liste na napis.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej listy: [2, 4, 7], powinien zostac zwrocony napis: “247”.

*/
public class Main {
  // Otrzymujesz napis reprezuntajacy zdanie.
  // Podziel zdanie na slowa skladowe.
  // Znaki interpunkcyjne nie sa liczone jako slowa.

  public static String wyczysc(String napis) {
    napis = napis.trim();

    return napis.replaceAll("\\p{Punct}", "");
  }

  public static void slowaV1(String napis) {
    int pocz = 0;
    int konc = 0;
    while ((konc = napis.indexOf(' ', pocz)) != -1) {
      if (konc != pocz) {
        var slowo = napis.substring(pocz, konc);
        slowo = wyczysc(slowo);
        if (!slowo.isEmpty()) {
          System.out.print(slowo);
          System.out.print("\n");
        }
      }
      pocz = konc + 1;
    }
    if (konc != pocz) {
      var slowo = napis.substring(pocz);
      slowo = wyczysc(slowo);
      if (!slowo.isEmpty()) {
        System.out.print(slowo);
        System.out.print("\n");
      }
    }
  }

  public static void main(String[] args) {
    String napis = "We think in generalities, but we live in details";
    slowaV1(napis);
  }
}

