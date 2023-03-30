/*
Tytul: Skopiuj pliki.

Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do folderow. Skopiuj wszystkie pliki PNG z pierwszego folderu do drugiego folderu.

Dane wejsciowe: Dwa napisy reprezentujace sciezki do folderow.

Dane wyjsciowe: Brak.

*/

const fs = require("fs").promises;
const path = require("path");

const skopiujPliki = async (zrodlo, cel, rozszerzenie) => {
  const dane = await fs.readdir(zrodlo);
  for (const danePliku of dane) {
    const sciezkaPliku = path.join(zrodlo, danePliku);
    const stat = await fs.lstat(sciezkaPliku);
    if (stat.isFile() && path.extname(danePliku) === rozszerzenie) {
      const sciezkaDocelowa = path.join(cel, danePliku);
      await fs.copyFile(sciezkaPliku, sciezkaDocelowa);
    }
  }
};

const test1 = async () => {
  const sciezka1 = "test1";
  const sciezka2 = "test2";
  const sciezkiPlikow = ["plik1.png", "plik2.png"];
  const tekst = "przykladowy tekst.\n";

  await fs.mkdir(sciezka1);
  await fs.mkdir(sciezka2);

  for (const plik of sciezkiPlikow) {
    const sciezkaPliku = path.join(sciezka1, plik);
    await fs.writeFile(sciezkaPliku, tekst);
  }

  await skopiujPliki(sciezka1, sciezka2, ".png");

  for (const plik of sciezkiPlikow) {
    const sciezkaPliku = path.join(sciezka2, plik);
    const oczekiwane = true;
    let wynik = false;

    try {
      await fs.access(sciezkaPliku);
      wynik = true;
    } catch (err) {
      console.log(err);
    }
    console.assert(
      wynik === oczekiwane,
      `Blad asercji: ${sciezkaPliku} nie istnieje`
    );
  }

  await fs.rmdir(sciezka1, {
    recursive: true,
  });
  await fs.rmdir(sciezka2, {
    recursive: true,
  });
};

const main = async () => {
  await test1();
};

main();

