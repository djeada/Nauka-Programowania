/*

Tytul: Obliczenie sredniej wazonej.

Tresc: Otrzymujesz dwie listy liczb zmiennoprzecinkowych. Pierwsza lista reprezentuje wagi, a druga wartosci. Oblicz srednia wazona.

Dane wejsciowe: Dwie listy liczb zmiennoprzecinkowych.

Dane wyjsciowe: Liczba zmiennoprzecinkowa.

Przyklad:

Dla otrzymanych list [2.0, 5.0, 0.0, 2.0, 1.0] oraz [0.2, 0.4, 0.1, 0.2, 0.1] zostanie zwrocona wartosc: 0.29.

*/

function obliczSredniaWazona(wagi, wartosci) {
  var sumaWartosci = 0;
  var sumaWag = 0;
  for (var i = 0; i < wagi.length; i++) {
    sumaWartosci += wagi[i] * wartosci[i];
    sumaWag += wagi[i];
  }
  return sumaWartosci / sumaWag;
}

// Testy

function testObliczSredniaWazona() {
  console.assert(
    obliczSredniaWazona(
      [2.0, 5.0, 0.0, 2.0, 1.0],
      [0.2, 0.4, 0.1, 0.2, 0.1]
    ).toFixed(2) === "0.29"
  );
  console.assert(
    obliczSredniaWazona(
      [2.0, 5.0, 0.0, 2.0, 1.0],
      [0.2, 0.4, 0.1, 0.2, 0.1]
    ).toFixed(2) === "0.29"
  );
}

function main() {
  testObliczSredniaWazona();
}

main();

