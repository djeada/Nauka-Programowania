/*
Tytul: Obliczenie sumy wielomianow.

Tresc: Otrzymujesz dwie listy n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$. Oblicz wspolczynniki wielomianu bedacego suma otrzymanych wielomianow.

Dane wejsciowe: Dwie listy liczb naturalnych.

Dane wyjsciowe: Lista liczb naturalnych.

Przyklad:

Dla otrzymanych dwoch list [3, 5, 2] oraz [2, -8, 1], zostanie zwrocona lista [5, -3, 3].
*/

function dodawanieWielomianow(wielomian1, wielomian2) {
  const dlugosc = Math.max(wielomian1.length, wielomian2.length);
  const wynik = [];

  for (let i = 0; i < dlugosc; i++) {
    const wspolczynnik1 = wielomian1[i] || 0;
    const wspolczynnik2 = wielomian2[i] || 0;
    wynik.push(wspolczynnik1 + wspolczynnik2);
  }

  return wynik;
}

// Testy
function testDodawanieWielomianow() {
  let wielomian1;
  let wielomian2;
  let wynik;

  wielomian1 = [3, 5, 2];
  wielomian2 = [2, -8, 1];
  wynik = dodawanieWielomianow(wielomian1, wielomian2);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([5, -3, 3]),
    "Test 1 nieudany"
  );

  wielomian1 = [1, 0, 3];
  wielomian2 = [2, 2, 2];
  wynik = dodawanieWielomianow(wielomian1, wielomian2);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([3, 2, 5]),
    "Test 2 nieudany"
  );

  wielomian1 = [0, 0, 0];
  wielomian2 = [1, 1, 1];
  wynik = dodawanieWielomianow(wielomian1, wielomian2);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([1, 1, 1]),
    "Test 3 nieudany"
  );
}

testDodawanieWielomianow();
console.log("Wszystkie testy zakonczone sukcesem");

