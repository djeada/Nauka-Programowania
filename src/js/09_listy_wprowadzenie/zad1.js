/*
Tytuł: Wczytaj i wypisz.

Treść: Dla podanej liczby naturalnej N, wczytaj N liczb całkowitych do listy, a następnie:

a) Wypisz listę od początku do końca, z każdym elementem w osobnym wierszu.

b) Wypisz listę od końca, z elementami oddzielonymi przecinkami i wypisanymi w jednym wierszu.

Dane wejściowe: N liczb całkowitych.

Dane wyjściowe: N liczb.

Przykład:

Dla N równego 3 oraz pobranych liczb: 8, 12, 7, w drugim podpunkcie powinno zostać wypisane: 7, 12, 8.
*/

// Funkcja wczytująca N liczb całkowitych do listy
function wczytajNliczbDoListy(N) {
    var lista = [];
    for (var i = 0; i < N; i++) {
        lista.push(parseInt(prompt('Podaj liczbę:')));
    }
    return lista;
}

// Funkcja wypisująca listę od początku do końca
function wypiszListeOdPoczatkuDoKonca(lista) {
    for (var i = 0; i < lista.length; i++) {
        console.log(lista[i]);
    }
}

// Funkcja wypisująca listę od końca z elementami oddzielonymi przecinkami
function wypiszListeOdKonca(lista) {
    for (var i = lista.length - 1; i >= 0; i--) {
        if (i === 0) {
            console.log(lista[i]);
        } else {
            console.log(lista[i] + ', ');
        }
    }
}

// Testy
var lista = wczytajNliczbDoListy(3);

console.log('Wypisz listę od początku do końca');
wypiszListeOdPoczatkuDoKonca(lista);

console.log('\nWypisz listę od końca');
wypiszListeOdKonca(lista);