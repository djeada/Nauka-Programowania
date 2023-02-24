/*
Otrzymujesz napis reprezentujacy sciezke pliku tekstowego.
Kazdy wiersz pliku reprezentuje adres ip. Posortuj adresy ip
i zapisz je w liscie.
*/
const fs = require('fs').promises;

wczytajPlik = async (sciezka) => {
    const tekst = await fs.readFile(sciezka, 'utf8');
    wiersze = tekst.split('\n');
    wiersze = wiersze.filter(wiersz => wiersz.length > 0);
    return wiersze;
}

sortujAdresyIp = (ip) => {
    ip.sort((a, b) => {
        const a1 = a.split('.');
        const b1 = b.split('.');
        if (parseInt(a1[0]) < parseInt(b1[0])) {
            return -1;
        }
        if (parseInt(a1[0]) > parseInt(b1[0])) {
            return 1;
        }
        if (parseInt(a1[1]) < parseInt(b1[1])) {
            return -1;
        }
        if (parseInt(a1[1]) > parseInt(b1[1])) {
            return 1;
        }
        if (parseInt(a1[2]) < parseInt(b1[2])) {
            return -1;
        }
        if (parseInt(a1[2]) > parseInt(b1[2])) {
            return 1;
        }
        if (parseInt(a1[3]) < parseInt(b1[3])) {
            return -1;
        }
        if (parseInt(a1[3]) > parseInt(b1[3])) {
            return 1;
        }
        return 0;
    });

    return ip;
}

test1 = async () => {
    const sciezka = 'temp.txt';
    const tekst = '123.4.245.23\n104.244.253.29\n1.198.3.93\n32.183.93.40\n104.30.244.2\n104.244.4.1\n';
    oczekiwane = ["1.198.3.93", "32.183.93.40", "104.30.244.2", "104.244.4.1", "104.244.253.29", "123.4.245.23"];

    await fs.writeFile(sciezka, tekst);
    const adresyIp = await wczytajPlik(sciezka);
    wynik = sortujAdresyIp(adresyIp);

    if (!(wynik.length == oczekiwane.length)) {
        throw new Error(`Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (wynik[i] != oczekiwane[i]) {
            throw new Error(`Assertion error line 39: ${wynik[i]} != ${oczekiwane[i]}`);
        }
    }
    await fs.unlink(sciezka);
}

main = async () => {
    await test1();
}

main();