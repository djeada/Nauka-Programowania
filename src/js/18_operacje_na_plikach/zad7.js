/*
Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke
pliku tekstowego. Drugi napis reprezentuje wiersz tekstu.
Dostaw otrzymany wiersz tekstu na poczatek pliku tekstowego.
*/
const fs = require("fs").promises;

wczytajPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  wiersze = tekst.split("\n");
  return wiersze;
};

dostawWierszNaPoczatek = async (sciezka, wiersz) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  const nowyTekst = wiersz + "\n" + tekst;
  await fs.writeFile(sciezka, nowyTekst);
};

test1 = async () => {
  const sciezka = "temp.txt";
  const tekst = "przykladowy tekst";

  await fs.writeFile(sciezka, tekst);

  await dostawWierszNaPoczatek(sciezka, "Hej");
  const oczekiwane = ["Hej", "przykladowy tekst"];
  const wynik = await wczytajPlik(sciezka);
  if (wynik.length !== oczekiwane.length) {
    throw new Error(
      `Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`
    );
  }

  for (let i = 0; i < wynik.length; i++) {
    if (wynik[i] !== oczekiwane[i]) {
      throw new Error(
        `Assertion error line 34: ${wynik[i]} != ${oczekiwane[i]}`
      );
    }
  }

  await fs.unlink(sciezka);
};

main = async () => {
  await test1();
};

main();
