/*

Tytuł: Sprawdź poprawność hasła.

Treść: Masz napis reprezentujący hasło. Sprawdź, czy hasło spełnia następujące warunki:

1. Hasło musi zawierać przynajmniej jedną małą literę [a-z].
2. Hasło musi zawierać przynajmniej jedną dużą literę [A-Z].
3. Hasło musi zawierać przynajmniej jedną cyfrę [0-9].
4. Hasło musi zawierać przynajmniej jeden znak specjalny [! # $ % & ' * + — / = ? ^ _ ` { | } ~].
5. Minimalna długość hasła to 8 znaków.
6. Maksymalna długość hasła to 20 znaków.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisu: “abc1234”, powinna zostać zwrócona wartość logiczna: Fałsz.

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
