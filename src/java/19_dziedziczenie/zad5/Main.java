/*
Tytul: Dziedziczenie wielokrotne
Tresc: Napisz klase Ptak, dziedziczaca po klasach Zwierz i ObiektLatajacy. W sklad klasy Zwierz powinny wchodzic funkcje o nazwach 'jedz()', 'spij()', 'wydaj_dzwiek()', ktore wypisuja odpowiednie komunikaty na standardowe wyjscie. W sklad klasy ObiektLatajacy powinny wchodzic funkcje o nazwach 'lec()', 'wyladuj()', ktore wypisuja odpowiednie komunikaty na standardowe wyjscie. Napisz program testujacy te klase.

*/
public class Main {

  private static interface ZwierzInterfejs {

    public void jedz();

    public void spij();

    public void wydajDzwiek();
  }

  private static interface ObiektLatajacyInterfejs {

    public void lec();

    public void laduj();
  }

  private static class Zwierz implements ZwierzInterfejs {

    private String nazwa = "";
    private String pokarm = "";
    private String dzwiek = "";

    public Zwierz(String nazwa, String pokarm, String dzwiek) {
      this.nazwa = nazwa;
      this.pokarm = pokarm;
      this.dzwiek = dzwiek;
    }

    public final void jedz() {
      System.out.print(nazwa);
      System.out.print(" spozywa ");
      System.out.print(pokarm);
      System.out.print(".");
      System.out.print("\n");
    }

    public final void spij() {
      System.out.print(nazwa);
      System.out.print(" idzie spac.");
      System.out.print("\n");
    }

    public final void wydajDzwiek() {
      System.out.print(dzwiek);
      System.out.print("\n");
    }
  }

  private static class ObiektLatajacy implements ObiektLatajacyInterfejs {

    private String nazwa = "";

    public ObiektLatajacy(String nazwa) {
      this.nazwa = nazwa;
    }

    public final void lec() {
      System.out.print(nazwa);
      System.out.print(" wznosi sie w powietrze.");
      System.out.print("\n");
    }

    public final void laduj() {
      System.out.print(nazwa);
      System.out.print(" laduje.");
      System.out.print("\n");
    }
  }

  private static class Ptak implements ZwierzInterfejs, ObiektLatajacyInterfejs {
    Zwierz zwierz;
    ObiektLatajacy obiektLatajacy;

    public Ptak(String nazwa) {
      zwierz = new Zwierz(nazwa, "robaki", "Aww!Aww!");
      obiektLatajacy = new ObiektLatajacy(nazwa);
    }

    public final void jedz() {
      zwierz.jedz();
    }

    public final void spij() {
      zwierz.spij();
    }

    public final void wydajDzwiek() {
      zwierz.wydajDzwiek();
    }

    public final void lec() {
      obiektLatajacy.lec();
    }

    public final void laduj() {
      obiektLatajacy.laduj();
    }
  }

  public static void main(String[] args) {

    Ptak koliber = new Ptak("Koliberek");
    koliber.jedz();
    koliber.lec();
    koliber.laduj();
    koliber.wydajDzwiek();
    koliber.spij();
  }
}

