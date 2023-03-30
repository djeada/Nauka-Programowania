/*
Tytul: Wczytaj i wypisz.

Tresc: Dla podanej liczby naturalnej N, wczytaj N liczb calkowitych do listy, a nastepnie:

a) Wypisz liste od poczatku do konca, z kazdym elementem w osobnym wierszu.

b) Wypisz liste od konca, z elementami oddzielonymi przecinkami i wypisanymi w jednym wierszu.

Dane wejsciowe: N liczb calkowitych.

Dane wyjsciowe: N liczb.

Przyklad:

Dla N rownego 3 oraz pobranych liczb: 8, 12, 7, w drugim podpunkcie powinno zostac wypisane: 7, 12, 8.
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
  for (var i = lista.length - 1; i >= 0; i--) {
    if (i === 0) {
      console.log(lista[i]);
    } else {
      console.log(lista[i] + ", ");
    }
  }
}

// Testy
var lista = wczytajNliczbDoListy(3);

console.log("Wypisz liste od poczatku do konca");
wypiszListeOdPoczatkuDoKonca(lista);

console.log("\nWypisz liste od konca");
wypiszListeOdKonca(lista);

