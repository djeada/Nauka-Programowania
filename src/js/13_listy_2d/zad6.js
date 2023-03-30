/*

Tytul: Scalanie przedzialow w liscie przedzialow.

Tresc: Otrzymujesz liste par liczb. Kazda para reprezentuje poczatek i koniec przedzialu. Niektore przedzialy moga sie nachodzic. W takim przypadku polacz je ze soba i zwroc liste przedzialow, ktore sie nie pokrywaja.

Dane wejsciowe: Lista list liczb naturalnych.

Dane wyjsciowe: Lista list liczb naturalnych.

Przyklad:

Dla otrzymanej listy: [[23, 67], [23, 53], [45, 88], [77, 88], [10, 22], [11, 12], [42, 45]], powinna zostac zwrocona lista: [[10, 22], [23, 88]].
*/

function scalPrzedzialy(przedzialy) {
  przedzialy.sort((a, b) => a[0] - b[0]); // sortujemy przedzialy po poczatku

  const wynik = [przedzialy[0]]; // dodajemy pierwszy przedzial
  let ostatniPrzedzial = przedzialy[0];

  for (let i = 1; i < przedzialy.length; i++) {
    const aktualnyPrzedzial = przedzialy[i];
    if (aktualnyPrzedzial[0] <= ostatniPrzedzial[1]) {
      // przedzialy nachodza na siebie
      ostatniPrzedzial[1] = Math.max(ostatniPrzedzial[1], aktualnyPrzedzial[1]); // przedzialy sie nakladaja, laczymy je w jeden
    } else {
      // przedzialy nie nachodza na siebie
      wynik.push(aktualnyPrzedzial); // dodajemy przedzial do wyniku
      ostatniPrzedzial = aktualnyPrzedzial;
    }
  }

  return wynik;
}

// test
function test() {
  const przedzialy1 = [
    [23, 67],
    [23, 53],
    [45, 88],
    [77, 88],
    [10, 22],
    [11, 12],
    [42, 45],
  ];
  const wynik1 = [
    [10, 22],
    [23, 88],
  ];
  const przedzialy2 = [
    [1, 2],
    [3, 4],
    [5, 6],
  ];
  const wynik2 = [
    [1, 2],
    [3, 4],
    [5, 6],
  ];
  const przedzialy3 = [
    [1, 3],
    [2, 4],
    [5, 6],
  ];
  const wynik3 = [
    [1, 4],
    [5, 6],
  ];
  console.assert(
    JSON.stringify(scalPrzedzialy(przedzialy1)) === JSON.stringify(wynik1),
    `Niepoprawny wynik dla przedzialow ${przedzialy1}.`
  );
  console.assert(
    JSON.stringify(scalPrzedzialy(przedzialy2)) === JSON.stringify(wynik2),
    `Niepoprawny wynik dla przedzialow ${przedzialy2}.`
  );
  console.assert(
    JSON.stringify(scalPrzedzialy(przedzialy3)) === JSON.stringify(wynik3),
    `Niepoprawny wynik dla przedzialow ${przedzialy3}.`
  );
}

test();

