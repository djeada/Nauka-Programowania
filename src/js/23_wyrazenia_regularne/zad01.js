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
function poprawny_identyfikator(identyfikator) {
  if (identyfikator.startsWith(".") || identyfikator.endsWith(".")) {
    return false;
  }

  if (/(\.{2,})/.test(identyfikator)) {
    return false;
  }

  return /^[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~.]+[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~.]*$/.test(
    identyfikator
  );
}

function poprawna_nazwa_domenowa(nazwa_domenowa) {
  if (
    nazwa_domenowa.startsWith(".") ||
    nazwa_domenowa.startsWith("-") ||
    nazwa_domenowa.endsWith(".") ||
    nazwa_domenowa.endsWith("-")
  ) {
    return false;
  }

  if (/[-.]{2,}/.test(nazwa_domenowa) || !nazwa_domenowa.includes(".")) {
    return false;
  }

  return /^[-a-zA-Z0-9.]+[-a-zA-Z0-9.]*$/.test(nazwa_domenowa);
}

function czy_email_poprawny(email) {
  if (email.split("@").length !== 2) {
    return false;
  }

  const [identyfikator, nazwa_domenowa] = email.split("@");
  if (
    !poprawny_identyfikator(identyfikator) ||
    !poprawna_nazwa_domenowa(nazwa_domenowa)
  ) {
    return false;
  }

  return true;
}

function test_czy_email_poprawny_pozytywne() {
  console.assert(czy_email_poprawny("email@example.com"));
  console.assert(czy_email_poprawny("firstname.lastname@example.com"));
  console.assert(czy_email_poprawny("email@subdomain.example.com"));
  console.assert(czy_email_poprawny("firstname+lastname@example.com"));
  console.assert(czy_email_poprawny("email@123.123.123.123"));
  console.assert(czy_email_poprawny("1234567890@example.com"));
  console.assert(czy_email_poprawny("email@example-one.com"));
  console.assert(czy_email_poprawny("_______@example.com"));
  console.assert(czy_email_poprawny("email@example.name"));
  console.assert(czy_email_poprawny("email@example.museum"));
  console.assert(czy_email_poprawny("email@example.co.jp"));
  console.assert(czy_email_poprawny("firstname-lastname@example.com"));
}

function test_czy_email_poprawny_negatywne() {
  console.assert(!czy_email_poprawny("plainaddress"));
  console.assert(!czy_email_poprawny("#@%^%#$@#$@#.com"));
  console.assert(!czy_email_poprawny("@example.com"));
  console.assert(!czy_email_poprawny("Joe Smith <email@example.com"));
  console.assert(!czy_email_poprawny("email.example.com"));
  console.assert(!czy_email_poprawny("email@example@example.com"));
  console.assert(!czy_email_poprawny(".email@example.com"));
  console.assert(!czy_email_poprawny("email..email@example.com"));
  console.assert(!czy_email_poprawny("あいうえお@example.com"));
  console.assert(!czy_email_poprawny("email@example.com (Joe Smith)"));
  console.assert(!czy_email_poprawny("email@example"));
  console.assert(!czy_email_poprawny("email@-example.com"));
  console.assert(!czy_email_poprawny("email@example..com"));
  console.assert(!czy_email_poprawny("Abc..123@example.com"));
}

function main() {
  test_czy_email_poprawny_pozytywne();
  test_czy_email_poprawny_negatywne();
}

main();

