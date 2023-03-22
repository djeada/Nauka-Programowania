/*
Tytuł: Wczytaj i wypisz treść pliku.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do pliku tekstowego. Wczytaj plik i wypisz jego treść.

Dane wejściowe: Napis reprezentujący ścieżkę do pliku.

Dane wyjściowe: Napis zawierający treść pliku.
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
