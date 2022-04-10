/*
Stworz klase Klasa. Klasa powinna zawierac funkcje statyczna zwracajaca 
aktualna liczbe instancji klasy w programie. Stworz kilka obiektow klasy 
i przetestuj dzialanie funkcji.
*/


class Klasa {
    constructor() {
        Klasa.liczbaInstancji++;
    }

    static liczbaInstancji = 0;

    static wypiszLiczbeInstancji() {
        console.log(`Liczba instancji klasy Klasa wynosi ${Klasa.liczbaInstancji}`);
    }
}

test1 = function() {
    n = 10;
    for (let i = 0; i < n; i++) {
        let klasa = new Klasa();
    }

    wynik = Klasa.liczbaInstancji;
    if (wynik !== n) {
        throw new Error(`Assertion error line 63: oczekiwane: ${n}, obliczone: ${wynik}`);
    }

}

main = function() {
    test1();
}

main();