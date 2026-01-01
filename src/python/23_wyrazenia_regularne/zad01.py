"""
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

"""

import re


def poprawny_identyfikator(identyfikator):
    """
    Sprawdza poprawnosc identyfikatora.
    """
    # Identyfikator uzytkownika sklada sie jedynie z:
    # a) Malych (a-z) i wielkich (A-Z) liter.
    # b) Cyfr (0-9).
    # c) Znakow  ! # $ % & ' * + - / = ? ^ _ ` { | } ~.
    # d) Kropki . pod warunkiem, ze nie jest pierwszym badz ostatnim znakiem
    # i nie wystepuje dwukrotnie po sobie.
    if identyfikator.startswith(".") or identyfikator.endswith("."):
        return False

    if re.search(r"[.]{2,}", identyfikator):
        return False

    return re.match(
        r"^[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~.]+[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~.]*$",
        identyfikator,
    )


def poprawna_nazwa_domenowa(nazwa_domenowa):
    """
    Sprawdza poprawnosc nazwy domenowej.
    """
    # Nazwa domenowa sklada sie jedynie z:
    # a) Malych (a-z) i wielkich (A-Z) liter.
    # b) Cyfr (0-9).
    # c) Kropki . oraz myslnika - pod warunkiem, ze nie sa pierwszym badz ostatnim znakiem
    # i nie wystepuja dwukrotnie po sobie.
    if (
        nazwa_domenowa.startswith(".")
        or nazwa_domenowa.startswith("-")
        or nazwa_domenowa.endswith(".")
        or nazwa_domenowa.endswith("-")
    ):
        return False

    if re.search(r"[-.]{2,}", nazwa_domenowa) or nazwa_domenowa.count(".") == 0:
        return False

    return re.match(r"^[-a-zA-Z0-9.]+[-a-zA-Z0-9.]*$", nazwa_domenowa)


def czy_email_poprawny(email):
    """
    Sprawdza poprawnosc adresu email.
    """
    # sprawdz czy malpa wystepuje w adresie dokladnie jeden raz
    if email.count("@") != 1:
        return False

    # sprawdz czy adres sklada sie z identyfikatora i nazwy domenowej
    identyfikator, nazwa_domenowa = email.split("@")
    if not poprawny_identyfikator(identyfikator) or not poprawna_nazwa_domenowa(
        nazwa_domenowa
    ):
        return False

    return True


def test_czy_email_poprawny_pozytywne():
    assert czy_email_poprawny("email@example.com")
    assert czy_email_poprawny("firstname.lastname@example.com")
    assert czy_email_poprawny("email@subdomain.example.com")
    assert czy_email_poprawny("firstname+lastname@example.com")
    assert czy_email_poprawny("email@123.123.123.123")
    assert czy_email_poprawny("1234567890@example.com")
    assert czy_email_poprawny("email@example-one.com")
    assert czy_email_poprawny("_______@example.com")
    assert czy_email_poprawny("email@example.name")
    assert czy_email_poprawny("email@example.museum")
    assert czy_email_poprawny("email@example.co.jp")
    assert czy_email_poprawny("firstname-lastname@example.com")


def test_czy_email_poprawny_negatywne():
    assert not czy_email_poprawny("plainaddress")
    assert not czy_email_poprawny("#@%^%#$@#$@#.com")
    assert not czy_email_poprawny("@example.com")
    assert not czy_email_poprawny("Joe Smith <email@example.com")
    assert not czy_email_poprawny("email.example.com")
    assert not czy_email_poprawny("email@example@example.com")
    assert not czy_email_poprawny(".email@example.com")
    assert not czy_email_poprawny("email..email@example.com")
    assert not czy_email_poprawny("あいうえお@example.com")
    assert not czy_email_poprawny("email@example.com (Joe Smith)")
    assert not czy_email_poprawny("email@example")
    assert not czy_email_poprawny("email@-example.com")
    assert not czy_email_poprawny("email@example..com")
    assert not czy_email_poprawny("Abc..123@example.com")


if __name__ == "__main__":
    test_czy_email_poprawny_pozytywne()
    test_czy_email_poprawny_negatywne()
