/*

Tytul: Zmodyfikuj elementy spelniajace warunek.

Tresc: Otrzymujesz liste liczb calkowitych. W wyniku wykonania ponizszych polecen otrzymasz nowa liste:

a) Zwieksz o 1 wszystkie elementy o parzystych indeksach (indeksy zaczynaja sie od 0).

b) Wyzeruj wszystkie elementy bedace wielokrotnosciami liczby 3.

c) Podnies do kwadratu wszystkie elementy mniejsze niz 10.

d) Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.

e) Zamien kazdy element na iloczyn wszystkich elementow listy poza nim samym.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Lista liczb calkowitych.

Przyklad:

Dla otrzymanej listy [5, 7, 9, 4, 2]:

a) Wynik: [5, 8, 9, 5, 2]

b) Wynik: [5, 0, 0, 5, 2]

c) Wynik: [25, 0, 0, 25, 4]

d) Wynik: [37, 0, 0, 25, 4]

e) Wynik: [2592, 0, 0, 36, 1080]
*/
// a) Zwieksz o 1 wszystkie elementy o parzystych indeksach (indeksy zaczynaja sie od 0).
function zwiekszElementyOParzystychIndeksach(lista) {
  return lista.map((element, indeks) => {
    if (indeks % 2 === 0) {
      return element + 1;
    }
    return element;
  });
}

// b) Wyzeruj wszystkie elementy bedace wielokrotnosciami liczby 3.
function wyzerujWielokrotnosciLiczby3(lista) {
  return lista.map((element) => {
    if (element % 3 === 0) {
      return 0;
    }
    return element;
  });
}

// c) Podnies do kwadratu wszystkie elementy mniejsze niz 10.
function podniesDoKwadratuMniejszeNiz10(lista) {
  return lista.map((element) => {
    if (element < 10) {
      return element * element;
    }
    return element;
  });
}

// d) Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
function wstawSumaNaIndeksyPierwsze(lista) {
  return lista.map((element, indeks) => {
    if (czyLiczbaJestPierwsza(indeks)) {
      return sumaListy(lista);
    }
    return element;
  });
}

// e) Zamien kazdy element na iloczyn wszystkich elementow listy poza nim samym.
function zamienNaIloczynPozaNimSamym(lista) {
  return lista.map((element) => {
    return iloczynListyBezElementu(lista, element);
  });
}

// Funkcje pomocnicze
function sumaListy(lista) {
  return lista.reduce((suma, element) => suma + element, 0);
}

function iloczynListyBezElementu(lista, element) {
  return lista.reduce((iloczyn, elementListy) => {
    if (elementListy !== element) {
      return iloczyn * elementListy;
    }
    return iloczyn;
  }, 1);
}

function czyLiczbaJestPierwsza(liczba) {
  if (liczba < 2) {
    return false;
  }
  for (let i = 2; i < liczba; i++) {
    if (liczba % i === 0) {
      return false;
    }
  }
  return true;
}

// Testy

function testZwiekszElementyOParzystychIndeksach() {
  const lista = [5, 7, 9, 4, 2];
  const wynik = [6, 7, 10, 4, 3];
  console.assert(
    JSON.stringify(zwiekszElementyOParzystychIndeksach(lista)) ===
      JSON.stringify(wynik),
    "Zwiekszanie elementow o parzystych indeksach nie dziala."
  );
}

function testWyzerujWielokrotnosciLiczby3() {
  const lista = [5, 7, 9, 4, 2];
  const wynik = [5, 7, 0, 4, 2];
  console.assert(
    JSON.stringify(wyzerujWielokrotnosciLiczby3(lista)) ===
      JSON.stringify(wynik),
    "Wyzerowywanie wielokrotnosci liczby 3 nie dziala."
  );
}

function testPodniesDoKwadratuMniejszeNiz10() {
  const lista = [5, 7, 9, 4, 2];
  const wynik = [25, 7, 81, 16, 4];
  console.assert(
    JSON.stringify(podniesDoKwadratuMniejszeNiz10(lista)) ===
      JSON.stringify(wynik),
    "Podnoszenie do kwadratu elementow mniejszych niz 10 nie dziala."
  );
}

function testWstawSumaNaIndeksyPierwsze() {
  const lista = [5, 7, 9, 4, 2];
  const wynik = [29, 7, 9, 29, 2];
  console.assert(
    JSON.stringify(wstawSumaNaIndeksyPierwsze(lista)) === JSON.stringify(wynik),
    "Wstawianie sumy na indeksy pierwsze nie dziala."
  );
}

function testZamienNaIloczynPozaNimSamym() {
  const lista = [5, 7, 9, 4, 2];
  const wynik = [504, 360, 280, 567, 945];
  console.assert(
    JSON.stringify(zamienNaIloczynPozaNimSamym(lista)) ===
      JSON.stringify(wynik),
    "Zamiana na iloczyn poza nim samym nie dziala."
  );
}

testZwiekszElementyOParzystychIndeksach();
testWyzerujWielokrotnosciLiczby3();
testPodniesDoKwadratuMniejszeNiz10();
testWstawSumaNaIndeksyPierwsze();
testZamienNaIloczynPozaNimSamym();

