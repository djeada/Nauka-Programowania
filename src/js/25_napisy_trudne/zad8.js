/*

Tytuł: Najdłuższy wspólny przedrostek.

Treść: Dostajesz listę napisów. Znajdź najdłuższy wspólny przedrostek dla wszystkich napisów na liście.

Dane wejściowe: Lista napisów.

Dane wyjściowe: Napis.

Przykład:

Dla listy ["Remolada", "Remux", "Remmy"] powinien zostać zwrócony napis "Rem".

*/

function najdluzszyWspolnyPrzedrostek(listaNapisow) {
  if (listaNapisow.length === 0) {
    return "";
  }

  let przedrostek = listaNapisow[0];

  for (let i = 1; i < listaNapisow.length; i++) {
    while (listaNapisow[i].indexOf(przedrostek) !== 0) {
      przedrostek = przedrostek.substring(0, przedrostek.length - 1);
      if (przedrostek === "") {
        return "";
      }
    }
  }

  return przedrostek;
}

function testNajdluzszyWspolnyPrzedrostek() {
  const lista1 = ["Remolada", "Remux", "Remmy"];
  const wynik1 = "Rem";
  const lista2 = ["piesek", "kotek", "myszka"];
  const wynik2 = "";

  console.assert(
    najdluzszyWspolnyPrzedrostek(lista1) === wynik1,
    "Test 1 nieudany"
  );
  console.assert(
    najdluzszyWspolnyPrzedrostek(lista2) === wynik2,
    "Test 2 nieudany"
  );
}

testNajdluzszyWspolnyPrzedrostek();
