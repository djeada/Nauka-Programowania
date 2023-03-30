/*
Tytul: Wywolywanie metody klasy bazowej w klasie potomnej
Tresc: Dla dwoch dowolnych klas, gdzie jedna jest klasa bazowa, a druga potomna, wywolaj metode klasy bazowej w metodzie klasy potomnej, ktora ja nadpisuje. Napisz program testujacy te klasy.

*/
public class Main {
  public static class Rodzic {
    public void info() {
      System.out.print("Jestem rodzicem");
      System.out.print("\n");
    }
  }

  public static class DzieckoA extends Rodzic {
    @Override
    public void info() {
      System.out.print("Jestem dzieckiem A");
      System.out.print("\n");
    }
  }

  public static class DzieckoB extends Rodzic {
    @Override
    public void info() {
      System.out.print("Jestem dzieckiem B");
      System.out.print("\n");
      super.info();
    }
  }

  public static void main(String[] args) {

    Rodzic rodzic = new Rodzic();
    rodzic.info();

    DzieckoA dzieckoA = new DzieckoA();
    dzieckoA.info();

    DzieckoB dzieckoB = new DzieckoB();
    dzieckoB.info();
  }
}

