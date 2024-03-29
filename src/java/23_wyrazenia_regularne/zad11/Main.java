/*
Tytul: Czy napis sklada sie wylacznie z cyfr?
Tresc: Masz napis. Sprawdz, czy sklada sie on wylacznie z cyfr.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisu: “1234”, powinna zostac zwrocona wartosc logiczna: Prawda.

*/
import java.util.*;

public class Main {
  public static String nazwaPlikuV1(String sciezka) {
    return sciezka.replaceAll("(.*[\\\\/]+)?([^\\.]*)(.*)?", "$2");
  }

  public static void test1() {
    String sciezka = "C:\\Windows\\explorer.exe";
    String wynik = "explorer";
    assert nazwaPlikuV1(sciezka).equals(wynik);
  }

  public static void test2() {
    String sciezka = "/home/user/var/log/syslog";
    String wynik = "syslog";
    assert nazwaPlikuV1(sciezka).equals(wynik);
  }

  public static void test3() {
    String sciezka = "test.jpg.png.mp3.mp5.html.txt";
    String wynik = "test";
    assert nazwaPlikuV1(sciezka).equals(wynik);
  }

  public static void test4() {
    String sciezka = "test";
    String wynik = "test";
    assert nazwaPlikuV1(sciezka).equals(wynik);
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
    test4();
  }
}

