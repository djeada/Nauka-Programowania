/*
Tytul: Zmodyfikuj elementy spelniajace warunek.
Tresc: Otrzymujesz liste liczb calkowitych. W wyniku wykonania ponizszych polecen otrzymasz nowa liste:
a) Zwieksz o 1 wszystkie elementy o parzystych indeksach (indeksy zaczynaja sie od 0).
b) Wyzeruj wszystkie elementy bedace wielokrotnosciami liczby 3.
c) Podnies do kwadratu wszystkie elementy mniejsze niz 10.
d) Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
e) Zamien kazdy element na iloczyn wszystkich elementow listy poza nim samym.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy [5, 7, 9, 4, 2]:
a) Wynik: [5, 8, 9, 5, 2]
b) Wynik: [5, 0, 0, 5, 2]
c) Wynik: [25, 0, 0, 25, 4]
d) Wynik: [37, 0, 0, 25, 4]
e) Wynik: [2592, 0, 0, 36, 1080]

*/
import java.util.*;

public class Main {
  // Dla otrzymanej listy, skladajacej sie z nieuporzadkowanych
  // kolejnych (za wyjatkiem jednego) wyrazow ciagu arytmetycznego,
  // znajdz brakujacy element.

  public static int sumaCiaguArt(ArrayList<Integer> lista) {
    int min = Collections.min(lista);
    int maks = Collections.max(lista);
    return (lista.size() + 1) * (min + maks) / 2;
  }

  public static int znajdzBrakujacyElement(ArrayList<Integer> lista) {

    int suma = 0;

    for (var liczba : lista) {
      suma += liczba;
    }

    int sumaPrzedzialu = sumaCiaguArt(lista);

    return sumaPrzedzialu - suma;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(6, 8, 4, 10, 14, 2));
    int wynik = 12;
    assert znajdzBrakujacyElement(lista) == wynik;
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 4, 5, 6));
    int wynik = 3;
    assert znajdzBrakujacyElement(lista) == wynik;
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

