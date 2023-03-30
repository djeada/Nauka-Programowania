/*

Tytul: Czy napis A jest poczatkiem napisu B?

Tresc: Dostajesz dwa napisy. Twoim zadaniem jest sprawdzenie, czy drugi napis zaczyna sie od pierwszego napisu.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla napisow: “Dinozaur jest zly” oraz “Dino”, zwrocona wartosc powinna byc: Prawda.

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

