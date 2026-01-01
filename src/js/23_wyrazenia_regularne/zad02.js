/*
ZAD-02 — Sprawdź poprawność hasła

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Otrzymujesz napis reprezentujący hasło. Sprawdź, czy hasło spełnia wszystkie warunki:

1. Zawiera co najmniej jedną małą literę `[a–z]`.
2. Zawiera co najmniej jedną wielką literę `[A–Z]`.
3. Zawiera co najmniej jedną cyfrę `[0–9]`.
4. Zawiera co najmniej jeden znak specjalny spośród:
   `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`.
5. Ma długość co najmniej 8 znaków.
6. Ma długość nie większą niż 20 znaków.

### Wejście

Jedna linia:

* `haslo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
abc1234
```

**Wyjście:**

```
Fałsz
```

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

