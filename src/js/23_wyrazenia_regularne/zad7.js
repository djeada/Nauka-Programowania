/*

Tytuł: Podziel tekst względem znaków interpunkcyjnych.

Treść: Dostajesz napis. Podziel go względem znaków interpunkcyjnych i zapisz w liście. Usuń spacje występujące na początku lub końcu otrzymanych napisów.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla napisu: “Ani nie poszedł do kina, ani nie wybrał się do teatru.”, powinna zostać zwrócona lista: [“Ani nie poszedł do kina”, “ani nie wybrał się do teatru”].

*/

function podziel_tekst(napis) {
  const podziel = /[^.,;:!?]+/g;

  return napis.match(podziel);
}

function test_podziel_tekst() {
  console.assert(
    podziel_tekst(
      "Ani nie poszedł do kina, ani nie wybrał się do teatru."
    ).join("") === "Aninieposzedłdokinaaniniewybrałsiędoteatru"
  );
  console.assert(
    podziel_tekst(
      "Ani nie poszedł do kina, ani nie wybrał się do teatru."
    ).join(" ") === "Ani nie poszedł do kina ani nie wybrał się do teatru"
  );
}

test_podziel_tekst();
