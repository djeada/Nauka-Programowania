/*

Tytuł: Wyodrębnij cyfry z tekstu.

Treść: Dostajesz napis. Zwróć napis składający się z cyfr występujących w tym napisie.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla napisu: “Terminator2001”, powinien zostać zwrócony napis: “2001”.

*/

function wyodrebnij_cyfry(napis) {
  const cyfry = /[0-9]+/g;

  return napis.match(cyfry).join("");
}

function test_wyodrebnij_cyfry() {
  console.assert(wyodrebnij_cyfry("Terminator2001") === "2001");
  console.assert(wyodrebnij_cyfry("Terminator 2001") === "2001");
  console.assert(wyodrebnij_cyfry(" Terminator 2001 ") === "2001");
}

test_wyodrebnij_cyfry();
