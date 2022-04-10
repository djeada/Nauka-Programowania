/*
Otrzymujesz napis reprezentujacy nazwe pliku. Przeszukaj caly
system i zapisz w liscie wszystkie sciezki plikow o danej nazwie.
*/

const fs = require('fs').promises;
const path = require('path');

znajdzSciezki = async (nazwaPliku) => {
    const sciezki = [];
    const sciezka = process.env.HOME;
    const dane = await fs.readdir(sciezka);
    for (const danePliku of dane) {
        const sciezkaPliku = path.join(sciezka, danePliku);
        const stat = await fs.lstat(sciezkaPliku);
        if (stat.isFile() && danePliku === nazwaPliku) {
            sciezki.push(sciezkaPliku);
        }
    }
    return sciezki;
}


test1 = async () => {
    const nazwaPliku = 'test.txt';
    const sciezkiPlikow = ['lista.txt', nazwaPliku];
    const tekst = 'przykladowy tekst.\n';

    const sciezkaFolderu = 'temp_dir';
    await fs.mkdir(sciezkaFolderu);

    for (const plik of sciezkiPlikow) {
        const sciezkaPliku = path.join(sciezkaFolderu, plik);
        await fs.writeFile(sciezkaPliku, tekst);
    }

    const oczekiwane = sciezkiPlikow;
    const wynik = await znajdzSciezki(nazwaPliku);

    if (wynik.length !== oczekiwane.length) {
        throw new Error(`Assertion error line 180: ${wynik.length} != ${oczekiwane.length}`);
    }

    for (const sciezkaPliku of oczekiwane) {
        if (wynik.indexOf(sciezkaPliku) === -1) {
            throw new Error(`Assertion error line 185: ${wynik} != ${oczekiwane}`);
        }
    }

    await fs.rmdir(sciezkaFolderu, {
        recursive: true
    });
}

main = async () => {
    await test1();
}

main();