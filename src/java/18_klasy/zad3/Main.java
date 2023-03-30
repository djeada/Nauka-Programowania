/*
Tytul: Prostokat powstaly z nalozenia sie dwoch prostokatow.
Opis zadania: Napisz klase Prostokat, ktora bedzie reprezentowala prostokat w ukladzie kartezjanskim. Prostokat jest okreslony przez wspolrzedne jego czterech wierzcholkow. Boki prostokata sa prostopadle do osi ukladu wspolrzednych. Klasa powinna zawierac funkcje statyczna, ktora zwraca pole prostokata powstalego z nalozenia sie dwoch prostokatow. Jesli dwa prostokaty nie pokrywaja sie, funkcja powinna zwracac 0.
Napisz program, ktory przetestuje twoja klase. Stworz prostokaty: A (3, 6, 9, 4) oraz B (2, 5, 7, 2). Wypisz na standardowe wyjscie informacje o utworzonych prostokatach. Sprawdz, czy pole czesci wspolnej rowne jest 6.

*/
public class Prostokat {

  private double lewo;
  private double prawo;
  private double gora;
  private double dol;

  public Prostokat(double _lewo, double _prawo, double _gora, double _dol) {
    this.lewo = _lewo;
    this.prawo = _prawo;
    this.gora = _gora;
    this.dol = _dol;
  }

  public final double getLewo() {
    return lewo;
  }

  public final double getPrawo() {
    return prawo;
  }

  public final double getGora() {
    return gora;
  }

  public final double getDol() {
    return dol;
  }

  public final double poleCzesciWspolnej(Prostokat innyProstokat) {
    double poleX =
        Math.max(
            0.00,
            Math.min(prawo, innyProstokat.getPrawo()) - Math.max(lewo, innyProstokat.getLewo()));
    double poleY =
        Math.max(
            0.00, Math.min(gora, innyProstokat.getGora()) - Math.max(dol, innyProstokat.getDol()));
    return poleX * poleY;
  }

  public static void test1() {
    Prostokat prostokatA = new Prostokat(2, 5, 7, 2);
    Prostokat prostokatB = new Prostokat(3, 6, 9, 4);
    double wynik = 6.00;

    assert prostokatA.poleCzesciWspolnej(prostokatB) == wynik;
  }

  public static void test2() {
    Prostokat prostokatA = new Prostokat(-9.5, 10.5, 6, 2);
    Prostokat prostokatB = new Prostokat(-4.5, 2.3, 3.8, -3.3);
    double wynik = 12.24;

    assert Math.abs(prostokatA.poleCzesciWspolnej(prostokatB) - wynik) < 0.01;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

