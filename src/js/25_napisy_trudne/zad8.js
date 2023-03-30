/*

Tytul: Najdluzszy wspolny przedrostek.

Tresc: Dostajesz liste napisow. Znajdz najdluzszy wspolny przedrostek dla wszystkich napisow na liscie.

Dane wejsciowe: Lista napisow.

Dane wyjsciowe: Napis.

Przyklad:

Dla listy ["Remolada", "Remux", "Remmy"] powinien zostac zwrocony napis "Rem".

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

