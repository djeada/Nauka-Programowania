import java.text.MessageFormat;

public class Punkt {

  private double x;
  private double y;

  public Punkt(double _x) {
    this(_x, 0);
  }

  public Punkt() {
    this(0, 0);
  }

  public Punkt(double _x, double _y) {
    this.x = _x;
    this.y = _y;
  }

  public final void setX(double _x) {
    x = _x;
  }

  public final void setY(double _y) {
    y = _y;
  }

  public final double getX() {
    return x;
  }

  public final double getY() {
    return y;
  }

  public final double odleglosc(Punkt innyPunkt) {
    double odlegloscX = x - innyPunkt.getX();
    double odlegloscY = y - innyPunkt.getY();

    return Math.sqrt(Math.pow(odlegloscX, 2) + Math.pow(odlegloscY, 2));
  }

  @Override
  public String toString() {

    return MessageFormat.format("({0}, {1})", this.x, this.y);
  }

  public boolean equalsTo(final Punkt p1, final Punkt p2) {
    return p1.x == p2.x && p1.y == p2.y;
  }

  public boolean notEqualsTo(final Punkt p1, final Punkt p2) {
    return p1.x != p2.x || p1.y != p2.y;
  }

  public static void main(String[] args) {

    Punkt punktA = new Punkt(5, 5);
    Punkt punktB = new Punkt(-3, -3);

    System.out.print("Odleglosc miedzy punktem A ");
    System.out.print(punktA);
    System.out.print(", a punktem B ");
    System.out.print(punktB);
    System.out.print(" wynosi: ");
    System.out.print(punktA.odleglosc(punktB));
    System.out.print("\n");
  }
}
