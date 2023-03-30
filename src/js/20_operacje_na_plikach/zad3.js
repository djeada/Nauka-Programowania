/*
Tytuł: Znalezienie ścieżki pliku o danej nazwie

Treść: Otrzymujesz napis reprezentujący nazwę pliku. Przeszukaj cały system i zapisz w liście wszystkie ścieżki plików o podanej nazwie.

Dane wejściowe: Napis

Dane wyjściowe: Lista napisów
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
    `Błąd testu znajdzSciezki: ${wynik.length} !== ${oczekiwane.length}`
  );

  console.assert(
    wynik.includes(oczekiwane[0]),
    `Błąd testu znajdzSciezki: ${wynik} nie zawiera ${oczekiwane[0]}`
  );

  await fs.rmdir(sciezkaFolderu, {
    recursive: true,
  });
};

const main = async () => {
  await testZnajdzSciezki();
};

main();
