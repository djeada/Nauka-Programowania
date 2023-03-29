/*

Tytuł: Czy napis A jest początkiem napisu B?

Treść: Dostajesz dwa napisy. Twoim zadaniem jest sprawdzenie, czy drugi napis zaczyna się od pierwszego napisu.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisów: “Dinozaur jest zly” oraz “Dino”, zwrócona wartość powinna być: Prawda.

*/

function czyPoczatek(napisA, napisB) {
  return napisB.startsWith(napisA);
}

function testCzyPoczatek() {
  const napisA = "Dino";
  const napisB = "Dinozaur jest zly";
  const wynik = true;
  console.assert(czyPoczatek(napisA, napisB) === wynik, "Test nieudany");
}

testCzyPoczatek();
