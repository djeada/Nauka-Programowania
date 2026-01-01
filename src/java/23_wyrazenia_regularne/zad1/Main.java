/*
ZAD-01 — Sprawdź poprawność adresu e-mail

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Otrzymujesz napis reprezentujący adres e-mail. Sprawdź, czy jest poprawny zgodnie z regułami:

* Adres e-mail składa się z identyfikatora użytkownika, znaku `@` oraz nazwy domeny.
* **Identyfikator użytkownika** może zawierać wyłącznie:

  * litery `a–z`, `A–Z`,
  * cyfry `0–9`,
  * znaki specjalne: `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`,
  * kropki `.`, ale:

    * nie może być pierwszym ani ostatnim znakiem,
    * nie może wystąpić dwukrotnie po sobie.
* **Nazwa domeny** może zawierać wyłącznie:

  * litery `a–z`, `A–Z`,
  * cyfry `0–9`,
  * kropki `.` oraz myślniki `-`, ale:

    * nie mogą być pierwszym ani ostatnim znakiem,
    * nie mogą wystąpić dwukrotnie po sobie.

### Wejście

Jedna linia:

* `email`

### Wyjście

Jedna linia:

* `Prawda` — jeśli e-mail jest poprawny
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
adam@gmail.com
```

**Wyjście:**

```
Prawda
```

*/
import java.util.*;

public class Main {
  // Sprawdza poprawność identyfikatora w adresie email
  // Złożoność czasowa: O(n) gdzie n to długość napisu
  // Złożoność pamięciowa: O(1)
  public static boolean poprawnyIdentyfikator(String napis) {
    String wzorzec = "^[^.][a-zA-Z0-9!#$%&'*+-/=?^_`{|}~\\.]*[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]+[^.]$";
    return napis.matches(wzorzec);
  }

  // Sprawdza poprawność nazwy domenowej
  // Złożoność czasowa: O(n) gdzie n to długość napisu
  // Złożoność pamięciowa: O(1)
  public static boolean poprawnaNazwaDomenowa(String napis) {
    String wzorzec = "[a-zA-Z0-9]+[-a-zA-Z0-9\\.]*\\.[-a-zA-Z0-9\\.]*[a-zA-Z0-9]+";
    return napis.matches(wzorzec);
  }

  // Sprawdza poprawność całego adresu email
  // Złożoność czasowa: O(n) gdzie n to długość adresu
  // Złożoność pamięciowa: O(n)
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

