/*
Otrzymujesz napis reprezentujacy zdanie. Znajdz najczesciej wystepujaca litere
w zdaniu. Jesli wiecej niz jedna litera wystepuje ta sama liczbe razy, zwroc
litere najwczesniej pojawiajaca sie w zdaniu.
*/

budujSlownik = function (napis) {
  histogram = {};
  for (const znak of napis) {
    if (!znak.match(/[a-z]/i)) continue;
    if (histogram[znak] === undefined) {
      histogram[znak] = 1;
    } else {
      histogram[znak]++;
    }
  }
  return histogram;
};

najczesciejWystepujacaLitera = function (napis) {
  histogram = budujSlownik(napis);
  wynik = undefined;
  max = 0;
  for (const znak in histogram) {
    if (histogram[znak] > max) {
      max = histogram[znak];
      wynik = znak;
    }
  }
  return wynik;
};

test1 = function () {
  napis = "lezy jerzy na wiezy";
  oczekiwane = "e";
  wynik = najczesciejWystepujacaLitera(napis);

  if (oczekiwane !== wynik) {
    throw new Error(
      `Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`
    );
  }
};

test2 = function () {
  napis =
    "The most intelligent people disguise the fact that they " +
    "are intelligent. Wise men do not wear name tags., " +
    "The more people talk about their own skills, the more " +
    "desperate they are--their work should speak for itself.";
  oczekiwane = "e";
  wynik = najczesciejWystepujacaLitera(napis);

  if (oczekiwane !== wynik) {
    throw new Error(
      `Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`
    );
  }
};

main = function () {
  test1();
  test2();
};

main();
