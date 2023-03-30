/*

Tytul: Sprawdz czy slowo wystepuje w zdaniu.

Tresc: Dostajesz dwa napisy. Sprawdz, czy drugi napis wystepuje w pierwszym jako pojedyncze slowo.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla napisow: “Siala baba mak.” oraz “babcia”, powinna zostac zwrocona wartosc logiczna: Falsz.

*/

function czy_wystepuje_jako_slowo(zdanie, slowo) {
  const wyrazenie = new RegExp(`\\b${slowo}\\b`);

  return wyrazenie.test(zdanie);
}

function test_czy_wystepuje_jako_slowo() {
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", "babcia") === false
  );
  console.assert(czy_wystepuje_jako_slowo("Siala baba mak.", "baba") === true);
  console.assert(czy_wystepuje_jako_slowo("Siala baba mak.", "Siala") === true);
  console.assert(czy_wystepuje_jako_slowo("Siala baba mak.", "mak.") === true);
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", "Siala baba mak.") === true
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", "Siala baba mak") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", "Siala baba mak. ") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", " Siala baba mak.") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", " Siala baba mak. ") === false
  );
}

test_czy_wystepuje_jako_slowo();

