/*
Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke folderu.
Drugi napis reprezentuje rozszerzenie szukanych plikow. Znajdz w
folderze wszystkie pliki z danym rozszerzeniem. Nazwy znalezionych
plikow zapisz w liscie.
*/

const fs = require('fs').promises;
const path = require('path');

znajdzPliki = async (sciezka, rozszerzenie) => {
    const pliki = [];
    const dane = await fs.readdir(sciezka);
    for (const danePliku of dane) {
        const sciezkaPliku = path.join(sciezka, danePliku);
        const stat = await fs.lstat(sciezkaPliku);
        if (stat.isFile() && path.extname(danePliku) === rozszerzenie) {
            pliki.push(danePliku);
        }
    }
    return pliki;
}


test1 = async () => {
    const sciezkaFolderu = 'temp_dir';
    const sciezkikiPlikow = ['lista.txt', 'test.txt'];
    const tekst = 'przykladowy tekst.\n';

    await fs.mkdir(sciezkaFolderu);

    for (const plik of sciezkikiPlikow) {
        const sciezkaPliku = path.join(sciezkaFolderu, plik);
        await fs.writeFile(sciezkaPliku, tekst);
    }

    const oczekiwane = sciezkikiPlikow;
    const wynik = await znajdzPliki(sciezkaFolderu, '.txt');

    if (wynik.length !== oczekiwane.length) {
        throw new Error(`Assertion error line 180: ${wynik.length} != ${oczekiwane.length}`);
    }

    for (const nazwaPliku of oczekiwane) {
        if (wynik.indexOf(nazwaPliku) === -1) {
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