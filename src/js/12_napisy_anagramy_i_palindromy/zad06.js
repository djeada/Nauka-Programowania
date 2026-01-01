/*
ZAD-06 — Permutacje słowa, które są palindromami

**Poziom:** ★★☆
**Tagi:** `palindrom`, `permutacje`, `multiset`

### Treść

Wczytaj słowo i wypisz wszystkie **unikalne** palindromy, które są jego permutacjami.

### Wejście

* 1. linia: słowo (litery mogą się powtarzać)

### Wyjście

Każdy unikalny palindrom w osobnej linii. Jeśli nie istnieje żaden — puste wyjście.

### Przykład

**Wejście:**

```
aabb
```

**Wyjście:**

```
abba
baab
```

### Uwagi

* Najpierw sprawdź warunek istnienia palindromu z liter: co najwyżej jeden znak może mieć nieparzystą liczbę wystąpień.
* Generuj palindromy z połówek (bez wypisywania duplikatów).

*/

// Funkcja sprawdza czy można utworzyć palindrom z liter słowa
// Złożoność czasowa: O(n), gdzie n to długość słowa
// Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych znaków
function moznaUtworzyPalindrom(slowo) {
  const licznikZnakow = {};

  for (const znak of slowo) {
    licznikZnakow[znak] = (licznikZnakow[znak] || 0) + 1;
  }

  let nieparzysteLiczniki = 0;
  for (const licznik of Object.values(licznikZnakow)) {
    if (licznik % 2 !== 0) {
      nieparzysteLiczniki++;
    }
  }

  // Palindrom można utworzyć gdy max 1 znak ma nieparzystą liczbę wystąpień
  return nieparzysteLiczniki <= 1;
}

// Funkcja generuje palindromy z liter słowa
// Złożoność czasowa: O(n!), gdzie n to długość słowa (przez permutacje)
// Złożoność pamięciowa: O(n!)
function generujPalindromy(slowo) {
  if (!moznaUtworzyPalindrom(slowo)) {
    return [];
  }

  const licznikZnakow = {};
  for (const znak of slowo) {
    licznikZnakow[znak] = (licznikZnakow[znak] || 0) + 1;
  }

  // Znajdź znak środkowy (jeśli istnieje)
  let srodek = "";
  for (const [znak, licznik] of Object.entries(licznikZnakow)) {
    if (licznik % 2 !== 0) {
      srodek = znak;
      licznikZnakow[znak]--;
      break;
    }
  }

  // Buduj połówkę palindromu
  const polowka = [];
  for (const [znak, licznik] of Object.entries(licznikZnakow)) {
    for (let i = 0; i < licznik / 2; i++) {
      polowka.push(znak);
    }
  }

  // Generuj unikalne permutacje połówki
  const permutacjePolowki = generujUnikalnePermutacje(polowka);
  const wynik = [];

  for (const perm of permutacjePolowki) {
    const permString = perm.join("");
    const palindrom =
      permString + srodek + permString.split("").reverse().join("");
    wynik.push(palindrom);
  }

  return wynik;
}

// Funkcja generuje unikalne permutacje tablicy
// Złożoność czasowa: O(n!), gdzie n to długość tablicy
// Złożoność pamięciowa: O(n!)
function generujUnikalnePermutacje(tablica) {
  if (tablica.length === 0) return [[]];
  if (tablica.length === 1) return [[tablica[0]]];

  const wynik = [];
  const uzyte = new Set();

  for (let i = 0; i < tablica.length; i++) {
    if (uzyte.has(tablica[i])) continue;
    uzyte.add(tablica[i]);

    const pozostale = tablica.slice(0, i).concat(tablica.slice(i + 1));
    const permutacjePozostałych = generujUnikalnePermutacje(pozostale);

    for (const perm of permutacjePozostałych) {
      wynik.push([tablica[i]].concat(perm));
    }
  }

  return wynik;
}

// Test
function test() {
  const input = "aabb";
  const expectedOutput = ["abba", "baab"];
  const output = generujPalindromy(input).sort();
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
