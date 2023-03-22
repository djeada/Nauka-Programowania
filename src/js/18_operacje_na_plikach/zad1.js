/*
Otrzymujesz napis reprezentujacy sciezke.
a) Sprawdz, czy jest to sciezka pliku.
b) Sprawdz, czy jest to sciezka folderu.
*/

const fs = require("fs").promises;

czyPlik = async (sciezka) => {
  try {
    const stat = await fs.lstat(sciezka);
    return stat.isFile();
  } catch (err) {
    return false;
  }
};

czyFolder = async (sciezka) => {
  try {
    const stat = await fs.lstat(sciezka);
    return stat.isDirectory();
  } catch (err) {
    return false;
  }
};

test1 = async () => {
  const sciezkaPliku = "temp.txt";
  const tekst = "przykladowy tekst.\n";

  await fs.writeFile(sciezkaPliku, tekst);

  const oczekiwane = true;
  const wynik = await czyPlik(sciezkaPliku);

  if (wynik !== oczekiwane) {
    throw new Error(`Assertion error line 164: ${wynik} != ${oczekiwane}`);
  }

  const oczekiwane2 = false;
  const wynik2 = await czyFolder(sciezkaPliku);

  if (wynik2 !== oczekiwane2) {
    throw new Error(`Assertion error line 169: ${wynik2} != ${oczekiwane2}`);
  }

  await fs.unlink(sciezkaPliku);
};

test2 = async () => {
  const sciezkaFolderu = "temp_dir";

  await fs.mkdir(sciezkaFolderu);

  const oczekiwane = false;
  const wynik = await czyPlik(sciezkaFolderu);

  if (wynik !== oczekiwane) {
    throw new Error(`Assertion error line 180: ${wynik} != ${oczekiwane}`);
  }

  const oczekiwane2 = true;
  const wynik2 = await czyFolder(sciezkaFolderu);

  if (wynik2 !== oczekiwane2) {
    throw new Error(`Assertion error line 185: ${wynik2} != ${oczekiwane2}`);
  }

  await fs.rmdir(sciezkaFolderu);
};

main = async () => {
  await test1();
  await test2();
};

main();
