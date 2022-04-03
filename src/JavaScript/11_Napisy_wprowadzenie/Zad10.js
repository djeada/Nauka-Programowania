var Main = (function() {
    function Main() {}
    Main.wyczysc = function(napis) {
        napis = napis.trim();
        return napis.replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "");
    };
    Main.najdluzsze = function(napis) {
        var wynik = null;
        var dlugosc = 0;
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = Main.wyczysc(slowo);
                    if (slowo.length > dlugosc) {
                        wynik = slowo;
                        dlugosc = slowo.length;
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = Main.wyczysc(slowo);
            if (slowo.length > dlugosc) {
                wynik = slowo;
                dlugosc = slowo.length;
            }
        }
        return wynik;
    };
    Main.najkrotsze = function(napis) {
        var wynik = null;
        var dlugosc = napis.length;
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = Main.wyczysc(slowo);
                    if (slowo.length < dlugosc) {
                        wynik = slowo;
                        dlugosc = slowo.length;
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = Main.wyczysc(slowo);
            if (slowo.length < dlugosc) {
                wynik = slowo;
                dlugosc = slowo.length;
            }
        }
        return wynik;
    };
    Main.test1 = function() {
        var napis = "Kaczka lubi wiosne.";
        var oczekiwane = "Kaczka";
        var wynik = Main.najdluzsze(napis);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.test2 = function() {
        var napis = "Kaczka lubi wiosne.";
        var oczekiwane = "lubi";
        var wynik = Main.najkrotsze(napis);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 30: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
