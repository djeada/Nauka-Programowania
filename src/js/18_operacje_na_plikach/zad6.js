/*
Otrzymujesz napis reprezentujacy sciezke pliku tekstowego. Oblicz:
a) Liczbe wierszy pliku.
b) Liczbe slow w pliku. Slowa oddzielone sa spacjami i moga skladac
sie wylacznie ze znakow bedacych literami.
c) Srednia dlugosc wiersza.
d) Srednia liczbe slow na wiersz.
e) Czestosc wystepowania kazdego ze slow w pliku.
*/
const fs = require("fs").promises;

wczytajPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  wiersze = tekst.split("\n");
  return wiersze;
};

liczbaWierszy = function (wiersze) {
  return wiersze.length;
};

liczbaSlow = function (wiersze) {
  let slowa = 0;
  for (let i = 0; i < wiersze.length; i++) {
    podzielonyWiersz = wiersze[i].split(" ");
    podzielonyWiersz = podzielonyWiersz.filter((slowo) => {
      return slowo.length > 0;
    });
    slowa += podzielonyWiersz.length;
  }
  return slowa;
};

sredniaDlugoscWiersza = function (wiersze) {
  let dlugosci = 0;
  for (let i = 0; i < wiersze.length; i++) {
    dlugosci += wiersze[i].length;
  }
  return dlugosci / wiersze.length;
};

sredniaLiczbaSlowNaWiersz = function (wiersze) {
  liczbaSlow = liczbaSlow(wiersze);
  return liczbaSlow / wiersze.length;
};

histogramSlow = function (wiersze) {
  slowa = [];
  for (let i = 0; i < wiersze.length; i++) {
    podzielonyWiersz = wiersze[i].split(" ");
    podzielonyWiersz = podzielonyWiersz.filter((slowo) => {
      return slowo.length;
    });
    for (let j = 0; j < podzielonyWiersz.length; j++) {
      slowo = podzielonyWiersz[j];
      slowo = slowo.replace(/[^a-zA-Z]/g, "").toLowerCase();
      slowa.push(slowo);
    }
  }
  histogram = new Map();
  for (const slowo of slowa) {
    if (histogram.has(slowo)) {
      histogram.set(slowo, histogram.get(slowo) + 1);
    } else {
      histogram.set(slowo, 1);
    }
  }
  return histogram;
};

test1 = async () => {
  const sciezka = "test1.txt";
  tekst =
    'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of ".txt".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.';
  await fs.writeFile(sciezka, tekst);
  const trescPliku = await wczytajPlik(sciezka);
  const oczekiwane = 10;
  const wynik = liczbaWierszy(trescPliku);

  if (wynik !== oczekiwane) {
    throw new Error(`Assertion error line 180: ${wynik} != ${oczekiwane}`);
  }

  fs.unlink(sciezka);
};

test2 = async () => {
  const sciezka = "test1.txt";
  tekst =
    'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of ".txt".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.';
  await fs.writeFile(sciezka, tekst);
  const trescPliku = await wczytajPlik(sciezka);
  const oczekiwane = 88;
  const wynik = liczbaSlow(trescPliku);

  if (wynik !== oczekiwane) {
    throw new Error(`Assertion error line 180: ${wynik} != ${oczekiwane}`);
  }

  fs.unlink(sciezka);
};

test3 = async () => {
  const sciezka = "test1.txt";
  tekst =
    'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of ".txt".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.';
  await fs.writeFile(sciezka, tekst);
  const trescPliku = await wczytajPlik(sciezka);
  const oczekiwane = 50.5;
  const wynik = sredniaDlugoscWiersza(trescPliku);

  if (Math.abs(wynik - oczekiwane) > 0.1) {
    throw new Error(`Assertion error line 180: ${wynik} != ${oczekiwane}`);
  }

  fs.unlink(sciezka);
};

test4 = async () => {
  const sciezka = "test1.txt";
  tekst =
    'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of ".txt".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.';
  await fs.writeFile(sciezka, tekst);
  const trescPliku = await wczytajPlik(sciezka);
  const oczekiwane = 8.8;
  const wynik = sredniaLiczbaSlowNaWiersz(trescPliku);

  if (Math.abs(wynik - oczekiwane) > 0.1) {
    throw new Error(`Assertion error line 180: ${wynik} != ${oczekiwane}`);
  }

  fs.unlink(sciezka);
};

test5 = async () => {
  const sciezka = "test1.txt";
  tekst =
    'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of ".txt".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.';
  await fs.writeFile(sciezka, tekst);
  const trescPliku = await wczytajPlik(sciezka);
  const oczekiwane = new Map([
    ["bold", 1],
    ["in", 1],
    ["shown", 1],
    ["then", 1],
    ["simple", 1],
    ["basic", 1],
    ["contains", 1],
    ["were", 1],
    ["may", 1],
    ["such", 3],
    ["files", 2],
    ["it", 1],
    ["hypertext", 1],
    ["hello", 1],
    ["note", 1],
    ["file", 3],
    ["web", 1],
    ["ascii", 1],
    ["is", 2],
    ["example", 2],
    ["following", 1],
    ["this", 1],
    ["of", 2],
    ["text", 3],
    ["stored", 1],
    ["that", 1],
    ["by", 1],
    ["on", 1],
    ["formatting", 1],
    ["browser", 1],
    ["typed", 1],
    ["a", 3],
    ["server", 1],
    ["would", 1],
    ["contain", 1],
    ["as", 2],
    ["markup", 1],
    ["characters", 1],
    ["there", 1],
    ["for", 2],
    ["the", 4],
    ["to", 1],
    ["have", 1],
    ["these", 1],
    ["will", 1],
    ["paragraphs", 1],
    ["attributes", 1],
    ["can", 1],
    ["has", 1],
    ["codes", 1],
    ["if", 1],
    ["some", 1],
    ["but", 1],
    ["not", 1],
    ["be", 2],
    ["interpreted", 1],
    ["into", 1],
    ["extension", 1],
    ["txt", 1],
    ["although", 1],
    ["no", 1],
    ["support", 1],
    ["bolding", 1],
    ["html", 1],
    ["layout", 1],
    ["an", 2],
    ["hej", 1],
    ["stronghellostrong", 1],
    ["word", 1],
  ]);
  const wynik = histogramSlow(trescPliku);

  if (wynik.size !== oczekiwane.size) {
    throw new Error(
      `Assertion error line 180: ${wynik.size} != ${oczekiwane.size}`
    );
  }

  for (const [klucz, wartosc] of wynik) {
    if (oczekiwane.get(klucz) !== wartosc) {
      throw new Error(
        `Assertion error line 180: for key ${klucz}: ${wartosc} != ${oczekiwane.get(
          klucz
        )}`
      );
    }
  }

  fs.unlink(sciezka);
};

main = async () => {
  await test1();
  await test2();
  await test3();
  await test4();
  await test5();
};

main();
