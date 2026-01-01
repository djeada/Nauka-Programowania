/*
ZAD-07 — Dodaj wiersz na początku pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `write`, `prepend`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego i wiersz tekstu. Dodaj ten wiersz na **początku** pliku.

### Wejście

* 1 linia: `file_path`
* 2 linia: `line_to_add` (może zawierać spacje)

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\notatki.txt
To jest nowy wiersz dodany na początku pliku.
```

**Wyjście:**
*(brak)*

*/

const fs = require("fs").promises;

const wczytajPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  const wiersze = tekst.split("\n");
  return wiersze;
};

const dostawWierszNaPoczatek = async (sciezka, wiersz) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  const nowyTekst = wiersz + "\n" + tekst;
  await fs.writeFile(sciezka, nowyTekst);
};

const test1 = async () => {
  const sciezka = "temp.txt";
  const tekst = "przykladowy tekst";

  await fs.writeFile(sciezka, tekst);

  await dostawWierszNaPoczatek(sciezka, "Hej");
  const oczekiwane = ["Hej", "przykladowy tekst"];
  const wynik = await wczytajPlik(sciezka);

  console.assert(
    wynik.length === oczekiwane.length,
    `Blad asercji: ${wynik.length} != ${oczekiwane.length}`
  );

  for (let i = 0; i < wynik.length; i++) {
    console.assert(
      wynik[i] === oczekiwane[i],
      `Blad asercji: ${wynik[i]} != ${oczekiwane[i]}`
    );
  }

  await fs.unlink(sciezka);
};

const main = async () => {
  await test1();
};

main();

