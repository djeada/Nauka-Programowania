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
  for (var i = 0; i < lista.length; i++) {
    if (i === lista.length - 1) {
      console.log(lista[i]);
    } else {
      console.log(lista[i] + ", ");
    }
  }
}

// Testy
var lista = wczytajNliczbDoListy(3);

console.log("Dodaj 1 do kazdego elementu listy");
wypiszListe(dodajJedynkeDoListy(lista));

console.log("\nPomnoz kazdy element przez jego indeks w liscie");
wypiszListe(pomnozElementyListy(lista));

console.log("\nZastap wszystkie elementy wartoscia pierwszego elementu listy");
wypiszListe(zastapElementyListy(lista));

