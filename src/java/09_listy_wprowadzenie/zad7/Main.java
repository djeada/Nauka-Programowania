/*
Tytul: Znalezienie indeksow pierwszej pary elementow listy o sumie rownej podanej liczbie.
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz indeksy pierwszej pary elementow listy, ktorych suma jest rowna x. Jesli taka para nie istnieje, zwroc pare (-1, -1).
Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.
Dane wyjsciowe: Para liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [1, 3, 4, 5, 2] oraz liczby 5, zostana zwrocone indeksy pierwszej pary elementow o sumie rownej 5: (0, 2).

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy znajdz liczbe mniejsza
  // od najwiekszej liczby z listy i jednoczesnie
  // wieksza od wszystkich pozostalych.
  public static double wieksza(ArrayList<Integer> lista) {

    if (lista.isEmpty()) {
      return 0.00;
    }

    if (lista.size() == 1) {
      return lista.get(0) - 1;
    }

    int maks = Integer.MIN_VALUE;
    int maks2 = Integer.MIN_VALUE;

    for (var liczba : lista) {

      if (liczba > maks) {
        maks2 = maks;
        maks = liczba;
      } else if (liczba > maks2) {
        maks2 = liczba;
      }
    }

    return (maks + maks2) / 2.00;
  }

  public static void main(String[] args) {

    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
    System.out.print(wieksza(lista));
    System.out.print("\n");

    lista = new ArrayList<Integer>(Arrays.asList(3, -2, 4, 9, -3, -40, 8, 5, -7, -1));
    System.out.print(wieksza(lista));
    System.out.print("\n");
  }
}

