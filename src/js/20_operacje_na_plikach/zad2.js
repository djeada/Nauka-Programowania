/*
Tytul: Znalezienie w folderze wszystkich plikow z danym rozszerzeniem

Tresc: Otrzymujesz dwa napisy. Pierwszy napis to sciezka folderu, a drugi to rozszerzenie szukanych plikow. Znajdz w folderze wszystkie pliki o podanym rozszerzeniu i zapisz ich nazwy w liscie.

Dane wejsciowe: Dwa napisy

Dane wyjsciowe: Lista napisow
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

