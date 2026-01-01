/*
ZAD-01 — Czy ścieżka istnieje?

**Poziom:** ★☆☆
**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Otrzymujesz ścieżkę w systemie plików. Sprawdź, czy odnosi się do istniejącego **pliku lub folderu**.

### Wejście

* 1 linia: `path` (napis — ścieżka)

### Wyjście

* 1 linia: `Prawda` jeśli ścieżka istnieje, w przeciwnym razie `Fałsz`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik.txt
```

**Wyjście:**

```
Prawda
```

*/

const fs = require("fs").promises;

const czyPlik = async (sciezka) => {
  try {
    const stat = await fs.lstat(sciezka);
    return stat.isFile();
  } catch (err) {
    return false;
  }
};

const czyFolder = async (sciezka) => {
  try {
    const stat = await fs.lstat(sciezka);
    return stat.isDirectory();
  } catch (err) {
    return false;
  }
};

const testCzyPlik = async () => {
  const sciezkaPliku = "temp.txt";
  const tekst = "przykladowy tekst.\n";

  await fs.writeFile(sciezkaPliku, tekst);

  const oczekiwane = true;
  const wynik = await czyPlik(sciezkaPliku);

  console.assert(
    wynik === oczekiwane,
    `Blad testu czyPlik: ${wynik} !== ${oczekiwane}`
  );

  const oczekiwane2 = false;
  const wynik2 = await czyFolder(sciezkaPliku);

  console.assert(
    wynik2 === oczekiwane2,
    `Blad testu czyPlik: ${wynik2} !== ${oczekiwane2}`
  );

  await fs.unlink(sciezkaPliku);
};

const testCzyFolder = async () => {
  const sciezkaFolderu = "temp_dir";

  await fs.mkdir(sciezkaFolderu);

  const oczekiwane = false;
  const wynik = await czyPlik(sciezkaFolderu);

  console.assert(
    wynik === oczekiwane,
    `Blad testu czyFolder: ${wynik} !== ${oczekiwane}`
  );

  const oczekiwane2 = true;
  const wynik2 = await czyFolder(sciezkaFolderu);

  console.assert(
    wynik2 === oczekiwane2,
    `Blad testu czyFolder: ${wynik2} !== ${oczekiwane2}`
  );

  await fs.rmdir(sciezkaFolderu);
};

const main = async () => {
  await testCzyPlik();
  await testCzyFolder();
};

main();

