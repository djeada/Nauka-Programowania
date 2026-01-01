/*
ZAD-04 — Wczytaj i wypisz treść pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `read`, `encoding`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Wczytaj zawartość pliku i wypisz ją.

### Wejście

* 1 linia: `file_path`

### Wyjście

* treść pliku (dokładnie taka jak w pliku)

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\wiadomość.txt
```

**Wyjście:**

```
Witaj! To jest przykładowa treść pliku tekstowego.
```

*/

const fs = require("fs").promises;

const wypiszPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  console.log(tekst);
};

const main = async () => {
  const sciezka = "test.txt";
  const tekst = "Przykladowy tekst.";

  await fs.writeFile(sciezka, tekst);

  await wypiszPlik(sciezka);

  await fs.unlink(sciezka);
};

main();

