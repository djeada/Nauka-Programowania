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

// Funkcja rekurencyjnie przeszukuje katalog w poszukiwaniu plików o podanej nazwie
// Złożoność czasowa: O(n), gdzie n to liczba wszystkich plików i katalogów
// Złożoność pamięciowa: O(d*k), gdzie d to głębokość drzewa katalogów, k to szerokość
const znajdzSciezki = async (nazwaPliku, katalogBazowy = process.env.HOME) => {
  const sciezki = [];
  
  try {
    const dane = await fs.readdir(katalogBazowy);
    
    for (const danePliku of dane) {
      const sciezkaPliku = path.join(katalogBazowy, danePliku);
      
      try {
        const stat = await fs.lstat(sciezkaPliku);
        
        if (stat.isFile() && danePliku === nazwaPliku) {
          sciezki.push(sciezkaPliku);
        } else if (stat.isDirectory()) {
          // Rekurencyjnie przeszukaj podkatalogi
          const podsciezki = await znajdzSciezki(nazwaPliku, sciezkaPliku);
          sciezki.push(...podsciezki);
        }
      } catch (err) {
        // Pomijaj niedostępne pliki/katalogi (brak uprawnień)
        continue;
      }
    }
  } catch (err) {
    // Pomijaj niedostępne katalogi
  }
  
  return sciezki;
};

const testZnajdzSciezki = async () => {
  const nazwaPliku = "test.txt";
  const sciezkiPlikow = ["lista.txt", nazwaPliku];
  const tekst = "przykladowy tekst.\n";

  const sciezkaFolderu = path.join(process.env.HOME, "temp_dir");
  await fs.mkdir(sciezkaFolderu);

  for (const plik of sciezkiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    await fs.writeFile(sciezkaPliku, tekst);
  }

  const oczekiwane = [path.join(sciezkaFolderu, nazwaPliku)];
  const wynik = await znajdzSciezki(nazwaPliku);

  console.assert(
    wynik.length === oczekiwane.length,
    `Blad testu znajdzSciezki: ${wynik.length} !== ${oczekiwane.length}`
  );

  console.assert(
    wynik.includes(oczekiwane[0]),
    `Blad testu znajdzSciezki: ${wynik} nie zawiera ${oczekiwane[0]}`
  );

  await fs.rm(sciezkaFolderu, {
    recursive: true,
  });
};

const main = async () => {
  await testZnajdzSciezki();
};

main();

