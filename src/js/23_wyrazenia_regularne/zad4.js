/*

Tytuł: Sprawdź czy słowo występuje w zdaniu.

Treść: Dostajesz dwa napisy. Sprawdź, czy drugi napis występuje w pierwszym jako pojedyncze słowo.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisów: “Siała baba mak.” oraz “babcia”, powinna zostać zwrócona wartość logiczna: Fałsz.

*/

function czy_wystepuje_jako_slowo(zdanie, slowo) {
  const wyrazenie = new RegExp(`\\b${slowo}\\b`);

  return wyrazenie.test(zdanie);
}

function test_czy_wystepuje_jako_slowo() {
  console.assert(
    czy_wystepuje_jako_slowo("Siała baba mak.", "babcia") === false
  );
  console.assert(czy_wystepuje_jako_slowo("Siała baba mak.", "baba") === true);
  console.assert(czy_wystepuje_jako_slowo("Siała baba mak.", "Siała") === true);
  console.assert(czy_wystepuje_jako_slowo("Siała baba mak.", "mak.") === true);
  console.assert(
    czy_wystepuje_jako_slowo("Siała baba mak.", "Siała baba mak.") === true
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siała baba mak.", "Siała baba mak") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siała baba mak.", "Siała baba mak. ") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siała baba mak.", " Siała baba mak.") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siała baba mak.", " Siała baba mak. ") === false
  );
}

test_czy_wystepuje_jako_slowo();
