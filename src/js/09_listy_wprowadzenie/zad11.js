/*
Tytul: Samochody jadace w przeciwnych kierunkach.

Tresc: Otrzymujesz liste zlozona wylacznie z liter 'A' i 'B', ktore odpowiadaja samochodom jadacym odpowiednio na wschod ('A') i zachod ('B'). Policz, ile razy samochody jadace w przeciwnych kierunkach mijaja sie.

Dane wejsciowe: Lista znakow odpowiadajacych samochodom jadacym na wschod ('A') i zachod ('B').

Dane wyjsciowe: Liczba naturalna oznaczajaca liczbe mijajacych sie samochodow.

Przyklad:

Dla otrzymanej listy ['A', 'B', 'A', 'B', 'B'] powinna zostac zwrocona liczba 5.
*/

// Funkcja liczaca ile razy samochody mijaja sie na drodze
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

function testLiczbaMijajacychSieSamochodow() {
  console.assert(
    liczbaMijajacychSieSamochodow(["A", "B", "A", "B", "B"]) === 5
  );
  console.assert(
    liczbaMijajacychSieSamochodow(["A", "A", "A", "B", "B"]) === 6
  );
  console.assert(
    liczbaMijajacychSieSamochodow(["A", "B", "A", "A", "B"]) === 4
  );
  console.assert(
    liczbaMijajacychSieSamochodow(["B", "B", "A", "A", "A"]) === 0
  );
  console.assert(
    liczbaMijajacychSieSamochodow(["A", "A", "A", "A", "A"]) === 0
  );
}

testLiczbaMijajacychSieSamochodow();

