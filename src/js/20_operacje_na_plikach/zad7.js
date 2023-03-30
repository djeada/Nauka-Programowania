/*
Tytul: Dodaj wiersz do pliku.

Tresc zadania: Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke do pliku tekstowego, a drugi napis reprezentuje wiersz tekstu. Dodaj otrzymany wiersz na poczatek pliku tekstowego.

Dane wejsciowe: Dwa napisy - sciezka do pliku oraz wiersz tekstu.

Dane wyjsciowe: Brak.
*/

const fs = require("fs").promises;

const wczytajPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  const wiersze = tekst.split("\n");
  return wiersze;
};

const dostawWierszNaPoczatek = async (sciezka, wiersz) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  const nowyTekst = wiersz + "\n" + tekst;
  await fs.writeFile(sciezka, nowyTekst);
};

const test1 = async () => {
  const sciezka = "temp.txt";
  const tekst = "przykladowy tekst";

  await fs.writeFile(sciezka, tekst);

  await dostawWierszNaPoczatek(sciezka, "Hej");
  const oczekiwane = ["Hej", "przykladowy tekst"];
  const wynik = await wczytajPlik(sciezka);

  console.assert(
    wynik.length === oczekiwane.length,
    `Blad asercji: ${wynik.length} != ${oczekiwane.length}`
  );

  for (let i = 0; i < wynik.length; i++) {
    console.assert(
      wynik[i] === oczekiwane[i],
      `Blad asercji: ${wynik[i]} != ${oczekiwane[i]}`
    );
  }

  await fs.unlink(sciezka);
};

const main = async () => {
  await test1();
};

main();

