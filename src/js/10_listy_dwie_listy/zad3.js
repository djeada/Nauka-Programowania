/*
Tytuł: Suma elementów dwóch list.

Treść: Dla otrzymanych dwóch list, zwróć listę, której elementy są sumą odpowiadających sobie elementów obu list. Jeśli listy nie są tej samej długości, załóż, że brakujące elementy krótszej listy są równe 0.

Dane wejściowe: Dwie listy.

Dane wyjściowe: Lista.

Przykład:

Dla otrzymanych list [3, 1, 2, 5] oraz [2, 8, 6, 5], zostanie zwrócona lista: [5, 9, 8, 10].
*/

// Funkcja zwracająca listę, której elementy są sumą odpowiadających sobie elementów obu list
function sumaElementowList(lista1, lista2) {
  let wynik = [];
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    let element1 = lista1[i] || 0;
    let element2 = lista2[i] || 0;
    wynik.push(element1 + element2);
  }

  return wynik;
}

// Testy

function testSumaElementowList() {
  console.assert(
    sumaElementowList([3, 1, 2, 5], [2, 8, 6, 5]).toString() ===
      [5, 9, 8, 10].toString()
  );
  console.assert(
    sumaElementowList([3, 1, 2, 5], [2, 8, 6]).toString() ===
      [5, 9, 8, 5].toString()
  );
  console.assert(
    sumaElementowList([3, 1, 2], [2, 8, 6, 5]).toString() ===
      [5, 9, 8, 5].toString()
  );
  console.assert(
    sumaElementowList([3, 1, 2, 5], [2, 8, 6, 5, 1]).toString() ===
      [5, 9, 8, 10, 1].toString()
  );
}

testSumaElementowList();
