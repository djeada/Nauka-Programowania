/*

Tytuł: Cyfry w słowach.

Treść: Dostajesz napis reprezentujący zdanie. Zapisz w liście cyfry, które są częścią słów. Cyfry oddzielone od liter spacją powinny zostać pominięte.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: "Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego", powinna zostać zwrócona lista: ["29", "37", "3891", "3"].

*/

function cyfry_w_slowach(napis) {
  const cyfry = /\d+/g;

  return napis.match(cyfry);
}

function test_cyfry_w_slowach() {
  console.assert(
    cyfry_w_slowach(
      "Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego"
    ).join("") === "293793389122"
  );
  console.assert(
    cyfry_w_slowach(
      "Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego"
    ).join(" ") === "29 37 3891 22"
  );
}

test_cyfry_w_slowach();
