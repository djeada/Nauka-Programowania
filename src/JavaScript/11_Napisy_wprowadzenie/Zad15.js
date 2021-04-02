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
        var wynik = (["We", "think", "in", "generalities", "but", "we", "live", "in", "details"].slice(0));
        if (!((function(a1, a2) {
                if (a1 == null && a2 == null)
                    return true;
                if (a1 == null || a2 == null)
                    return false;
                if (a1.length != a2.length)
                    return false;
                for (var i = 0; i < a1.length; i++) {
                    if (a1[i] != a2[i])
                        return false;
                }
                return true;
            })(wynik, Main.slowaV1(napis)))) {
            throw new Error("Assertion error line 34: assert wynik.equals(slowaV1(napis));");
        };
    };
    Main.test2 = function() {
        var napis = "";
        var wynik = ([]);
        if (!((function(a1, a2) {
                if (a1 == null && a2 == null)
                    return true;
                if (a1 == null || a2 == null)
                    return false;
                if (a1.length != a2.length)
                    return false;
                for (var i = 0; i < a1.length; i++) {
                    if (a1[i] != a2[i])
                        return false;
                }
                return true;
            })(wynik, Main.slowaV1(napis)))) {
            throw new Error("Assertion error line 40: assert wynik.equals(slowaV1(napis));");
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
