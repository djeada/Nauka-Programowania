/*
ZAD-04 — Palindromy w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `tokenizacja`, `palindrom`

### Treść

Wczytaj zdanie i wypisz wszystkie słowa, które są palindromami.
Ignoruj wielkość liter przy sprawdzaniu.

### Wejście

* 1. linia: zdanie (może zawierać spacje i znaki interpunkcyjne)

### Wyjście

Każdy znaleziony palindrom w osobnej linii, w kolejności występowania w zdaniu.

### Przykład

**Wejście:**

```
Tata zabrał kajak na wycieczkę i uderzył się w oko
```

**Wyjście:**

```
Tata
kajak
i
w
oko
```

### Uwagi o formatowaniu

* Traktuj „słowo” jako ciąg liter/cyfr po usunięciu interpunkcji z brzegów (np. `kara.` → `kara`).
* Porównuj w wersji `lower()`, ale wypisz w oryginalnym brzmieniu z wejścia (tak jak w przykładzie).

*/

// Funkcja sprawdza czy słowo jest palindromem (ignorując wielkość liter)
// Złożoność czasowa: O(n), gdzie n to długość słowa
// Złożoność pamięciowa: O(n)
function czyPalindrom(slowo) {
  const slowoMale = slowo.toLowerCase();
  const odwrocone = slowoMale.split("").reverse().join("");
  return slowoMale === odwrocone;
}

// Funkcja znajduje wszystkie palindromy w zdaniu
// Złożoność czasowa: O(n*m), gdzie n to liczba słów, m to średnia długość słowa
// Złożoność pamięciowa: O(k), gdzie k to liczba palindromów
function palindromyWZdaniu(zdanie) {
  const slowa = zdanie.split(/\s+/);
  const palindromy = [];

  for (const slowo of slowa) {
    // Usuń interpunkcję z brzegów
    const czystoSlowo = slowo.replace(/^[^\w]+|[^\w]+$/g, "");
    if (czystoSlowo && czyPalindrom(czystoSlowo)) {
      palindromy.push(slowo.replace(/^[^\w]+|[^\w]+$/g, ""));
    }
  }

  return palindromy;
}

// Test
function test() {
  const input = "Tata zabrał kajak na wycieczkę i uderzył się w oko";
  // Uwaga: "Tata" nie jest palindromem (tata != atat), więc nie powinno być w wyniku
  const expectedOutput = ["kajak", "i", "w", "oko"];
  const output = palindromyWZdaniu(input);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedl pomyslnie");
}

test();
