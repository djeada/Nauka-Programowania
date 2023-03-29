/*

Tytuł: Scalanie przedziałów w liście przedziałów.

Treść: Otrzymujesz listę par liczb. Każda para reprezentuje początek i koniec przedziału. Niektóre przedziały mogą się nachodzić. W takim przypadku połącz je ze sobą i zwróć listę przedziałów, które się nie pokrywają.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej listy: [[23, 67], [23, 53], [45, 88], [77, 88], [10, 22], [11, 12], [42, 45]], powinna zostać zwrócona lista: [[10, 22], [23, 88]].
*/

function scalPrzedzialy(przedzialy) {
  przedzialy.sort((a, b) => a[0] - b[0]); // sortujemy przedziały po początku

  const wynik = [przedzialy[0]]; // dodajemy pierwszy przedział
  let ostatniPrzedzial = przedzialy[0];

  for (let i = 1; i < przedzialy.length; i++) {
    const aktualnyPrzedzial = przedzialy[i];
    if (aktualnyPrzedzial[0] <= ostatniPrzedzial[1]) {
      // przedziały nachodzą na siebie
      ostatniPrzedzial[1] = Math.max(ostatniPrzedzial[1], aktualnyPrzedzial[1]); // przedziały się nakładają, łączymy je w jeden
    } else {
      // przedziały nie nachodzą na siebie
      wynik.push(aktualnyPrzedzial); // dodajemy przedział do wyniku
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
  assert(
    JSON.stringify(scalPrzedzialy(przedzialy1)) === JSON.stringify(wynik1),
    `Niepoprawny wynik dla przedziałów ${przedzialy1}.`
  );
  assert(
    JSON.stringify(scalPrzedzialy(przedzialy2)) === JSON.stringify(wynik2),
    `Niepoprawny wynik dla przedziałów ${przedzialy2}.`
  );
  assert(
    JSON.stringify(scalPrzedzialy(przedzialy3)) === JSON.stringify(wynik3),
    `Niepoprawny wynik dla przedziałów ${przedzialy3}.`
  );
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}
test();
