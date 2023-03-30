/*
Tytul: Sprawdzenie, czy sciezka nalezy do pliku/folderu

Tresc: Otrzymujesz napis reprezentujacy sciezke. Sprawdz, czy jest to sciezka do pliku lub folderu.

Dane wejsciowe: Napis

Dane wyjsciowe: Wartosc logiczna
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

