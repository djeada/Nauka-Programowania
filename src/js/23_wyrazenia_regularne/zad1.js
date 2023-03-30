/*

Tytuł: Sprawdź poprawność adresu e-mail.

Treść: Masz napis reprezentujący adres e-mail. Sprawdź, czy jest on poprawny.

Pamiętaj, że każdy adres e-mail składa się z identyfikatora użytkownika, znaku @ oraz nazwy domenowej.

Identyfikator użytkownika składa się tylko z:

* Małych (a-z) i wielkich (A-Z) liter.
* Cyfr (0-9).
* Znaków ! # $ % & ' * + — / = ? ^ _ ` { | } ~.
* Kropek . pod warunkiem, że nie jest pierwszym lub ostatnim znakiem i nie występuje dwukrotnie po sobie.

Nazwa domenowa składa się tylko z:

* Małych (a-z) i wielkich (A-Z) liter.
* Cyfr (0-9).
* Kropek . oraz myślnika — pod warunkiem, że nie są pierwszym lub ostatnim znakiem i nie występują dwukrotnie po sobie.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisu: “adam@gmail.com”, powinna zostać zwrócona wartość logiczna: Prawda.

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
