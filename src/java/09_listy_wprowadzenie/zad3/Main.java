/*
Tytul: Rotacja w lewo/prawo.
Tresc: Otrzymujesz liste liczb calkowitych, kierunek przesuniecia (1 odpowiada przesunieciu w prawo, a 0 w lewo) oraz liczbe miejsc, o jaka elementy listy maja zostac przesuniete. Na przyklad dla przesuniecia w prawo, pierwszy element trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce. Przesun elementy listy w podanym kierunku.
Dane wejsciowe: Lista liczb calkowitych oraz dwie liczby naturalne.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostac zwrocona lista: [6, 2, 1, 10, 8, 5, 27].

*/
import java.util.stream.IntStream;

public class Main {

  public static int znajdzKluczV1(int[] tablica, int klucz) {

    for (int i = 0; i < tablica.length; i++) if (tablica[i] == klucz) return i;

    return -1;
  }

  public static int znajdzKluczV2(int[] tablica, int klucz) {

    return IntStream.range(0, tablica.length)
        .filter(i -> klucz == tablica[i])
        .findFirst()
        .orElse(-1);
  }

  private static void test1() {
    int[] tablica = new int[] {3, 5, -7, 4, 9, -11, 2};
    int klucz = 2;
    int wynik = 6;

    assert znajdzKluczV1(tablica, klucz) == wynik;
    assert znajdzKluczV2(tablica, klucz) == wynik;
  }

  private static void test2() {
    int[] tablica = new int[] {3, -2, 4, 9, -3, -40, 8, 5, -7, -1};
    int klucz = 2;
    int wynik = -1;

    assert znajdzKluczV1(tablica, klucz) == wynik;
    assert znajdzKluczV2(tablica, klucz) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

