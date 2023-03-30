/*

Tytul: Wiersze konczace sie okreslonym napisem.

Tresc: Dostajesz dwa napisy. Znajdz wiersze w pierwszym napisie konczace sie drugim napisem. Wiersz moze byc zakonczony dowolnym znakiem interpunkcyjnym.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla napisow:

> Folgujmy paniom nie sobie, ma rada;
  Milujmy wiernie nie jest w nich przysada.
  Godnosci trzeba nie za nic tu cnota,
  Milosci pragna nie pragna tu zlota.

oraz

> da

powinna zostac zwrocona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy wiernie nie jest w nich przysada.”]

*/

function wiersze_konczace_sie_okreslonym_napisem(tekst, napis) {
  const wyrazenie = new RegExp(`^.*${napis}.*$`, "gm");

  return tekst.match(wyrazenie);
}

function test_wiersze_konczace_sie_okreslonym_napisem() {
  const tekst = `Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragna nie pragna tu zlota.`;

  const oczekiwany_wynik = [
    "Folgujmy paniom nie sobie, ma rada;",
    "Milujmy wiernie nie jest w nich przysada.",
  ];

  console.assert(
    wiersze_konczace_sie_okreslonym_napisem(tekst, "da").join() ===
      oczekiwany_wynik.join()
  );
}

test_wiersze_konczace_sie_okreslonym_napisem();

