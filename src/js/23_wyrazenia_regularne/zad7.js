/*

Tytul: Podziel tekst wzgledem znakow interpunkcyjnych.

Tresc: Dostajesz napis. Podziel go wzgledem znakow interpunkcyjnych i zapisz w liscie. Usun spacje wystepujace na poczatku lub koncu otrzymanych napisow.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla napisu: “Ani nie poszedl do kina, ani nie wybral sie do teatru.”, powinna zostac zwrocona lista: [“Ani nie poszedl do kina”, “ani nie wybral sie do teatru”].

*/

function podziel_tekst(napis) {
  const podziel = /[^.,;:!?]+/g;

  return napis.match(podziel);
}

function test_podziel_tekst() {
  console.assert(
    podziel_tekst(
      "Ani nie poszedl do kina, ani nie wybral sie do teatru."
    ).join("") === "Aninieposzedldokinaaniniewybralsiedoteatru"
  );
  console.assert(
    podziel_tekst(
      "Ani nie poszedl do kina, ani nie wybral sie do teatru."
    ).join(" ") === "Ani nie poszedl do kina ani nie wybral sie do teatru"
  );
}

test_podziel_tekst();

