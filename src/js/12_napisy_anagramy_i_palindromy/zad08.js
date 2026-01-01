/*
ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

**Poziom:** ★★★
**Tagi:** `substring`, `palindrom`, `unikalność`

### Treść

Wczytaj słowo i znajdź wszystkie **unikalne** palindromy, które można z niego utworzyć jako **spójne podciągi** (substringi), bez zmiany kolejności znaków, spełniające warunek „wyjątkowości”:

1. wszystkie znaki są identyczne (np. `aaa`), **albo**
2. wszystkie znaki poza środkowym są identyczne (np. `cbc`).

Pojedynczy znak też jest wyjątkowym palindromem.

### Wejście

* 1. linia: słowo (litery)

### Wyjście

Każdy unikalny wyjątkowy palindrom w osobnej linii.
Jeśli nic poza pojedynczymi znakami nie pasuje, wypisz tylko te unikalne znaki (po jednej linii na znak).

### Przykład

**Wejście:**

```
xxyxx
```

**Wyjście:**

```
x
xx
xxx
xxyxx
y
yxy
```

### Uwagi o formatowaniu

* Usuń duplikaty w wyniku (np. ten sam palindrom znaleziony w kilku miejscach wypisz raz).
* Kolejność wypisywania może być zgodna z pierwszym pojawieniem się w tekście (łatwe i czytelne): wypisuj przy pierwszym znalezieniu danego palindromu.

*/

// Funkcja sprawdza czy podciąg jest wyjątkowym palindromem
// Złożoność czasowa: O(n), gdzie n to długość podciągu
// Złożoność pamięciowa: O(1)
function czyWyjatkowyPalindrom(podciag) {
  if (podciag.length === 0) return false;
  if (podciag.length === 1) return true;

  const srodek = Math.floor(podciag.length / 2);
  const pierwszyZnak = podciag[0];

  // Sprawdź czy wszystkie znaki poza środkowym są takie same jak pierwszy
  for (let i = 0; i < srodek; i++) {
    if (podciag[i] !== pierwszyZnak) {
      return false;
    }
  }

  for (let i = srodek + (podciag.length % 2); i < podciag.length; i++) {
    if (podciag[i] !== pierwszyZnak) {
      return false;
    }
  }

  return true;
}

// Funkcja znajduje wszystkie unikalne wyjątkowe palindromy w słowie
// Złożoność czasowa: O(n^3), gdzie n to długość słowa
// Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych palindromów
function wyjatkowePalindromy(slowo) {
  const znalezione = new Set();

  // Sprawdź wszystkie podciągi
  for (let i = 0; i < slowo.length; i++) {
    for (let j = i + 1; j <= slowo.length; j++) {
      const podciag = slowo.substring(i, j);
      if (czyWyjatkowyPalindrom(podciag)) {
        znalezione.add(podciag);
      }
    }
  }

  return Array.from(znalezione);
}

// Test
function test() {
  const input = "xxyxx";
  // Uwaga: Poprawiona lista - "xxx" i "yxy" nie istnieją w "xxyxx"
  const expectedOutput = ["x", "xx", "xxyxx", "xyx", "y"];
  const output = wyjatkowePalindromy(input).sort();
  const expected = expectedOutput.sort();

  console.assert(
    JSON.stringify(output) === JSON.stringify(expected),
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expected)
  );
  console.log("Test przeszedl pomyslnie");
}

test();
