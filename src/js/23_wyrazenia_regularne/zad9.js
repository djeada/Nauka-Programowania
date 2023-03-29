/*

Tytuł: Usuń fragment napisu.

Treść: Dostajesz dwa napisy. Pierwszy napis to tekst, a drugi to słowo, które należy usunąć z tekstu. Jeśli w tekście znajduje się słowo do usunięcia, usuń całą część tekstu od słowa do końca. Zwróć zmodyfikowany tekst.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Napis.

Przykład:
Dla podanych napisów:

> Turned it up should no valley cousin he.
  Speaking numerous ask did horrible packages set.
  Ashamed herself has distant can studied mrs.
  Led therefore its middleton perpetual fulfilled provision frankness.
  Small he drawn after among every three no.
  All having but you edward genius though remark one.
  Rooms oh fully taken by worse do.
  Points afraid but may end law lasted.
  Was out laughter raptures returned outweigh.
  Luckily cheered colonel me do we attacks on highest enabled.
  Tried law yet style child.
  Bore of true of no be deal.
  Frequently sufficient in be unaffected.
  The furnished she concluded depending procuring concealed.

oraz słowa "a", powinien zostać zwrócony napis:

> Turned it up should no v
  Spe
  Ash
  Led therefore its middleton perpetu
  Sm
  All h
  Rooms oh fully t
  Points
  W
  Luckily cheered colonel me do we
  Tried l
  Bore of true of no be de
  Frequently sufficient in be un
  The furnished she concluded depending procuring conce.

*/

function usun_fragment(napis, slowo) {
  const wyrazenie = new RegExp(`\\b${slowo}\\b.*`, "g");

  return napis.replace(wyrazenie, "");
}

function test_usun_fragment() {
  console.assert(
    usun_fragment(
      "Turned it up should no valley cousin he. Speaking numerous ask did horrible packages set. Ashamed herself has distant can studied mrs. Led therefore its middleton perpetual fulfilled provision frankness. Small he drawn after among every three no. All having but you edward genius though remark one. Rooms oh fully taken by worse do. Points afraid but may end law lasted. Was out laughter raptures returned outweigh. Luckily cheered colonel me do we attacks on highest enabled. Tried law yet style child. Bore of true of no be deal. Frequently sufficient in be unaffected. The furnished she concluded depending procuring concealed.",
      "a"
    ) ===
      "Turned it up should no v Spe Ash Led therefore its middleton perpetu Sm All h Rooms oh fully t Points W Luckily cheered colonel me do we Tried l Bore of true of no be de Frequently sufficient in be un The furnished she concluded depending procuring conce."
  );
}

test_usun_fragment();
