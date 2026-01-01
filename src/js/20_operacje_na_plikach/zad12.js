/*
ZAD-12 — Przenieś wszystkie pliki CSV do jednego folderu (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `move`, `csv`, `recursive`

### Treść

Otrzymujesz ścieżkę folderu źródłowego i docelowego. Przenieś wszystkie pliki `.csv` z folderu źródłowego **i wszystkich jego podfolderów** do folderu docelowego.

### Wejście

* 1 linia: `src_folder`
* 2 linia: `dst_folder`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Projekty
D:\Dane\CSV
```

**Wyjście:**
*(brak)*

### Uwagi

* Jeśli w folderze docelowym istnieje już plik o tej samej nazwie, zadanie wymaga zdefiniowania zachowania (np. zmiana nazwy / pominięcie) — jeśli sprawdzarka tego nie doprecyzowuje, przyjmij jedną spójną strategię w całym rozwiązaniu.

*/

const fs = require("fs").promises;
const path = require("path");

const przeniesPliki = async (zrodlo, cel, rozszerzenie) => {
  const dane = await fs.readdir(zrodlo);
  const pliki = dane.filter((plik) => plik.endsWith(rozszerzenie));
  for (const plik of pliki) {
    const sciezkaPliku = path.join(zrodlo, plik);
    const sciezkaDocelowa = path.join(cel, plik);
    await fs.copyFile(sciezkaPliku, sciezkaDocelowa);
    await fs.unlink(sciezkaPliku);
  }
};

const test1 = async () => {
  const folder1 = "temp_dir1";
  const folder2 = "temp_dir2";

  await fs.mkdir(folder1);
  await fs.mkdir(folder2);

  const sciezkaPliku1 = path.join(folder1, "plik1.csv");
  const sciezkaPliku2 = path.join(folder1, "plik2.csv");

  const sciezki = [sciezkaPliku1, sciezkaPliku2];

  for (const sciezkaPliku of sciezki) {
    await fs.writeFile(sciezkaPliku, "test1; test2");
  }

  await przeniesPliki(folder1, folder2, ".csv");

  const nowaSciezkaPliku1 = path.join(folder2, "plik1.csv");
  const nowaSciezkaPliku2 = path.join(folder2, "plik2.csv");

  const noweSciezki = [nowaSciezkaPliku1, nowaSciezkaPliku2];

  for (const nowaSciezkaPliku of noweSciezki) {
    const stat = await fs.lstat(nowaSciezkaPliku);
    console.assert(
      stat.isFile(),
      `Blad asercji: ${nowaSciezkaPliku} nie istnieje`
    );
  }

  for (const sciezkaPliku of sciezki) {
    try {
      await fs.access(sciezkaPliku);
      throw new Error(`Blad asercji: ${sciezkaPliku} istnieje`);
    } catch (err) {
      if (err.code !== "ENOENT") {
        throw err;
      }
    }
  }

  await fs.rm(folder1, {
    recursive: true,
  });
  await fs.rm(folder2, {
    recursive: true,
  });
};

const main = async () => {
  await test1();
};

main();

