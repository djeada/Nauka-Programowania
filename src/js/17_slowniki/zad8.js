/*


Tytul: Najczesciej wystepujaca litera w zdaniu

Tresc: Otrzymujesz napis reprezentujacy zdanie. Twoim zadaniem jest znalezienie najczesciej wystepujacej litery w zdaniu. Jesli wiecej niz jedna litera wystepuje te sama liczbe razy, nalezy zwrocic litere najwczesniej pojawiajaca sie w zdaniu.

Dane wejsciowe: Napis.

Dane wyjsciowe: Znak.

Przyklad:

Dla otrzymanego napisu: "lezy jerzy na wiezy"

Powinna zostac zwrocona litera: 'e'
*/

function najczestszaLitera(zdanie) {
  const litery = {};
  let maxCzestosc = 0;
  let najczestszaLitera = "";
  for (let i = 0; i < zdanie.length; i++) {
    const litera = zdanie[i];
    if (litera === " ") {
      continue;
    }
    if (!litery[litera]) {
      litery[litera] = 0;
    }
    litery[litera]++;
    if (litery[litera] > maxCzestosc) {
      maxCzestosc = litery[litera];
      najczestszaLitera = litera;
    }
  }
  return najczestszaLitera;
}

function testNajczestszaLitera() {
  const zdanie1 = "lezy jerzy na wiezy";
  const wynik1 = najczestszaLitera(zdanie1);
  console.assert(wynik1 === "e", "Test 1 nie powiodl sie");

  const zdanie2 = "Ala ma kota";
  const wynik2 = najczestszaLitera(zdanie2);
  console.assert(wynik2 === "a", "Test 2 nie powiodl sie");
}

testNajczestszaLitera();

