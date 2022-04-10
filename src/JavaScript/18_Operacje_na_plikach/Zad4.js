/*
Otrzymujesz napis reprezentujacy sciezke pliku tekstowego.
Wczytaj i wypisz tresc pliku.
*/

const fs = require('fs').promises;

wypiszPlik = async (sciezka) => {
    const tekst = await fs.readFile(sciezka, 'utf8');
    console.log(tekst);
}

main = async () => {
    const sciezka = 'test.txt';
    const tekst = 'Przykladowy tekst.';

    await fs.writeFile(sciezka, tekst);

    wypiszPlik(sciezka);

    await fs.unlink(sciezka);
}

main();