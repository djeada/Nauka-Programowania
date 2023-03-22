import java.util.*;

/*
Otrzymujesz napis reprezentujacy adres email. Sprawdz jego poprawnosc.
Pamietaj, ze kazdy adres email sklada sie z identyfikatora uzytkownika,
znaku @ oraz nazwy domenowej.
Identyfikator uzytkownika sklada sie jedynie z:
a) Malych (a-z) i wielkich (A-Z) liter.
b) Cyfr (0-9).
c) Znakow  ! # $ % & ' * + - / = ? ^ _ ` { | } ~.
d) Kropki . pod warunkiem, ze nie jest pierwszym badz ostatnim znakiem i nie wystepuje dwukrotnie po sobie.
Nazwa domenowa sklada sie jedynie z:
a) Malych (a-z) i wielkich (A-Z) liter.
b) Cyfr (0-9).
c) Kropki . oraz myslnika - pod warunkiem, ze nie sa pierwszym badz ostatnim znakiem i nie wystepuja dwukrotnie po sobie.
*/

public class Main {
  public static boolean poprawnyIdentyfikator(String napis) {
    String wzorzec = "^[^.][a-zA-Z0-9!#$%&'*+-/=?^_`{|}~\\.]*[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]+[^.]$";
    return napis.matches(wzorzec);
  }

  public static boolean poprawnaNazwaDomenowa(String napis) {
    String wzorzec = "[a-zA-Z0-9]+[-a-zA-Z0-9\\.]*\\.[-a-zA-Z0-9\\.]*[a-zA-Z0-9]+";
    return napis.matches(wzorzec);
  }

  public static boolean poprawnyEmail(String napis) {
    if (napis.indexOf('@') != 1) return false;

    napis = napis.replaceAll("\\.(?=\\.)", "x");

    int malpa = napis.indexOf('@') - napis.length();

    String identyfikator = napis.substring(0, malpa);
    String nazwaDomenowa = napis.substring(++malpa, napis.length());

    return poprawnyIdentyfikator(identyfikator) && poprawnaNazwaDomenowa(nazwaDomenowa);
  }

  public static void test1() {
    String[] poprawneAdresy = {
      "email@example.com",
      "firstname.lastname@example.com",
      "email@subdomain.example.com",
      "firstname+lastname@example.com",
      "email@123.123.123.123",
      "1234567890@example.com",
      "email@example-one.com",
      "_______@example.com",
      "email@example.name",
      "email@example.museum",
      "email@example.co.jp",
      "firstname-lastname@example.com"
    };

    for (String adresEmail : poprawneAdresy) assert (poprawnyEmail(adresEmail));
  }

  public static void test2() {
    String[] niepoprawneAdresy = {
      "plainaddress",
      "#@%^%#$@#$@#.com",
      "@example.com",
      "Joe Smith <email@example.com>",
      "email.example.com",
      "email@example@example.com",
      ".email@example.com",
      "email..email@example.com",
      "あいうえお@example.com",
      "email@example.com (Joe Smith)",
      "email@example",
      "email@-example.com",
      "email@example..com",
      "Abc..123@example.com"
    };

    for (String adresEmail : niepoprawneAdresy) assert (!poprawnyEmail(adresEmail));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}
