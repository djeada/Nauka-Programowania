/*
ZAD-01 — Wczytaj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `I/O`, `odwracanie`

### Treść

Wczytaj `N`, następnie `N` liczb całkowitych do listy.

a) Wypisz elementy listy od początku do końca — każdy w osobnej linii.
b) Wypisz elementy listy od końca do początku — w **jednej** linii, oddzielone przecinkami (bez spacji).

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

a) `N` linii — elementy w kolejności wczytania.
b) 1 linia — elementy w kolejności odwrotnej, oddzielone przecinkami.

### Przykład

**Wejście:**

```
3
8
12
7
```

**Wyjście:**

```
8
12
7
7,12,8
```

### Uwagi o formatowaniu

* W podpunkcie (b) nie dodawaj przecinka na końcu.

*/

// Funkcja wczytujaca N liczb calkowitych do listy
function wczytajNliczbDoListy(N) {
  var lista = [];
  for (var i = 0; i < N; i++) {
    lista.push(parseInt(prompt("Podaj liczbe:")));
  }
  return lista;
}

// Funkcja wypisujaca liste od poczatku do konca
function wypiszListeOdPoczatkuDoKonca(lista) {
  for (var i = 0; i < lista.length; i++) {
    console.log(lista[i]);
  }
}

// Funkcja wypisujaca liste od konca z elementami oddzielonymi przecinkami
function wypiszListeOdKonca(lista) {
  const wynik = [];
  for (let i = lista.length - 1; i >= 0; i--) {
    wynik.push(lista[i]);
  }
  console.log(wynik.join(","));
}

// Pobieranie danych od uzytkownika
const N = parseInt(prompt("Podaj liczbe elementow:"));
const lista = wczytajNliczbDoListy(N);

// Wypisanie listy
wypiszListeOdPoczatkuDoKonca(lista);
wypiszListeOdKonca(lista);

