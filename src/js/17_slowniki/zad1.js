/*
Otrzymujesz liczbe naturalna. Zbuduj slownik skladajacy sie
z kluczy bedacych kolejnymi liczbami naturalnymi mniejszymi
od otrzymanej liczby oraz wartosci bedacych kwadratami
odpowiadajacych im kluczy.
*/

budujSlownik = function (n) {
  var slownik = {};
  for (var i = 1; i <= n; i++) {
    slownik[i] = i * i;
  }
  return slownik;
};

test1 = function () {
  var liczba = 5;
  var oczekiwane = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
  };
  var wynik = budujSlownik(liczba);
  if (oczekiwane.length !== wynik.length) {
    throw new Error(
      `Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`
    );
  }

  for (const key in oczekiwane) {
    if (oczekiwane[key] !== wynik[key]) {
      throw new Error(
        `Assertion error line 34: ${wynik[key]} != ${oczekiwane[key]}`
      );
    }
  }
};

test2 = function () {
  var liczba = -1;
  var oczekiwane = {};
  var wynik = budujSlownik(liczba);
  if (oczekiwane.length !== wynik.length) {
    throw new Error(
      `Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`
    );
  }

  for (const key in oczekiwane) {
    if (oczekiwane[key] !== wynik[key]) {
      throw new Error(
        `Assertion error line 34: ${wynik[key]} != ${oczekiwane[key]}`
      );
    }
  }
};

main = function () {
  test1();
  test2();
};

main();
