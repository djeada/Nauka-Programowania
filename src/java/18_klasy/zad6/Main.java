/*
Tytul: Zaprojektuj klase Zespolona.
Tresc: Napisz klase Zespolona, ktora bedzie reprezentowala liczbe zespolona. Klasa powinna zawierac nastepujace funkcje:
1. Konstruktor, ktory przyjmuje jako argument dwie liczby. Pierwsza liczba reprezentuje czesc rzeczywista, a druga czesc urojona liczby zespolonej. Domyslne wartosci dla obu argumentow to 0.
2. Funkcje, ktore zwracaja wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnozenie, dzielenie). Jesli jest to mozliwe, nalezy przeciazyc operatory: +, -, *, /.
3. Funkcje, ktora wypisuje informacje o liczbie zespolonej na standardowe wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Zespolona. Jesli jest to mozliwe, nalezy przeciazyc operatory == oraz !=.
5. Funkcje modul, ktora zwraca modul liczby zespolonej.
Napisz program, ktory przetestuje twoja klase. Stworz liczby zespolone: A (9, 12) oraz B (-3, -3). Wypisz na standardowe wyjscie informacje o utworzonych liczbach zespolonych oraz ich sume, roznice pierwszej i drugiej, iloraz pierwszej przez druga oraz iloczyn liczb zespolonych.

*/
import java.util.*;

public class Macierz {

  private ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>>();

  public Macierz() {}

  public Macierz(final ArrayList<ArrayList<Integer>> _macierz) {
    this.macierz = new ArrayList<ArrayList<Integer>>(_macierz);
  }

  public Macierz(Macierz innaMacierz) {
    this.macierz = innaMacierz.macierz;
  }

  public final void setElement(int wiersz, int kolumna, int wartosc) {
    if (wiersz >= wiersze() || kolumna >= kolumny()) {
      throw new IllegalArgumentException("Nieprawidlowy indeks.");
    }

    macierz.get(wiersz).set(kolumna, wartosc);
  }

  public final int element(int wiersz, int kolumna) {

    if (wiersz >= wiersze() || kolumna >= kolumny()) {
      throw new IllegalArgumentException("Nieprawidlowy indeks.");
    }

    return macierz.get(wiersz).get(kolumna);
  }

  public final int wiersze() {
    return macierz.size();
  }

  public final int kolumny() {
    if (wiersze() >= 1) {
      return macierz.get(0).size();
    } else {
      return 0;
    }
  }

  public Macierz dodaj(final Macierz innaMacierz) {

    if (wiersze() != innaMacierz.wiersze() || kolumny() != innaMacierz.kolumny()) {
      throw new IllegalArgumentException("Wymiary macierzy musza byc jednakowe.");
    }

    Macierz pom =
        new Macierz(
            new ArrayList<ArrayList<Integer>>(
                Collections.nCopies(
                    wiersze(), new ArrayList<Integer>(Collections.nCopies(kolumny(), 0)))));

    for (int i = 0; i < pom.wiersze(); i++) {
      for (int j = 0; j < pom.kolumny(); j++) {
        pom.setElement(i, j, element(i, j) + innaMacierz.element(i, j));
      }
    }

    return new Macierz(pom);
  }

  public Macierz odejmij(final Macierz innaMacierz) {

    if (wiersze() != innaMacierz.wiersze() || kolumny() != innaMacierz.kolumny()) {
      throw new IllegalArgumentException("Wymiary macierzy musza byc jednakowe.");
    }

    Macierz pom =
        new Macierz(
            new ArrayList<ArrayList<Integer>>(
                Collections.nCopies(
                    wiersze(), new ArrayList<Integer>(Collections.nCopies(kolumny(), 0)))));

    for (int i = 0; i < pom.wiersze(); i++) {
      for (int j = 0; j < pom.kolumny(); j++) {
        pom.setElement(i, j, element(i, j) - innaMacierz.element(i, j));
      }
    }

    return new Macierz(pom);
  }

  public Macierz pomnoz(final Macierz innaMacierz) {

    if (kolumny() != innaMacierz.wiersze()) {
      throw new IllegalArgumentException(
          "Liczba kolumn mnoznej musi sie rownac liczbie wierszy mnoznika.");
    }

    final int n = wiersze();
    final int m = kolumny();

    final int p = innaMacierz.kolumny();

    Macierz pom =
        new Macierz(
            new ArrayList<ArrayList<Integer>>(
                Collections.nCopies(n, new ArrayList<Integer>(Collections.nCopies(p, 0)))));

    for (int j = 0; j < p; j++) {
      for (int k = 0; k < m; k++) {
        for (int i = 0; i < n; i++) {
          pom.setElement(i, j, pom.element(i, j) + element(i, k) * innaMacierz.element(k, j));
        }
      }
    }
    return new Macierz(pom);
  }

  public void wypisz() {

    for (var wiersz : macierz) {
      for (var wartosc : wiersz) {
        System.out.print(wartosc);
        System.out.print(" ");
      }
      System.out.print("\n");
    }
  }

  public boolean equalsTo(final Macierz p1, final Macierz p2) {
    return p1.macierz == p2.macierz;
  }

  public boolean notEqualsTo(final Macierz p1, final Macierz p2) {
    return p1.macierz != p2.macierz;
  }

  public static void main(String[] args) {

    Macierz macierzA =
        new Macierz(
            new ArrayList<ArrayList<Integer>>(
                Arrays.asList(new ArrayList<Integer>(Arrays.asList(1, -2, 3)))));
    Macierz macierzB =
        new Macierz(
            new ArrayList<ArrayList<Integer>>(
                Arrays.asList(new ArrayList<Integer>(Arrays.asList(8, 9, -5)))));

    var suma = macierzA.dodaj(macierzB);
    var roznica = macierzA.odejmij(macierzB);

    System.out.print("Macierz A \n");
    macierzA.wypisz();
    System.out.print("Macierz B \n");
    macierzB.wypisz();
    System.out.print("\n");
    System.out.print("suma: \n");
    suma.wypisz();
    System.out.print("\n");
    System.out.print("roznica: \n");
    roznica.wypisz();
    System.out.print("\n");

    macierzA =
        new Macierz(
            new ArrayList<ArrayList<Integer>>(
                Arrays.asList(new ArrayList<Integer>(Arrays.asList(1, 2, 3)))));
    macierzB =
        new Macierz(
            new ArrayList<ArrayList<Integer>>(
                Arrays.asList(
                    new ArrayList<Integer>(Arrays.asList(4)),
                    new ArrayList<Integer>(Arrays.asList(5)),
                    new ArrayList<Integer>(Arrays.asList(6)))));

    var iloczynAB = macierzA.pomnoz(macierzB);
    var iloczynBA = macierzB.pomnoz(macierzA);

    System.out.print("Macierz A \n");
    macierzA.wypisz();
    System.out.print("Macierz B \n");
    macierzB.wypisz();
    System.out.print("\n");
    System.out.print("iloczyn A*B: \n");
    iloczynAB.wypisz();
    System.out.print("\n");
    System.out.print("iloczyn B*A: \n");
    iloczynBA.wypisz();
    System.out.print("\n");
  }
}

