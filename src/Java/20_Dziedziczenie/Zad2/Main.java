// Zaprojektuj klase Ksztalt oraz klasy pochodne Kolo oraz Kwadrat.

public class Main {

  private static interface Ksztalt {
    double obwod();
    double pole();
  }

  private static class Kolo implements Ksztalt {
    public Kolo(double _promien) {
      if (_promien <= 0) {
        throw new IllegalArgumentException("Wartosc musi byc dodatnia.");
      }

      promien = _promien;
    }

    public final double obwod() {
      return 2 * Math.PI * promien;
    }

    public final double pole() {
      return Math.PI * Math.pow(promien, 2);
    }

    private double promien;
  }

  private static class Kwadrat implements Ksztalt {
    public Kwadrat(double _bok) {
      if (_bok <= 0) {
        throw new IllegalArgumentException("Wartosc musi byc dodatnia.");
      }

      bok = _bok;
    }

    public final double obwod() {
      return 4 * bok;
    }

    public final double pole() {
      return Math.pow(bok, 2);
    }

    private double bok;
  }

  public static void test1() {
    Kolo kolo = new Kolo(3);
    assert Math.abs(kolo.obwod() - 18.85) < 0.01;
    assert Math.abs(kolo.pole() - 28.27) < 0.01;
  }

  public static void test2() {
    Kwadrat kwadrat = new Kwadrat(3);
    assert Math.abs(kwadrat.obwod() - 12) < 0.01;
    assert Math.abs(kwadrat.pole() - 9) < 0.01;
  }

  public static void main(String[] args) {

    test1();
    test2();

  }

}