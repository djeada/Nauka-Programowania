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
        var wynik = "Kaczka";
        if (!(wynik === Main.najdluzsze(napis))) {
            throw new Error("Assertion error line 64: assert wynik.equals(najdluzsze(napis));");
        };
    };
    Main.test2 = function() {
        var napis = "Kaczka lubi wiosne.";
        var wynik = "lubi";
        if (!(wynik === Main.najkrotsze(napis))) {
            throw new Error("Assertion error line 70: assert wynik.equals(najkrotsze(napis));");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
