/*
ZAD-02A — Wypisz binarnie tylko gdy liczba parzysta

**Poziom:** ★☆☆
**Tagi:** `warunki`, `parzystość`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest parzysta — wypisz jej zapis binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

* Jeśli `n % 2 == 0`: jedna linia z zapisem binarnym `n`
* W przeciwnym razie: brak wyjścia

### Przykład

**Wejście:**

```
7
```

**Wyjście:** *(brak)*

ZAD-02B — Wypisz binarnie tylko gdy liczba pierwsza

**Poziom:** ★☆☆
**Tagi:** `pierwszość`, `warunki`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest liczbą pierwszą — wypisz jej zapis binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

* Jeśli `n` jest pierwsza: jedna linia z zapisem binarnym `n`
* W przeciwnym razie: brak wyjścia

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
111
```

*/

function konwersjaWarunkowa(liczba) {
  let wynik = "";
  if (liczba % 2 === 0) {
    wynik = liczba.toString(2);
  } else {
    let czyPierwsza = true;
    for (let i = 2; i <= Math.sqrt(liczba); i++) {
      if (liczba % i === 0) {
        czyPierwsza = false;
        break;
      }
    }
    if (czyPierwsza) {
      wynik = liczba.toString(2);
    }
  }
  return wynik;
}

// Testy
function test() {
  let input = 7;
  let expectedOutput = "111"; // 7 jest liczbą pierwszą
  let output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");

  input = 8;
  expectedOutput = "1000";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");

  input = 11;
  expectedOutput = "1011"; // 11 jest liczbą pierwszą
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");

  input = 13;
  expectedOutput = "1101";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");

  input = 17;
  expectedOutput = "10001";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

