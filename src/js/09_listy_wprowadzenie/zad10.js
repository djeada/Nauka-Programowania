/*
Tytul: Czy punkty moga stanowic wierzcholki trojkata?

Tresc: Otrzymujesz dokladnie 6 liczb calkowitych, ktore odpowiadaja wspolrzednym punktow A, B, C w kolejnosci: xA, yA, xB, yB, xC, yC. Sprawdz, czy punkty A, B, C moga stanowic wierzcholki trojkata.

Dane wejsciowe: Lista liczb calkowitych reprezentujaca wspolrzedne punktow A, B, C.

Dane wyjsciowe: Wartosc logiczna okreslajaca, czy punkty A, B, C moga stanowic wierzcholki trojkata.

Przyklad:

Dla otrzymanej listy [-3, -2, -3, 1, -3, 0], powinna zostac zwrocona wartosc logiczna: Falsz.
*/

// Funkcja sprawdzajaca, czy punkty moga stanowic wierzcholki trojkata
function czyTrojkat(punkty) {
  var xA = punkty[0];
  var yA = punkty[1];
  var xB = punkty[2];
  var yB = punkty[3];
  var xC = punkty[4];
  var yC = punkty[5];

  var AB = Math.sqrt(Math.pow(xB - xA, 2) + Math.pow(yB - yA, 2));
  var BC = Math.sqrt(Math.pow(xC - xB, 2) + Math.pow(yC - yB, 2));
  var AC = Math.sqrt(Math.pow(xC - xA, 2) + Math.pow(yC - yA, 2));

  return AB + BC > AC && AB + AC > BC && BC + AC > AB;
}

// Testy

function testCzyTrojkat() {
  console.assert(czyTrojkat([-3, -2, -3, 1, -3, 0]) === false);
  console.assert(czyTrojkat([0, 0, 3, 0, 0, 4]) === true);
  console.assert(czyTrojkat([0, 0, 0, 0, 0, 0]) === false);
  console.assert(czyTrojkat([1, 2, 2, 2, 3, 2]) === false);
  console.assert(czyTrojkat([0, 0, 5, 0, 0, 5]) === true);
}

testCzyTrojkat();

