/*

Tytul: Sprawdz poprawnosc hasla.

Tresc: Masz napis reprezentujacy haslo. Sprawdz, czy haslo spelnia nastepujace warunki:

1. Haslo musi zawierac przynajmniej jedna mala litere [a-z].
2. Haslo musi zawierac przynajmniej jedna duza litere [A-Z].
3. Haslo musi zawierac przynajmniej jedna cyfre [0-9].
4. Haslo musi zawierac przynajmniej jeden znak specjalny [! # $ % & ' * + — / = ? ^ _ ` { | } ~].
5. Minimalna dlugosc hasla to 8 znakow.
6. Maksymalna dlugosc hasla to 20 znakow.

Dane wejsciowe: Napis.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla napisu: “abc1234”, powinna zostac zwrocona wartosc logiczna: Falsz.

*/

function czy_haslo_poprawne(haslo) {
  const minDlugosc = 8;
  const maxDlugosc = 20;
  const malaLitera = /[a-z]/;
  const duzaLitera = /[A-Z]/;
  const cyfra = /[0-9]/;
  const znakSpecjalny = /[!#$%&'*+\-/=?^_`{|}~]/;

  if (haslo.length < minDlugosc || haslo.length > maxDlugosc) {
    return false;
  }

  if (!malaLitera.test(haslo)) {
    return false;
  }

  if (!duzaLitera.test(haslo)) {
    return false;
  }

  if (!cyfra.test(haslo)) {
    return false;
  }

  if (!znakSpecjalny.test(haslo)) {
    return false;
  }

  return true;
}

function test_czy_haslo_poprawne() {
  console.assert(!czy_haslo_poprawne("Ab1!"));
  console.assert(!czy_haslo_poprawne("haslo"));
  console.assert(!czy_haslo_poprawne("HASLO"));
  console.assert(!czy_haslo_poprawne("HASLO123!@#"));
  console.assert(!czy_haslo_poprawne("12345678"));
  console.assert(!czy_haslo_poprawne("proste_haslo"));
  console.assert(!czy_haslo_poprawne("Haslo123"));
  console.assert(czy_haslo_poprawne("Haslo123!"));
  console.assert(czy_haslo_poprawne("Haslo123!#"));
  console.assert(czy_haslo_poprawne("Haslo123!#$"));
  console.assert(czy_haslo_poprawne("Haslo123!#$%&*"));
}

test_czy_haslo_poprawne();

