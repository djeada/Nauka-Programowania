/*
Otrzymujesz dwa napisy reprezentujace sciezki folderow. Przenies wszystkie pliki
csv z pierwszego folderu (oraz wszystkich jego podfolderow) do drugiego folderu.
*/

const fs = require("fs").promises;
const path = require("path");

przeniesPliki = async (zrodlo, cel, rozszerzenie) => {
  const dane = await fs.readdir(zrodlo);
  const pliki = dane.filter((plik) => plik.endsWith(rozszerzenie));
  for (const plik of pliki) {
    const sciezkaPliku = path.join(zrodlo, plik);
    const sciezkaDocelowa = path.join(cel, plik);
    await fs.copyFile(sciezkaPliku, sciezkaDocelowa);
    await fs.unlink(sciezkaPliku);
  }
};

test1 = async () => {
  const folder1 = "temp_dir1";
  const folder2 = "temp_dir2";

  await fs.mkdir(folder1);
  await fs.mkdir(folder2);

  const sciezkaPliku1 = path.join(folder1, "plik1.csv");
  const sciezkaPliku2 = path.join(folder1, "plik2.csv");

  sciezki = [sciezkaPliku1, sciezkaPliku2];

  for (const sciezkaPliku of sciezki) {
    await fs.writeFile(sciezkaPliku, "test1; test2");
  }

  await przeniesPliki(folder1, folder2, ".csv");

  const nowaSciezkaPliku1 = path.join(folder2, "plik1.csv");
  const nowaSciezkaPliku2 = path.join(folder2, "plik2.csv");

  const noweSciezki = [nowaSciezkaPliku1, nowaSciezkaPliku2];

  for (const nowaSciezkaPliku of noweSciezki) {
    const stat = await fs.lstat(nowaSciezkaPliku);
    if (!stat.isFile()) {
      throw new Error(
        `Assertion error line 32: ${nowaSciezkaPliku} does not exist`
      );
    }
  }

  for (const sciezkaPliku of sciezki) {
    try {
      await fs.access(sciezkaPliku);
      throw new Error(`Assertion error line 38: ${sciezkaPliku} exists`);
    } catch (err) {
      if (err.code !== "ENOENT") {
        throw err;
      }
    }
  }

  await fs.rmdir(folder1, {
    recursive: true,
  });
  await fs.rmdir(folder2, {
    recursive: true,
  });
};

main = async () => {
  await test1();
};

main();
