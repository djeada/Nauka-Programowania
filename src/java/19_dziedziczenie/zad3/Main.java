/*
Tytul: Polimorfizm.
Tresc: Zaprojektuj klase Zwierz oraz klasy potomne Pies i Kot. Obie klasy potomne powinny nadpisywac metode 'odglos()' zdefiniowana w klasie bazowej. Napisz program testujacy te klasy, w ktorym umiescisz obiekty wszystkich trzech klas w jednej liscie i przejdziesz przez wszystkie elementy tej listy, wywolujac dla kazdego z nich funkcje 'odglos()'."

*/
import java.util.*;

public class Main {
  private static class Zwierz {

    public void odglos() {
      System.out.print("Jestem zwierzem");
      System.out.print("\n");
    }
  }

  private static class Kot extends Zwierz {

    @Override
    public void odglos() {
      System.out.print("Miau");
      System.out.print("\n");
    }
  }

  private static class Pies extends Zwierz {

    @Override
    public void odglos() {
      System.out.print("Hau");
      System.out.print("\n");
    }
  }

  public static void main(String[] args) {

    ArrayList<Zwierz> zwierzaki =
        new ArrayList<Zwierz>(Arrays.asList(new Zwierz(), new Pies(), new Kot()));

    for (var zwierz : zwierzaki) {
      zwierz.odglos();
    }
  }
}

