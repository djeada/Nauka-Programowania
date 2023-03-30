/*
Tytul: Wczytaj, zmodyfikuj i wypisz.

Tresc: Wczytaj liczbe calkowita N oraz N liczb calkowitych i umiesc je w liscie. Nastepnie:

a) Dodaj 1 do kazdego elementu listy.

b) Pomnoz kazdy element przez jego indeks w liscie (indeksy zaczynaja sie od 0).

c) Zastap wszystkie elementy wartoscia pierwszego elementu listy.

Dla kazdego z powyzszych podpunktow wypisz zmodyfikowana liste. Elementy listy powinny byc oddzielone przecinkami i wypisane w jednym wierszu.

Dane wejsciowe: N oraz N liczb calkowitych.

Dane wyjsciowe: N liczb calkowitych.

Przyklad:

Dla N rownego 3 oraz pobranych liczb 3, 9, 7 w pierwszym podpunkcie powinno zostac wypisana: 4, 10, 8.
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

