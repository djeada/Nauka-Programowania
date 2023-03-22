/*
Otrzymujesz napis reprezentujacy sciezke folderu. Usun
wszystkie pliki o rozmiarach wiekszych niz 10 kB znajdujace
sie w podanym folderze oraz jego podfolderach.
*/
const fs = require("fs").promises;
const path = require("path");

usunPliki = async (sciezka, rozmiar) => {
  const pliki = await fs.readdir(sciezka);
  const plikiTxt = pliki.filter((plik) => plik.endsWith(".txt"));
  for (let i = 0; i < plikiTxt.length; i++) {
    const plik = plikiTxt[i];
    const sciezkaPliku = path.join(sciezka, plik);
    const rozmiarPliku = (await fs.stat(sciezkaPliku)).size;
    if (rozmiarPliku > rozmiar) {
      await fs.unlink(sciezkaPliku);
    }
  }
};

test1 = async () => {
  const sciezkaFolderu = "temp_dir";
  const sciezkikiPlikow = ["lista.txt", "test.txt"];
  const tekst = "przykladowy tekst.\n";

  await fs.mkdir(sciezkaFolderu);

  for (const plik of sciezkikiPlikow) {
    const sciezkaPliku = path.join(sciezkaFolderu, plik);
    await fs.writeFile(sciezkaPliku, tekst.repeat(10000));
  }

  await usunPliki(sciezkaFolderu, 10 * 1024);

  const daneFolderu = await fs.readdir(sciezkaFolderu);
  if (daneFolderu.length !== 0) {
    throw new Error(`Assertion error line 180: ${daneFolderu.length} != 0`);
  }

  await fs.rmdir(sciezkaFolderu, {
    recursive: true,
  });
};

main = async () => {
  await test1();
};

main();
