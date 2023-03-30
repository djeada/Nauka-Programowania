/*

Tytul: Wyodrebnij cyfry z tekstu.

Tresc: Dostajesz napis. Zwroc napis skladajacy sie z cyfr wystepujacych w tym napisie.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla napisu: “Terminator2001”, powinien zostac zwrocony napis: “2001”.

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

