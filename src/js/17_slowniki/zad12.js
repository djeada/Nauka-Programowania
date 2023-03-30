/*
Tytul: Czy slowniki sa identyczne?

Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych. Listy sa nieuporzadkowane. Twoim zadaniem jest sprawdzenie, czy slowniki skladaja sie z tych samych par. Dwie listy uznajemy za identyczne, jesli zawieraja te same elementy, niezaleznie od kolejnosci, w jakiej sie one znajduja.

Dane wejsciowe: Dwa slowniki par: napis, lista liczb calkowitych.

Dane wyjsciowe: Wartosc boolowska.

Przyklad:

Dla otrzymanych slownikow:

{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4]}

Powinna zostac zwrocona wartosc logiczna: Prawda.

Dla otrzymanych slownikow:

{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4], 'c': [6, 7]}

Powinna zostac zwrocona wartosc logiczna: Falsz.

*/

function czySlownikiSaIdentyczne(slownik1, slownik2) {
  // Sprawdzamy czy liczba par w slownikach jest taka sama
  if (Object.keys(slownik1).length !== Object.keys(slownik2).length) {
    return false;
  }

  // Dla kazdej pary w slowniku 1 sprawdzamy czy istnieje rownowazna w slowniku 2
  for (const [klucz, wartosci] of Object.entries(slownik1)) {
    if (!Object.prototype.hasOwnProperty.call(slownik2, klucz)) {
      return false;
    }

    // Sprawdzamy czy listy sa identyczne niezaleznie od kolejnosci
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
  console.assert(wynik1 === true, "Blad testu 1");

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
  console.assert(wynik2 === false, "Blad testu 2");
}

testCzySlownikiSaIdentyczne();

