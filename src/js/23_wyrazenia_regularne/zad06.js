/*
ZAD-06 — Wiersze kończące się określonym napisem

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`, `linijki`

### Treść

Otrzymujesz dwa napisy:

1. tekst wielowierszowy,
2. słowo lub fragment.

Znajdź wszystkie wiersze, które kończą się podanym napisem (wiersz może kończyć się znakiem interpunkcyjnym).

### Wejście

Dwie części:

1. Tekst (wiele wierszy)
2. W osobnej linii: `koncowka`

*(Sposób wczytania tekstu wielowierszowego zależy od platformy — przyjmij, że tekst jest podany w całości jako wejście, a ostatnia linia to `koncowka`.)*

### Wyjście

Wiersze spełniające warunek, każdy w osobnej linii, w kolejności występowania.

### Przykład

**Wejście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godności trzeba nie za nic tu cnota,
Miłości pragną nie pragną tu złota.
da
```

**Wyjście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
```

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

