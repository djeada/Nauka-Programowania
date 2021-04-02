var Main = (function() {
    function Main() {}
    Main.wyczysc = function(napis) {
        napis = napis.trim();
        return napis.replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "");
    };
    Main.srednia = function(napis) {
        var calk_dlugosc = 0;
        var n = 0;
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = Main.wyczysc(slowo);
                    if (!(slowo.length === 0)) {
                        n++;
                        calk_dlugosc += slowo.length;
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = Main.wyczysc(slowo);
            if (!(slowo.length === 0)) {
                n++;
                calk_dlugosc += slowo.length;
            }
        }
        return (calk_dlugosc / n | 0);
    };
    Main.test1 = function() {
        var napis = "Kaczka lubi wiosne.";
        var wynik = 5;
        if (!(Main.srednia(napis) === wynik)) {
            throw new Error("Assertion error line 37: assert srednia(napis) == wynik;");
        };
    };
    Main.test2 = function() {
        var napis = "Kaczka lubi wiosne.";
        var wynik = 5;
        if (!(Main.srednia(napis) === wynik)) {
            throw new Error("Assertion error line 43: assert srednia(napis) == wynik;");
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
