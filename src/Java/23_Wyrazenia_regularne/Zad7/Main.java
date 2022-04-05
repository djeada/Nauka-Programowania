import java.util.*;

/*
Otrzymujesz napis. Podziel go wzgledem znakow interpunkcyjnych i 
zapisz w liscie. Usun spacje wystepujace na poczatku lub koncu 
otrzymanych napisow.
*/

public class Main {
  public static  ArrayList<String> podzielNapisV1(String napis) {
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