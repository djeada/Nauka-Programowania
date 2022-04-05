import java.util.*;

/*
Otrzymujesz napis reprezentujacy zdanie. Zapisz w liscie cyfry 
bedace czescia slow. Cyfry odseparowane od liter spacjami pomin.
*/

public class Main {
  public static cyfryV1(String napis) {
    String[] tablica = napis.split("\\p{Punct}+");
    List<String> lista = new ArrayList<String>();
    for (String slowo : tablica) {
      if (slowo.matches("[0-9]+") && !slowo.matches("[^0-9]+")) {
        lista.add(slowo.replaceAll("[^0-9]", ""));
      }
    }
    return lista;
  }

  public static void test1() {
    String napis = "jerzy29 i an37a s3uc8ali91 lekcji 22 2 jezyka polki3go";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("29");
    oczekiwane.add("37");
    oczekiwane.add("3891");
    oczekiwane.add("3");
    assert cyfryV1(napis).equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();

  }
}