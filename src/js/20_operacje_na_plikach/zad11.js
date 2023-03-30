/*
Tytul: Podmien tresci plikow.

Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do plikow. Podmien tresci obu plikow.

Dane wejsciowe: Dwa napisy reprezentujace sciezki do plikow.

Dane wyjsciowe: Brak.

*/

const fs = require("fs").promises;

const wczytajPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  const wiersze = tekst.split("\n");
  return wiersze;
};

const podmienPliki = async (sciezka1, sciezka2) => {
  const dane1 = await fs.readFile(sciezka1, "utf8");
  const dane2 = await fs.readFile(sciezka2, "utf8");
  await fs.writeFile(sciezka1, dane2);
  await fs.writeFile(sciezka2, dane1);
};

const test1 = async () => {
  const sciezka1 = "temp1.txt";
  const sciezka2 = "temp2.txt";
  const tekst1 = "Ala ma kota";
  const tekst2 = "Kot ma Ale";

  await fs.writeFile(sciezka1, tekst1);
  await fs.writeFile(sciezka2, tekst2);

  await podmienPliki(sciezka1, sciezka2);

  const oczekiwane1 = ["Kot ma Ale"];
  const wynik1 = await wczytajPlik(sciezka1);
  console.assert(
    wynik1.length === oczekiwane1.length,
    `Blad asercji: ${wynik1.length} != ${oczekiwane1.length}`
  );

  for (let i = 0; i < wynik1.length; i++) {
    console.assert(
      wynik1[i] === oczekiwane1[i],
      `Blad asercji: ${wynik1[i]} != ${oczekiwane1[i]}`
    );
  }

  const oczekiwane2 = ["Ala ma kota"];
  const wynik2 = await wczytajPlik(sciezka2);
  console.assert(
    wynik2.length === oczekiwane2.length,
    `Blad asercji: ${wynik2.length} != ${oczekiwane2.length}`
  );

  for (let i = 0; i < wynik2.length; i++) {
    console.assert(
      wynik2[i] === oczekiwane2[i],
      `Blad asercji: ${wynik2[i]} != ${oczekiwane2[i]}`
    );
  }

  await fs.unlink(sciezka1);
  await fs.unlink(sciezka2);
};

const main = async () => {
  await test1();
};

main();

