/*
ZAD-02 — Wczytaj, zmodyfikuj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `modyfikacja`

### Treść

Wczytaj `N` oraz `N` liczb całkowitych do listy. Następnie:

a) Zwiększ każdy element o `1`.
b) Pomnóż każdy element przez jego indeks (indeksy od `0`).
c) Zastąp wszystkie elementy wartością pierwszego elementu.

Po każdym podpunkcie wypisz wynikową listę w **jednej** linii, elementy oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Trzy linie:

1. wynik po (a)
2. wynik po (b)
3. wynik po (c)

Elementy w linii oddzielone przecinkami (bez spacji).

### Przykład

**Wejście:**

```
3
3
9
7
```

**Wyjście:**

```
4,10,8
0,9,14
3,3,3
```

*/

// Funkcja wczytujaca N liczb calkowitych do listy
function wczytajNliczbDoListy(N) {
  var lista = [];
  for (var i = 0; i < N; i++) {
    lista.push(parseInt(prompt("Podaj liczbe:")));
  }
  return lista;
}

// Funkcja dodajaca 1 do kazdego elementu listy
function dodajJedynkeDoListy(lista) {
  for (var i = 0; i < lista.length; i++) {
    lista[i] += 1;
  }
  return lista;
}

// Funkcja mnozaca kazdy element przez jego indeks w liscie
function pomnozElementyListy(lista) {
  for (var i = 0; i < lista.length; i++) {
    lista[i] *= i;
  }
  return lista;
}

// Funkcja zastepujaca wszystkie elementy wartoscia pierwszego elementu listy
function zastapElementyListy(lista) {
  for (var i = 1; i < lista.length; i++) {
    lista[i] = lista[0];
  }
  return lista;
}

// Funkcja wypisujaca liste z elementami oddzielonymi przecinkami
function wypiszListe(lista) {
  console.log(lista.join(","));
}

// Pobieranie danych od uzytkownika
const N = parseInt(prompt("Podaj liczbe elementow:"));
const lista = wczytajNliczbDoListy(N);

// Zapisz oryginalna pierwsza wartosc
const pierwszaWartosc = lista[0];

// a) Dodaj 1 do kazdego elementu
const listaA = dodajJedynkeDoListy([...lista]);
wypiszListe(listaA);

// b) Pomnoz kazdy element przez jego indeks (na oryginalnej liscie + 1)
const listaB = lista.map(x => x + 1);
const listaB2 = pomnozElementyListy(listaB);
wypiszListe(listaB2);

// c) Zastap wszystkie elementy wartoscia pierwszego elementu (z oryginalnej listy)
const listaC = new Array(N).fill(pierwszaWartosc);
wypiszListe(listaC);

