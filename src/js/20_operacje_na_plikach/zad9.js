/*
Tytuł: Usuń pliki spełniające warunek.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do folderu. Usuń wszystkie pliki o rozmiarze większym niż 10 kB znajdujące się w podanym folderze i jego podfolderach.

Dane wejściowe: Napis reprezentujący ścieżkę do folderu.

Dane wyjściowe: Brak.
*/
const fs = require("fs").promises;
const path = require("path");

const usunPliki = async (sciezka, rozmiar) => {
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

const test1 = async () => {
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
  console.assert(
    daneFolderu.length === 0,
    `Błąd asercji: ${daneFolderu.length} != 0`
  );

  await fs.rmdir(sciezkaFolderu, {
    recursive: true,
  });
};

const main = async () => {
  await test1();
};

main();
