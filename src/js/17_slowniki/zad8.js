/*


Tytuł: Najczęściej występująca litera w zdaniu

Treść: Otrzymujesz napis reprezentujący zdanie. Twoim zadaniem jest znalezienie najczęściej występującej litery w zdaniu. Jeśli więcej niż jedna litera występuje tę samą liczbę razy, należy zwrócić literę najwcześniej pojawiającą się w zdaniu.

Dane wejściowe: Napis.

Dane wyjściowe: Znak.

Przykład:

Dla otrzymanego napisu: "lezy jerzy na wiezy"

Powinna zostać zwrócona litera: 'e'
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
  assert(wynik1 === "e", "Test 1 nie powiódł się");

  const zdanie2 = "Ala ma kota";
  const wynik2 = najczestszaLitera(zdanie2);
  assert(wynik2 === "a", "Test 2 nie powiódł się");
}

// test
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Asercja nie powiodła się");
  }
}

testNajczestszaLitera();
