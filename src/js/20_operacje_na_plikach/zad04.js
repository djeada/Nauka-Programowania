/*
Tytul: Wczytaj i wypisz tresc pliku.

Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Wczytaj plik i wypisz jego tresc.

Dane wejsciowe: Napis reprezentujacy sciezke do pliku.

Dane wyjsciowe: Napis zawierajacy tresc pliku.
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

