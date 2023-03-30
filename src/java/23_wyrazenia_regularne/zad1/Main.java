/*
Tytul: Sprawdz poprawnosc adresu e-mail.
Tresc: Masz napis reprezentujacy adres e-mail. Sprawdz, czy jest on poprawny.
Pamietaj, ze kazdy adres e-mail sklada sie z identyfikatora uzytkownika, znaku @ oraz nazwy domenowej.
Identyfikator uzytkownika sklada sie tylko z:
* Malych (a-z) i wielkich (A-Z) liter.
* Cyfr (0-9).
* Znakow ! # $ % & ' * + — / = ? ^ _ ` { | } ~.
* Kropek . pod warunkiem, ze nie jest pierwszym lub ostatnim znakiem i nie wystepuje dwukrotnie po sobie.
Nazwa domenowa sklada sie tylko z:
* Malych (a-z) i wielkich (A-Z) liter.
* Cyfr (0-9).
* Kropek . oraz myslnika — pod warunkiem, ze nie sa pierwszym lub ostatnim znakiem i nie wystepuja dwukrotnie po sobie.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisu: “adam@gmail.com”, powinna zostac zwrocona wartosc logiczna: Prawda.

*/
import java.util.*;

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

