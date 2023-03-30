/*
Tytul: Usun fragment napisu.
Tresc: Dostajesz dwa napisy. Pierwszy napis to tekst, a drugi to slowo, ktore nalezy usunac z tekstu. Jesli w tekscie znajduje sie slowo do usuniecia, usun cala czesc tekstu od slowa do konca. Zwroc zmodyfikowany tekst.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla podanych napisow:
> Turned it up should no valley cousin he.
Speaking numerous ask did horrible packages set.
Ashamed herself has distant can studied mrs.
Led therefore its middleton perpetual fulfilled provision frankness.
Small he drawn after among every three no.
All having but you edward genius though remark one.
Rooms oh fully taken by worse do.
Points afraid but may end law lasted.
Was out laughter raptures returned outweigh.
Luckily cheered colonel me do we attacks on highest enabled.
Tried law yet style child.
Bore of true of no be deal.
Frequently sufficient in be unaffected.
The furnished she concluded depending procuring concealed.
oraz slowa "a", powinien zostac zwrocony napis:
> Turned it up should no v
Spe
Ash
Led therefore its middleton perpetu
Sm
All h
Rooms oh fully t
Points
W
Luckily cheered colonel me do we
Tried l
Bore of true of no be de
Frequently sufficient in be un
The furnished she concluded depending procuring conce.

*/
import java.util.*;

public class Main {
  public static ArrayList<String> podzielNapisV1(String napis) {
    String[] tablica = napis.split("\\p{Punct}+");
    List<String> lista = new ArrayList<String>();
    for (String slowo : tablica) {
      if (!slowo.isEmpty()) {
        lista.add(slowo);
      }
    }
    return lista;
  }

  public static void test1() {
    String napis = "Ani nie poszedl do kina, ani nie wybral sie do teatru.";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("Ani");
    oczekiwane.add("nie");
    oczekiwane.add("poszedl");
    oczekiwane.add("do");
    oczekiwane.add("kina");
    oczekiwane.add("ani");
    oczekiwane.add("nie");
    oczekiwane.add("wybral");
    oczekiwane.add("sie");
    oczekiwane.add("do");
    oczekiwane.add("teatru");
    assert podzielNapisV1(napis).equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
  }
}

