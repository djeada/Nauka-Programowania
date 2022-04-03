var Main = (function() {
    function Main() {}
    Main.wyczysc = function(napis) {
        napis = napis.trim();
        return napis.replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "");
    };
    Main.slowaV1 = function(napis) {
        var wynik = ([]);
        var pocz = 0;
        var konc = 0;
        while (((konc = napis.indexOf(' ', pocz)) !== -1)) {
            {
                if (konc !== pocz) {
                    var slowo = napis.substring(pocz, konc);
                    slowo = Main.wyczysc(slowo);
                    if (!(slowo.length === 0)) {
                        (wynik.push(slowo) > 0);
                    }
                }
                pocz = konc + 1;
            }
        };
        if (konc !== pocz) {
            var slowo = napis.substring(pocz);
            slowo = Main.wyczysc(slowo);
            if (!(slowo.length === 0)) {
                (wynik.push(slowo) > 0);
            }
        }
        return (wynik.slice(0));
    };
    Main.test1 = function() {
        var napis = "We think in generalities, but we live in details";
        var oczekiwane = (["We", "think", "in", "generalities", "but", "we", "live", "in", "details"].slice(0));
        var wynik = Main.slowaV1(napis);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 31: ${wynik[i]} != ${oczekiwane[i]}`);
            }
        }
    };
    Main.test2 = function() {
        var napis = "";
        var oczekiwane = ([]);
        var wynik = Main.slowaV1(napis);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 39: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 41: ${wynik[i]} != ${oczekiwane[i]}`);
            }
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
