/*
Tytul: Wczytaj, zmodyfikuj i wypisz.
Tresc: Wczytaj liczbe calkowita N oraz N liczb calkowitych i umiesc je w liscie. Nastepnie:
a) Dodaj 1 do kazdego elementu listy.
b) Pomnoz kazdy element przez jego indeks w liscie (indeksy zaczynaja sie od 0).
c) Zastap wszystkie elementy wartoscia pierwszego elementu listy.
Dla kazdego z powyzszych podpunktow wypisz zmodyfikowana liste. Elementy listy powinny byc oddzielone przecinkami i wypisane w jednym wierszu.
Dane wejsciowe: N oraz N liczb calkowitych.
Dane wyjsciowe: N liczb calkowitych.
Przyklad:
Dla N rownego 3 oraz pobranych liczb 3, 9, 7 w pierwszym podpunkcie powinno zostac wypisana: 4, 10, 8.

*/
import java.util.*;

public class Main {
  // Otrzymujesz dokladnie 6 liczb. Otrzymane liczby stanowia
  // odpowienio wspolrzedne xA, yA, xB, yB, xC, yC. Sprawdz
  // czy punkty A, B oraz C moga stanowic wierzcholki trojkata.

  public static double odleglosc(int x1, int y1, int x2, int y2) {
    int roznicaX = x1 - x2;
    int roznicaY = y1 - y2;
    double sumaKwadratow = Math.pow(roznicaX, 2) + Math.pow(roznicaY, 2);
    return Math.sqrt(sumaKwadratow);
  }

  public static boolean czyTrojkatV1(ArrayList<Integer> wsplX, ArrayList<Integer> wsplY) {

    assert wsplX.size() == wsplY.size() && wsplX.size() == 3;

    double odlegloscAB = odleglosc(wsplX.get(0), wsplY.get(0), wsplX.get(1), wsplY.get(1));
    double odlegloscBC = odleglosc(wsplX.get(2), wsplY.get(2), wsplX.get(1), wsplY.get(1));
    double odlegloscAC = odleglosc(wsplX.get(0), wsplY.get(0), wsplX.get(2), wsplY.get(2));

    return (odlegloscAB + odlegloscBC) > odlegloscAC
        && (odlegloscAB + odlegloscAC) > odlegloscBC
        && (odlegloscAC + odlegloscBC) > odlegloscAB;
  }

  public static boolean czyTrojkatV2(ArrayList<Integer> wsplX, ArrayList<Integer> wsplY) {

    assert wsplX.size() == wsplY.size() && wsplX.size() == 3;

    int a =
        wsplX.get(0) * (wsplY.get(1) - wsplY.get(2))
            + wsplX.get(1) * (wsplY.get(2) - wsplY.get(0))
            + wsplX.get(2) * (wsplY.get(0) - wsplY.get(1));

    return a != 0;
  }

  public static void test1() {
    ArrayList<Integer> wsplX = new ArrayList<Integer>(Arrays.asList(-2, 7, 8));
    ArrayList<Integer> wsplY = new ArrayList<Integer>(Arrays.asList(4, 5, -8));
    assert czyTrojkatV1(wsplX, wsplY);
    assert czyTrojkatV2(wsplX, wsplY);
  }

  public static void test2() {
    ArrayList<Integer> wsplX = new ArrayList<Integer>(Arrays.asList(0, 2, 5));
    ArrayList<Integer> wsplY = new ArrayList<Integer>(Arrays.asList(0, -2, -5));
    assert !czyTrojkatV1(wsplX, wsplY);
    assert !czyTrojkatV2(wsplX, wsplY);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

