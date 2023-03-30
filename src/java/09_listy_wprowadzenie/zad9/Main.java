/*
Tytul: Znalezienie indeksu najmniejszego elementu w posortowanej i przesunietej w prawo liscie.
Tresc: Dla otrzymanej listy liczb calkowitych, znajdz indeks najmniejszego elementu. Lista jest posortowana rosnaco, ale zostala przesunieta w prawo o okreslona liczbe miejsc. Przykladowo dla przesuniecia w prawo o 1, ostatni element trafia na pierwsze miejsce, a przedostatni na ostatnie miejsce itd.
Dane wejsciowe: Lista liczb calkowitych oraz liczba naturalna okreslajaca przesuniecie w prawo.
Dane wyjsciowe: Liczba calkowita.
Przyklad:
Dla otrzymanej listy: [7, 8, -1, 4, 5] zostanie zwrocona liczba: 2.

*/
import java.util.*;

public class Main {

  public static List<Integer> usunDuplikatyV1(List<Integer> lista) {

    List<Integer> wynik = new ArrayList<Integer>();

    for (int x : lista) if (!wynik.contains(x)) wynik.add(x);

    return wynik;
  }

  public static List<Integer> usunDuplikatyV2(List<Integer> lista) {

    List<Integer> wynik = new ArrayList<Integer>();
    Set<Integer> zbior = new HashSet<>();

    for (int x : lista) if (zbior.add(x)) wynik.add(x);

    return wynik;
  }

  public static void main(String[] args) {

    List<Integer> lista = new ArrayList<>(Arrays.asList(2, 1, 2, 2, 3, 3));
    List<Integer> wynik = new ArrayList<>(Arrays.asList(2, 1, 3));

    assert usunDuplikatyV1(lista).equals(wynik);
    assert usunDuplikatyV2(lista).equals(wynik);
  }
}

