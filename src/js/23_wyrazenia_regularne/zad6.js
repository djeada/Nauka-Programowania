/*

Tytuł: Wiersze kończące się określonym napisem.

Treść: Dostajesz dwa napisy. Znajdź wiersze w pierwszym napisie kończące się drugim napisem. Wiersz może być zakończony dowolnym znakiem interpunkcyjnym.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Lista napisów.

Przykład:

Dla napisów:

> Folgujmy paniom nie sobie, ma rada;
  Milujmy wiernie nie jest w nich przysada.
  Godności trzeba nie za nic tu cnota,
  Miłości pragną nie pragną tu złota.

oraz

> da

powinna zostać zwrócona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy wiernie nie jest w nich przysada.”]

*/

function wiersze_konczace_sie_okreslonym_napisem(tekst, napis) {
  const wyrazenie = new RegExp(`^.*${napis}.*$`, "gm");

  return tekst.match(wyrazenie);
}

function test_wiersze_konczace_sie_okreslonym_napisem() {
  const tekst = `Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godności trzeba nie za nic tu cnota,
Miłości pragną nie pragną tu złota.`;

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
