import java.text.MessageFormat;

public class Kolo {
	
  public Kolo() {
    this(1);
  }

  public Kolo(double r) {
    if (r <= 0) {
      System.out.print("Promien nie moze byc liczba ujemna.\n");
      System.out.print("Promien ustawiono na 1.\n");
      promien = 1.0;
    } else {
      promien = r;
    }
  }

  public final void setPromien(double r) {
    promien = r;
  }

  public final double getPromien() {
    return promien;
  }

  public final double pole() {
    return Math.PI * Math.pow(promien, 2);
  }

  public final double obwod() {
    return 2 * Math.PI * promien;
  }

  public final double srednica() {
    return 2 * promien;
  }

  @Override
  public String toString() {

    return MessageFormat.format("Promien = {0}.\nSrednica = {1}.\nPole = {2}.\nObwod = {3}.", this.promien, this.srednica(), this.pole(), this.obwod());

  }

  private double promien;

  public static void main(String[] args) {

    Kolo kolo = new Kolo(3);
    System.out.print(kolo);

  }
}