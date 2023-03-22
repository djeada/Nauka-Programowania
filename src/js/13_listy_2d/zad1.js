/*
Tytuł: Macierz z identycznymi wierszami, składającymi się z liczb od 0 do b.

Treść: Otrzymujesz dwie liczby naturalne, a i b. Stwórz macierz, składającą się z a identycznych wierszy, które składają się z liczb od 0 do b.

Dane wejściowe: Dwie liczby naturalne, a i b.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanych liczb: 3 i 2, powinna zostać zwrócona macierz: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
*/

function utworzMacierz(a, b) {
  const macierz = [];
  for (let i = 0; i < a; i++) {
    const wiersz = [];
    for (let j = 0; j <= b; j++) {
      wiersz.push(j);
    }
    macierz.push(wiersz);
  }
  return macierz;
}

// test
function test() {
  const oczekiwana = [
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2],
  ];
  const wynik = utworzMacierz(3, 2);
  assert(
    wynik.length === oczekiwana.length,
    `Długości macierzy nie są równe. Oczekiwano: ${oczekiwana.length}, otrzymano: ${wynik.length}.`
  );
  for (let i = 0; i < wynik.length; i++) {
    assert(
      wynik[i].length === oczekiwana[i].length,
      `Długości wierszy nie są równe. Oczekiwano: ${oczekiwana[i].length}, otrzymano: ${wynik[i].length}.`
    );
    for (let j = 0; j < wynik[i].length; j++) {
      assert(
        wynik[i][j] === oczekiwana[i][j],
        `Element macierzy o indeksie (${i}, ${j}) nie jest taki sam jak w oczekiwanej macierzy. Oczekiwano: ${oczekiwana[i][j]}, otrzymano: ${wynik[i][j]}.`
      );
    }
  }
}
function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}
test();
