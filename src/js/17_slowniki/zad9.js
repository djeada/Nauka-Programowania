/*
Otrzymujesz napis. Znajdz w otrzymanym napisie wszystkie znaki
powtarzajace sie wiecej niz raz.
*/

budujSlownik = function (napis) {
  histogram = {};
  for (const znak of napis) {
    if (histogram[znak] === undefined) {
      histogram[znak] = 1;
    } else {
      histogram[znak]++;
    }
  }
  return histogram;
};

znakiPowtarzajaceSieWiecejNizRaz = function (napis) {
  histogram = budujSlownik(napis);
  wynik = [];
  for (const znak in histogram) {
    if (histogram[znak] > 1) {
      wynik.push(znak);
    }
  }
  return wynik;
};

test1 = function () {
  var slowo = "podwodny";
  var oczekiwane = ["o", "d"];
  var wynik = znakiPowtarzajaceSieWiecejNizRaz(slowo);
  if (!(wynik.length == oczekiwane.length)) {
    throw new Error(
      `Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`
    );
  }
  for (var i = 0; i < wynik.length; i++) {
    if (
      !(
        wynik[i].first == oczekiwane[i].first &&
        wynik[i].second == oczekiwane[i].second
      )
    ) {
      throw new Error(
        `Assertion error line 38: ${wynik[i].first} != ${oczekiwane[i].first} || ${wynik[i].second} != ${oczekiwane[i].second}`
      );
    }
  }
};

test2 = function () {
  var slowo = "jedzie pociag z daleka";
  var oczekiwane = ["e", "a", "i", "d", "z", " "];
  var wynik = znakiPowtarzajaceSieWiecejNizRaz(slowo);
  if (!(wynik.length == oczekiwane.length)) {
    throw new Error(
      `Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`
    );
  }
  for (var i = 0; i < wynik.length; i++) {
    if (
      !(
        wynik[i].first == oczekiwane[i].first &&
        wynik[i].second == oczekiwane[i].second
      )
    ) {
      throw new Error(
        `Assertion error line 38: ${wynik[i].first} != ${oczekiwane[i].first} || ${wynik[i].second} != ${oczekiwane[i].second}`
      );
    }
  }
};

main = function () {
  test1();
  test2();
};

main();
