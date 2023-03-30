/*
Tytul: Wczytaj i rozdziel informacje o pracowniku.
Tresc: Otrzymasz rekord z bazy danych reprezentujacy dane pracownika. Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki. Informacje sa rozdzielone srednikami. Zapisz je w osobnych zmiennych i wypisz je razem z odpowiednimi komunikatami.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu:
"Jan; Kowalski; Warszawa; Programista; 1000;",
powinna zostac zwrocona lista:
["Imie: Jan", "Nazwisko: Kowalski", "Miejsce urodzenia: Warszawa", "Zawod: Programista", "Zarobki: 1000"].

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste liczb.
  // Zamien liste na napis.

  public static String liczby(final ArrayList<Integer> lista) {
    String wynik = "";

    for (var liczba : lista) {
      wynik += String.valueOf(liczba);
    }

    return wynik;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(2, 4, 7));
    String wynik = "247";
    assert wynik.equals(liczby(lista));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    String wynik = "";
    assert wynik.equals(liczby(lista));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

