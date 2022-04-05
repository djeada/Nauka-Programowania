import java.util.*;

/*
Otrzymujesz napis. Zwroc napis skladajacy sie z cyfr wystepujacych w otrzymanym napisie.
*/

public class Main {

  public static String odfiltrujCyfryV1(String napis) {
    return napis.replaceAll("[^0-9]", "");
  }
  
  public static void test1() {
    String napis = "numer 32.19 wyzej niz 31.17";
    String wynik = "32193117";
    assert odfiltrujCyfryV1(napis).equals(wynik);
  }

  public static void test2() {
    String napis = "Lezy jerzy na wiezy";
    String wynik = "";
    assert odfiltrujCyfryV1(napis).equals(wynik);
  }

  public static void main(String[] args) {

    test1();
    test2();

  }
}

