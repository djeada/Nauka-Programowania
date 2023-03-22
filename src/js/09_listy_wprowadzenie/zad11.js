/*
Tytuł: Samochody jadące w przeciwnych kierunkach.

Treść: Otrzymujesz listę złożoną wyłącznie z liter 'A' i 'B', które odpowiadają samochodom jadącym odpowiednio na wschód ('A') i zachód ('B'). Policz, ile razy samochody jadące w przeciwnych kierunkach mijają się.

Dane wejściowe: Lista znaków odpowiadających samochodom jadącym na wschód ('A') i zachód ('B').

Dane wyjściowe: Liczba naturalna oznaczająca liczbę mijających się samochodów.

Przykład:

Dla otrzymanej listy ['A', 'B', 'A', 'B', 'B'] powinna zostać zwrócona liczba 5.
*/

// Funkcja licząca ile razy samochody mijają się na drodze
function liczbaMijajacychSieSamochodow(listaSamochodow) {
  var samochodyA = 0;
  var liczbaMijajacych = 0;

  for (var i = 0; i < listaSamochodow.length; i++) {
    if (listaSamochodow[i] === "A") {
      samochodyA++;
    } else if (listaSamochodow[i] === "B") {
      liczbaMijajacych += samochodyA;
    }
  }

  return liczbaMijajacych;
}

// Testy
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

function testLiczbaMijajacychSieSamochodow() {
  assert(liczbaMijajacychSieSamochodow(["A", "B", "A", "B", "B"]) === 5);
  assert(liczbaMijajacychSieSamochodow(["A", "A", "A", "B", "B"]) === 6);
  assert(liczbaMijajacychSieSamochodow(["A", "B", "A", "A", "B"]) === 4);
  assert(liczbaMijajacychSieSamochodow(["B", "B", "A", "A", "A"]) === 0);
  assert(liczbaMijajacychSieSamochodow(["A", "A", "A", "A", "A"]) === 0);
}

testLiczbaMijajacychSieSamochodow();
