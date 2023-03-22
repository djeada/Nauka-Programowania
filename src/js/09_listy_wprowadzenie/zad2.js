/*
Tytuł: Wczytaj, zmodyfikuj i wypisz.

Treść: Wczytaj liczbę całkowitą N oraz N liczb całkowitych i umieść je w liście. Następnie:

a) Dodaj 1 do każdego elementu listy.

b) Pomnóż każdy element przez jego indeks w liście (indeksy zaczynają się od 0).

c) Zastąp wszystkie elementy wartością pierwszego elementu listy.

Dla każdego z powyższych podpunktów wypisz zmodyfikowaną listę. Elementy listy powinny być oddzielone przecinkami i wypisane w jednym wierszu.

Dane wejściowe: N oraz N liczb całkowitych.

Dane wyjściowe: N liczb całkowitych.

Przykład:

Dla N równego 3 oraz pobranych liczb 3, 9, 7 w pierwszym podpunkcie powinno zostać wypisana: 4, 10, 8.
*/

// Funkcja wczytująca N liczb całkowitych do listy
function wczytajNliczbDoListy(N) {
  var lista = [];
  for (var i = 0; i < N; i++) {
    lista.push(parseInt(prompt("Podaj liczbę:")));
  }
  return lista;
}

// Funkcja dodająca 1 do każdego elementu listy
function dodajJedynkeDoListy(lista) {
  for (var i = 0; i < lista.length; i++) {
    lista[i] += 1;
  }
  return lista;
}

// Funkcja mnożąca każdy element przez jego indeks w liście
function pomnozElementyListy(lista) {
  for (var i = 0; i < lista.length; i++) {
    lista[i] *= i;
  }
  return lista;
}

// Funkcja zastępująca wszystkie elementy wartością pierwszego elementu listy
function zastapElementyListy(lista) {
  for (var i = 1; i < lista.length; i++) {
    lista[i] = lista[0];
  }
  return lista;
}

// Funkcja wypisująca listę z elementami oddzielonymi przecinkami
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

console.log("Dodaj 1 do każdego elementu listy");
wypiszListe(dodajJedynkeDoListy(lista));

console.log("\nPomnóż każdy element przez jego indeks w liście");
wypiszListe(pomnozElementyListy(lista));

console.log("\nZastąp wszystkie elementy wartością pierwszego elementu listy");
wypiszListe(zastapElementyListy(lista));
