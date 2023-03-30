/*

Tytul: Cyfry w slowach.

Tresc: Dostajesz napis reprezentujacy zdanie. Zapisz w liscie cyfry, ktore sa czescia slow. Cyfry oddzielone od liter spacja powinny zostac pominiete.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla otrzymanego napisu: "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego", powinna zostac zwrocona lista: ["29", "37", "3891", "3"].

*/

function cyfry_w_slowach(napis) {
  const cyfry = /\d+/g;

  return napis.match(cyfry);
}

function test_cyfry_w_slowach() {
  console.assert(
    cyfry_w_slowach(
      "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego"
    ).join("") === "293793389122"
  );
  console.assert(
    cyfry_w_slowach(
      "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego"
    ).join(" ") === "29 37 3891 22"
  );
}

test_cyfry_w_slowach();

