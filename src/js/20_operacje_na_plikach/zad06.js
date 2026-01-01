/*
ZAD-06 — Statystyki pliku tekstowego

**Poziom:** ★★☆
**Tagi:** `files`, `stats`, `dict`, `regex`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Oblicz:

a) liczbę wierszy,
b) łączną liczbę słów (słowa = ciągi liter),
c) średnią długość wiersza (w znakach),
d) średnią liczbę słów na wiersz,
e) częstość występowania słów (słownik).

### Wejście

* 1 linia: `file_path`

### Wyjście

5 elementów w tej kolejności:

1. liczba wierszy
2. liczba słów
3. średnia długość wiersza
4. średnia liczba słów na wiersz
5. słownik częstości słów

Każdy element wypisz w osobnej linii.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\tekst.txt
```

**Wyjście:**

```
4
12
17.75
3.0
{'ala': 2, 'ma': 2, 'kota': 1, 'kot': 1, 'na': 1, 'imię': 1, 'filemon': 1, 'filemona': 1, 'lubi': 2, 'mleko': 1}
```

### Uwagi o formatowaniu

* Jeżeli ujednolicisz wielkość liter — w słowniku używaj małych liter (jak w przykładzie).
* Interpunkcję traktuj jako separator (usuń ją przy wyznaczaniu słów).

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
    "Nieprawidlowa liczba wierszy"
  );
};

const testznajdzLiczbeSlow = () => {
  const wiersze = ["To jest wiersz", "To jest inny wiersz", "Ostatni wiersz"];
  const oczekiwanaznajdzLiczbeSlow = 9;
  const wynik = znajdzLiczbeSlow(wiersze);
  console.assert(
    wynik === oczekiwanaznajdzLiczbeSlow,
    "Nieprawidlowa liczba slow"
  );
};
const testznajdzSredniaDlugoscWiersza = () => {
  const wiersze = ["To jest wiersz", "To jest inny wiersz", "Ostatni wiersz"];
  const oczekiwanaSredniaDlugosc = 15.666;

  const wynik = znajdzSredniaDlugoscWiersza(wiersze);
  console.assert(
    Math.abs(wynik - oczekiwanaSredniaDlugosc) < 0.1,
    "Nieprawidlowa srednia dlugosc wiersza"
  );
};
const testznajdzSredniaLiczbeSlowNaWiersz = () => {
  const wiersze = ["To jest wiersz", "To jest inny wiersz", "Ostatni wiersz"];
  const oczekiwanaSredniaznajdzLiczbeSlow = 3;
  const wynik = znajdzSredniaLiczbeSlowNaWiersz(wiersze);
  console.assert(
    wynik === oczekiwanaSredniaznajdzLiczbeSlow,
    "Nieprawidlowa srednia liczba slow na wiersz"
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
    "Nieprawidlowy histogram slow"
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
    "Nieprawidlowe statystyki"
  );
};

const uruchomTesty = async () => {
  testznajdzLiczbeWierszy();
  testznajdzLiczbeSlow();
  testznajdzSredniaDlugoscWiersza();
  testznajdzSredniaLiczbeSlowNaWiersz();
  testznajdzHistogramSlow();
  testStatystykiDlaPliku();
  console.log("Wszystkie testy zakonczone powodzeniem");
};

uruchomTesty();

