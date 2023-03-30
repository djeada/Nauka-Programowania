/*
Tytuł: Statystyki dla pliku tekstowego.

Treść zadania: Otrzymujesz napis reprezentujący ścieżkę do pliku tekstowego. Oblicz:

a) Liczbę wierszy w pliku.

b) Liczbę słów w pliku (słowa oddzielone są spacjami i mogą składać się wyłącznie z liter).

c) Średnią długość wiersza.

d) Średnią liczbę słów na wiersz.

e) Częstość występowania każdego ze słów w pliku.

Dane wejściowe: Napis reprezentujący ścieżkę do pliku.

Dane wyjściowe:

a) Liczba naturalna reprezentująca liczbę wierszy.

b) Liczba naturalna reprezentująca liczbę słów.

c) Liczba zmiennoprzecinkowa reprezentująca średnią długość wiersza.

d) Liczba zmiennoprzecinkowa reprezentująca średnią liczbę słów na wiersz.

e) Słownik par: napis (słowo), liczba naturalna (częstotliwość występowania słowa). 

Przykład:

Dla otrzymanego napisu: "C:\Users\Username\Documents\text_file.txt" powinno zostać zwrócone:

a) Liczba naturalna reprezentująca liczbę wierszy, np. 6

b) Liczba naturalna reprezentująca liczbę słów, np. 25

c) Liczba zmiennoprzecinkowa reprezentująca średnią długość wiersza, np. 41.5

d) Liczba zmiennoprzecinkowa reprezentująca średnią liczbę słów na wiersz, np. 4.2

e) Słownik par: napis (słowo), liczba naturalna (częstotliwość występowania słowa): {'The': 2, 'quick': 2, 'brown': 2, 'fox': 2, 'jumped': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog.': 1, 'cat': 1, 'sat': 1, 'on': 1, 'mat.': 1, 'Foxes': 1, 'are': 1, 'known': 1, 'for': 1, 'their': 2, 'cunning': 1, 'and': 1, 'intelligence.': 1, 'Dogs': 1, 'loyalty': 1, 'kindness.': 1, 'Cats': 1, 'independent': 1, 'animals': 1, 'but': 1, 'can': 1, 'be': 1, 'affectionate.': 1, 'This': 1, 'text': 1, 'file': 1, 'contains': 1, 'ten': 1, 'lines': 1, 'and': 1, 'words.': 1}

Tekst pliku:

"The quick brown fox jumped over the lazy dog.
The quick brown cat sat on the mat.
Foxes are known for their cunning and intelligence.
Dogs are known for their loyalty and kindness.
Cats are independent animals but can be affectionate.
This text file contains six lines and 25 words."
*/
const fs = require("fs").promises;

const wczytajPlik = async (sciezka) => {
  const tekst = await fs.readFile(sciezka, "utf8");
  const wiersze = tekst.split("\n");
  return wiersze;
};

const zapiszPlik = async (sciezka, tekst) => {
  await fs.writeFile(sciezka, tekst);
};

const znajdzLiczbeWierszy = (wiersze) => {
  return wiersze.length;
};

const znajdzLiczbeSlow = (wiersze) => {
  let slowa = 0;
  wiersze.forEach((wiersz) => {
    const podzielonyWiersz = wiersz
      .split(" ")
      .filter((slowo) => slowo.length > 0);
    slowa += podzielonyWiersz.length;
  });
  return slowa;
};

const znajdzSredniaDlugoscWiersza = (wiersze) => {
  const dlugosci = wiersze.reduce((acc, wiersz) => acc + wiersz.length, 0);
  return dlugosci / wiersze.length;
};

const znajdzSredniaLiczbeSlowNaWiersz = (wiersze) => {
  let znajdzLiczbeSlow = 0;
  wiersze.forEach((wiersz) => {
    znajdzLiczbeSlow += wiersz.split(" ").length;
  });
  return znajdzLiczbeSlow / wiersze.length;
};

const znajdzHistogramSlow = (wiersze) => {
  const slowa = [];
  wiersze.forEach((wiersz) => {
    const podzielonyWiersz = wiersz
      .split(" ")
      .filter((slowo) => slowo.length > 0);
    podzielonyWiersz.forEach((slowo) => {
      slowa.push(slowo.replace(/[^a-zA-Z]/g, "").toLowerCase());
    });
  });

  const histogram = new Map();
  slowa.forEach((slowo) => {
    if (histogram.has(slowo)) {
      histogram.set(slowo, histogram.get(slowo) + 1);
    } else {
      histogram.set(slowo, 1);
    }
  });

  return histogram;
};

const statystykiDlaPliku = async (sciezka) => {
  const wiersze = await wczytajPlik(sciezka);
  const liczbaWierszy = znajdzLiczbeWierszy(wiersze);
  const liczbaSlow = znajdzLiczbeSlow(wiersze);
  const sredniaDlugoscWiersza = znajdzSredniaDlugoscWiersza(wiersze);
  const sredniaLiczbaSlowNaWiersz = znajdzSredniaLiczbeSlowNaWiersz(wiersze);
  const histogramSlow = znajdzHistogramSlow(wiersze);

  return {
    liczbaWierszy,
    liczbaSlow,
    sredniaDlugoscWiersza,
    sredniaLiczbaSlowNaWiersz,
    histogramSlow,
  };
};

const testznajdzLiczbeWierszy = () => {
  const wiersze = ["Wiersz 1", "Wiersz 2", "Wiersz 3"];
  const oczekiwanaznajdzLiczbeWierszy = 3;
  const wynik = znajdzLiczbeWierszy(wiersze);
  console.assert(
    wynik === oczekiwanaznajdzLiczbeWierszy,
    "Nieprawidłowa liczba wierszy"
  );
};

const testznajdzLiczbeSlow = () => {
  const wiersze = ["To jest wiersz", "To jest inny wiersz", "Ostatni wiersz"];
  const oczekiwanaznajdzLiczbeSlow = 9;
  const wynik = znajdzLiczbeSlow(wiersze);
  console.assert(
    wynik === oczekiwanaznajdzLiczbeSlow,
    "Nieprawidłowa liczba słów"
  );
};
const testznajdzSredniaDlugoscWiersza = () => {
  const wiersze = ["To jest wiersz", "To jest inny wiersz", "Ostatni wiersz"];
  const oczekiwanaSredniaDlugosc = 15.666;

  const wynik = znajdzSredniaDlugoscWiersza(wiersze);
  console.assert(
    Math.abs(wynik - oczekiwanaSredniaDlugosc) < 0.1,
    "Nieprawidłowa średnia długość wiersza"
  );
};
const testznajdzSredniaLiczbeSlowNaWiersz = () => {
  const wiersze = ["To jest wiersz", "To jest inny wiersz", "Ostatni wiersz"];
  const oczekiwanaSredniaznajdzLiczbeSlow = 3;
  const wynik = znajdzSredniaLiczbeSlowNaWiersz(wiersze);
  console.assert(
    wynik === oczekiwanaSredniaznajdzLiczbeSlow,
    "Nieprawidłowa średnia liczba słów na wiersz"
  );
};

const testznajdzHistogramSlow = () => {
  const wiersze = ["To jest wiersz", "To jest inny wiersz", "Ostatni wiersz"];
  const oczekiwanyHistogram = new Map([
    ["to", 2],
    ["jest", 2],
    ["wiersz", 3],
    ["inny", 1],
    ["ostatni", 1],
  ]);
  const wynik = znajdzHistogramSlow(wiersze);
  console.assert(
    JSON.stringify([...wynik]) === JSON.stringify([...oczekiwanyHistogram]),
    "Nieprawidłowy histogram słów"
  );
};
const testStatystykiDlaPliku = async () => {
  // stworz plik testowy
  const sciezka = "test.txt";

  const wiersze = ["To jest wiersz", "To jest inny wiersz", "Ostatni wiersz"];

  await zapiszPlik(sciezka, wiersze.join("\n"));

  const oczekiwaneStatystyki = {
    liczbaWierszy: 3,
    liczbaSlow: 9,
    sredniaDlugoscWiersza: 15.666666666666666,
    sredniaLiczbaSlowNaWiersz: 3,

    histogramSlow: new Map([
      ["to", 2],
      ["jest", 2],
      ["wiersz", 3],
      ["inny", 1],
      ["ostatni", 1],
    ]),
  };

  const wynik = await statystykiDlaPliku(sciezka);

  // usun plik testowy
  await fs.unlink(sciezka);

  console.assert(
    JSON.stringify(wynik) === JSON.stringify(oczekiwaneStatystyki),
    "Nieprawidłowe statystyki"
  );
};

const uruchomTesty = async () => {
  testznajdzLiczbeWierszy();
  testznajdzLiczbeSlow();
  testznajdzSredniaDlugoscWiersza();
  testznajdzSredniaLiczbeSlowNaWiersz();
  testznajdzHistogramSlow();
  testStatystykiDlaPliku();
  console.log("Wszystkie testy zakończone powodzeniem");
};

uruchomTesty();
