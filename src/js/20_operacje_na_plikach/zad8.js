/*
Tytuł: Znajdź i zmodyfikuj pliki spełniające warunek.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do folderu.

a) Dodaj swoje inicjały na końcu wszystkich plików tekstowych znajdujących się w podanym folderze i jego podfolderach.

b) Usuń środkowy wiersz z każdego pliku CSV znajdującego się w podanym folderze i jego podfolderach.

Dane wejściowe: Napis reprezentujący ścieżkę do folderu.

Dane wyjściowe: Brak.
*/

const fs = require("fs").promises;
const path = require("path");

const wczytajPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  const wiersze = tekst.split("\n");
  return wiersze;
};

const dodajInicjaly = async (sciezka, inicjaly) => {
  const pliki = await fs.readdir(sciezka);
  const plikiTxt = pliki.filter((plik) => plik.endsWith(".txt"));
  for (let i = 0; i < plikiTxt.length; i++) {
    const plik = plikiTxt[i];
    const sciezkaPliku = sciezka + "/" + plik;
    const tekst = await fs.readFile(sciezkaPliku, "utf8");
    const nowyTekst = tekst + "\n" + inicjaly;
    await fs.writeFile(sciezkaPliku, nowyTekst);
  }
};

const usunSrodkowyWiersz = async (sciezka) => {
  const pliki = await fs.readdir(sciezka);
  const plikiCsv = pliki.filter((plik) => plik.endsWith(".csv"));
  for (let i = 0; i < plikiCsv.length; i++) {
    const plik = plikiCsv[i];
    const sciezkaPliku = sciezka + "/" + plik;
    const tekst = await fs.readFile(sciezkaPliku, "utf8");
    const wiersze = tekst.split("\n");
    const srodek = Math.floor(wiersze.length / 2);
    const nowyTekst = wiersze
      .slice(0, srodek)
      .concat(wiersze.slice(srodek + 1))
      .join("\n");
    await fs.writeFile(sciezkaPliku, nowyTekst);
  }
};

const test1 = async () => {
  const sciezkaFolderu = "temp_dir";
  const sciezkikiPlikow = ["lista.txt", "test.txt"];
  const tekst = "przykladowy tekst.";

  await fs.mkdir(sciezkaFolderu);

  for (const plik of sciezkikiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    await fs.writeFile(sciezkaPliku, tekst);
  }

  const dane = "A.D.";
  await dodajInicjaly(sciezkaFolderu, dane);

  const oczekiwane = ["przykladowy tekst.", "A.D."];
  for (const plik of sciezkikiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    const wynik = await wczytajPlik(sciezkaPliku);
    console.assert(
      wynik.length === oczekiwane.length,
      `Błąd asercji: ${wynik.length} != ${oczekiwane.length}`
    );

    for (let i = 0; i < wynik.length; i++) {
      console.assert(
        wynik[i] === oczekiwane[i],
        `Błąd asercji: ${wynik[i]} != ${oczekiwane[i]}`
      );
    }
  }

  await fs.rmdir(sciezkaFolderu, {
    recursive: true,
  });
};

const test2 = async () => {
  const sciezkaFolderu = "temp_dir";
  const sciezkikiPlikow = ["lista.csv", "test.csv"];
  const tekst = "test1; test2; test3\ntest4; test5; test6\ntest7; test8; test9";

  await fs.mkdir(sciezkaFolderu);

  for (const plik of sciezkikiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    await fs.writeFile(sciezkaPliku, tekst);
  }

  await usunSrodkowyWiersz(sciezkaFolderu);

  const oczekiwane = ["test1; test2; test3", "test7; test8; test9"];
  for (const plik of sciezkikiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    const wynik = await wczytajPlik(sciezkaPliku);
    console.assert(
      wynik.length === oczekiwane.length,
      `Błąd asercji: ${wynik.length} != ${oczekiwane.length}`
    );

    for (let i = 0; i < wynik.length; i++) {
      console.assert(
        wynik[i] === oczekiwane[i],
        `Błąd asercji: ${wynik[i]} != ${oczekiwane[i]}`
      );
    }
  }

  await fs.rmdir(sciezkaFolderu, {
    recursive: true,
  });
};

const main = async () => {
  await test1();
  await test2();
};

main();
