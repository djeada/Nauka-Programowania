/*
ZAD-05 — Posortuj adresy IP z pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `sort`, `list`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego, w którym w każdej linii znajduje się jeden adres IP. Wczytaj wszystkie adresy, posortuj je **alfabetycznie** i wypisz jako listę.

### Wejście

* 1 linia: `file_path`

### Wyjście

* 1 linia: lista adresów IP jako napisy, np. `['10.0.0.1', ...]`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\adresy_ip.txt
```

**Wyjście:**

```
['10.0.0.1', '172.16.0.5', '192.168.1.10', '192.168.1.2']
```

*/
const fs = require("fs").promises;

const wczytajPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  let wiersze = tekst.split("\n");
  wiersze = wiersze.filter((wiersz) => wiersz.length > 0);
  return wiersze;
};

const sortujAdresyIp = (ip) => {
  ip.sort((a, b) => {
    const a1 = a.split(".");
    const b1 = b.split(".");
    if (parseInt(a1[0]) < parseInt(b1[0])) {
      return -1;
    }
    if (parseInt(a1[0]) > parseInt(b1[0])) {
      return 1;
    }
    if (parseInt(a1[1]) < parseInt(b1[1])) {
      return -1;
    }
    if (parseInt(a1[1]) > parseInt(b1[1])) {
      return 1;
    }
    if (parseInt(a1[2]) < parseInt(b1[2])) {
      return -1;
    }
    if (parseInt(a1[2]) > parseInt(b1[2])) {
      return 1;
    }
    if (parseInt(a1[3]) < parseInt(b1[3])) {
      return -1;
    }
    if (parseInt(a1[3]) > parseInt(b1[3])) {
      return 1;
    }
    return 0;
  });

  return ip;
};

const test1 = async () => {
  const sciezka = "temp.txt";
  const tekst =
    "123.4.245.23\n104.244.253.29\n1.198.3.93\n32.183.93.40\n104.30.244.2\n104.244.4.1\n";
  const oczekiwane = [
    "1.198.3.93",
    "32.183.93.40",
    "104.30.244.2",
    "104.244.4.1",
    "104.244.253.29",
    "123.4.245.23",
  ];

  await fs.writeFile(sciezka, tekst);
  const adresyIp = await wczytajPlik(sciezka);
  const wynik = sortujAdresyIp(adresyIp);

  console.assert(
    wynik.length == oczekiwane.length,
    `Error: ${wynik.length} != ${oczekiwane.length}`
  );

  for (let i = 0; i < wynik.length; i++) {
    console.assert(
      wynik[i] === oczekiwane[i],
      `Error: ${wynik[i]} != ${oczekiwane[i]}`
    );
  }
  await fs.unlink(sciezka);
};

const main = async () => {
  await test1();
};

main();

