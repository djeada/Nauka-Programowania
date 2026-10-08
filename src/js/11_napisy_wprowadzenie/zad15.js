/*
ZAD-15 — Akronim ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `upper`

### Treść

**Akronim** to skrót utworzony z pierwszych liter kolejnych słów, np. „Polska Akademia Nauk” → `PAN`.

Wczytaj zdanie i wypisz jego akronim: pierwsze znaki wszystkich słów (zgodnie z konwencją rozdziału — bez interpunkcji), zapisane jeden za drugim **wielkimi** literami.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo; może zawierać polskie litery)

### Wyjście

Jedna linia: akronim.

### Przykład

**Wejście:**

```
Polska Akademia Nauk
```

**Wyjście:**

```
PAN
```

### Uwagi

* Słowa mogą być rozdzielone kilkoma spacjami, a zdanie może zaczynać się lub kończyć spacjami — `split()` bez argumentu poradzi sobie z tym.
* Interpunkcja nie należy do słowa: w zdaniu `(Unia Europejska)` słowami są `Unia` i `Europejska`, więc akronim to `UE`. Samotny myślnik `-` nie jest słowem.
* Zamiana na wielką literę dotyczy także polskich liter: `żółta łódź` → `ŻŁ`.

*/
const zdanie = require("fs").readFileSync(0, "utf8").split("\n")[0];

// Znaki interpunkcyjne (jak string.punctuation w Pythonie)
const INTERPUNKCJA = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

function usunInterpunkcje(fragment) {
  let poczatek = 0;
  let koniec = fragment.length;
  while (poczatek < koniec && INTERPUNKCJA.includes(fragment[poczatek])) {
    poczatek++;
  }
  while (koniec > poczatek && INTERPUNKCJA.includes(fragment[koniec - 1])) {
    koniec--;
  }
  return fragment.slice(poczatek, koniec);
}

// Akronim: wielkie pierwsze litery kolejnych słów
function akronim(zdanie) {
  let wynik = "";
  for (const fragment of zdanie.split(/\s+/)) {
    const slowo = usunInterpunkcje(fragment);
    if (slowo.length > 0) {
      wynik += [...slowo][0].toUpperCase();
    }
  }
  return wynik;
}

console.log(akronim(zdanie));
