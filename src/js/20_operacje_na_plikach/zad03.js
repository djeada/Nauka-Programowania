/*
ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Otrzymujesz nazwę pliku (np. `raport.docx`). Przeszukaj cały system plików i znajdź wszystkie pliki o tej nazwie. Wypisz listę pełnych ścieżek do znalezionych plików.

### Wejście

* 1 linia: `filename` (np. `raport.docx`)

### Wyjście

* 1 linia: lista pełnych ścieżek (napisy)

### Przykład

**Wejście:**

```
raport.docx
```

**Wyjście:**

```
[
  'C:\Users\Username\Documents\raport.docx',
  'D:\Projekty\Raporty\raport.docx',
  'E:\Backup\raport.docx'
]
```

### Uwagi

* W środowisku testowym możesz nie mieć uprawnień do wszystkich katalogów — program powinien to bezpiecznie obsłużyć (np. pomijać niedostępne miejsca).

*/

const fs = require("fs").promises;
const path = require("path");

const znajdzSciezki = async (nazwaPliku) => {
  const sciezki = [];
  const sciezka = process.env.HOME;
  const dane = await fs.readdir(sciezka);
  for (const danePliku of dane) {
    const sciezkaPliku = path.join(sciezka, danePliku);
    const stat = await fs.lstat(sciezkaPliku);
    if (stat.isFile() && danePliku === nazwaPliku) {
      sciezki.push(sciezkaPliku);
    }
  }
  return sciezki;
};

const testZnajdzSciezki = async () => {
  const nazwaPliku = "test.txt";
  const sciezkiPlikow = ["lista.txt", nazwaPliku];
  const tekst = "przykladowy tekst.\n";

  const sciezkaFolderu = "temp_dir";
  await fs.mkdir(sciezkaFolderu);

  for (const plik of sciezkiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    await fs.writeFile(sciezkaPliku, tekst);
  }

  const oczekiwane = [path.join(process.env.HOME, sciezkaFolderu, nazwaPliku)];
  const wynik = await znajdzSciezki(nazwaPliku);

  console.assert(
    wynik.length === oczekiwane.length,
    `Blad testu znajdzSciezki: ${wynik.length} !== ${oczekiwane.length}`
  );

  console.assert(
    wynik.includes(oczekiwane[0]),
    `Blad testu znajdzSciezki: ${wynik} nie zawiera ${oczekiwane[0]}`
  );

  await fs.rmdir(sciezkaFolderu, {
    recursive: true,
  });
};

const main = async () => {
  await testZnajdzSciezki();
};

main();

