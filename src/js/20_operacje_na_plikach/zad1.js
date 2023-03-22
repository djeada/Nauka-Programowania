/*
Tytuł: Sprawdzenie, czy ścieżka należy do pliku/folderu

Treść: Otrzymujesz napis reprezentujący ścieżkę. Sprawdź, czy jest to ścieżka do pliku lub folderu.

Dane wejściowe: Napis

Dane wyjściowe: Wartość logiczna
*/

const fs = require("fs").promises;

function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

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

  assert(
    wynik === oczekiwane,
    `Błąd testu czyPlik: ${wynik} !== ${oczekiwane}`
  );

  const oczekiwane2 = false;
  const wynik2 = await czyFolder(sciezkaPliku);

  assert(
    wynik2 === oczekiwane2,
    `Błąd testu czyPlik: ${wynik2} !== ${oczekiwane2}`
  );

  await fs.unlink(sciezkaPliku);
};

const testCzyFolder = async () => {
  const sciezkaFolderu = "temp_dir";

  await fs.mkdir(sciezkaFolderu);

  const oczekiwane = false;
  const wynik = await czyPlik(sciezkaFolderu);

  assert(
    wynik === oczekiwane,
    `Błąd testu czyFolder: ${wynik} !== ${oczekiwane}`
  );

  const oczekiwane2 = true;
  const wynik2 = await czyFolder(sciezkaFolderu);

  assert(
    wynik2 === oczekiwane2,
    `Błąd testu czyFolder: ${wynik2} !== ${oczekiwane2}`
  );

  await fs.rmdir(sciezkaFolderu);
};

const main = async () => {
  await testCzyPlik();
  await testCzyFolder();
};

main();
