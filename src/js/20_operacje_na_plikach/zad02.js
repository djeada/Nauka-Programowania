/*
ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez przeszukiwania podfolderów). Zwróć listę nazw plików.

### Wejście

* 1 linia: `folder_path`
* 2 linia: `ext` (np. `.txt`)

### Wyjście

* 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents
.txt
```

**Wyjście:**

```
['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
```

### Uwagi o formatowaniu

* Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje do `.txt`).

*/

const fs = require("fs").promises;
const path = require("path");

const znajdzPliki = async (sciezka, rozszerzenie) => {
  const pliki = [];
  const dane = await fs.readdir(sciezka);
  for (const danePliku of dane) {
    const sciezkaPliku = path.join(sciezka, danePliku);
    const stat = await fs.lstat(sciezkaPliku);
    if (stat.isFile() && path.extname(danePliku) === rozszerzenie) {
      pliki.push(danePliku);
    }
  }
  return pliki;
};

const testZnajdzPliki = async () => {
  const sciezkaFolderu = "temp_dir";
  const sciezkiPlikow = ["lista.txt", "test.txt"];
  const tekst = "przykladowy tekst.\n";

  await fs.mkdir(sciezkaFolderu);

  for (const plik of sciezkiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    await fs.writeFile(sciezkaPliku, tekst);
  }

  const oczekiwane = sciezkiPlikow;
  const wynik = await znajdzPliki(sciezkaFolderu, ".txt");

  console.assert(
    wynik.length === oczekiwane.length,
    `Blad testu znajdzPliki: ${wynik.length} !== ${oczekiwane.length}`
  );

  for (const nazwaPliku of oczekiwane) {
    console.assert(
      wynik.includes(nazwaPliku),
      `Blad testu znajdzPliki: ${wynik} nie zawiera ${nazwaPliku}`
    );
  }

  await fs.rmdir(sciezkaFolderu, {
    recursive: true,
  });
};

const main = async () => {
  await testZnajdzPliki();
};

main();

