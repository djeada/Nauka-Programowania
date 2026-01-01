/*
ZAD-09 — Usuń fragment napisu od pierwszego wystąpienia słowa klucz

**Poziom:** ★★☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz tekst (wiele zdań lub wierszy) oraz słowo klucz. Jeśli słowo klucz wystąpi w tekście, usuń całą część od **pierwszego wystąpienia** tego słowa do końca tekstu. Jeśli słowo klucz nie występuje, wypisz tekst bez zmian.

### Wejście

Dwie części:

1. Tekst (może mieć wiele wierszy)
2. W osobnej linii: `klucz`

### Wyjście

Zmodyfikowany tekst.

### Przykład

*(jak w treści zadania — długi tekst)*

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

