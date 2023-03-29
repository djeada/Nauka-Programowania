/*
Tytuł: Czy słowniki są identyczne?

Otrzymujesz dwa słowniki składające się z par napisów i list liczb całkowitych. Listy są nieuporządkowane. Twoim zadaniem jest sprawdzenie, czy słowniki składają się z tych samych par. Dwie listy uznajemy za identyczne, jeśli zawierają te same elementy, niezależnie od kolejności, w jakiej się one znajdują.

Dane wejściowe: Dwa słowniki par: napis, lista liczb całkowitych.

Dane wyjściowe: Wartość boolowska.

Przykład:

Dla otrzymanych słowników:

{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4]}

Powinna zostać zwrócona wartość logiczna: Prawda.

Dla otrzymanych słowników:

{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4], 'c': [6, 7]}

Powinna zostać zwrócona wartość logiczna: Fałsz.

*/

function czySlownikiSaIdentyczne(slownik1, slownik2) {
  // Sprawdzamy czy liczba par w słownikach jest taka sama
  if (Object.keys(slownik1).length !== Object.keys(slownik2).length) {
    return false;
  }

  // Dla każdej pary w słowniku 1 sprawdzamy czy istnieje równoważna w słowniku 2
  for (const [klucz, wartosci] of Object.entries(slownik1)) {
    if (!Object.prototype.hasOwnProperty.call(slownik2, klucz)) {
      return false;
    }

    // Sprawdzamy czy listy są identyczne niezależnie od kolejności
    const lista1 = wartosci.sort();
    const lista2 = slownik2[klucz].sort();
    if (
      lista1.length !== lista2.length ||
      !lista1.every((el, i) => el === lista2[i])
    ) {
      return false;
    }
  }

  return true;
}

// test
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Asercja nie powiodła się");
  }
}

function testCzySlownikiSaIdentyczne() {
  const slownik1 = {
    a: [1, 2, 3],
    b: [4, 5],
  };
  const slownik2 = {
    a: [3, 2, 1],
    b: [5, 4],
  };
  const wynik1 = czySlownikiSaIdentyczne(slownik1, slownik2);
  assert(wynik1 === true, "Błąd testu 1");

  const slownik3 = {
    a: [1, 2, 3],
    b: [4, 5],
  };
  const slownik4 = {
    a: [3, 2, 1],
    b: [5, 4],
    c: [6, 7],
  };
  const wynik2 = czySlownikiSaIdentyczne(slownik3, slownik4);
  assert(wynik2 === false, "Błąd testu 2");
}

testCzySlownikiSaIdentyczne();
