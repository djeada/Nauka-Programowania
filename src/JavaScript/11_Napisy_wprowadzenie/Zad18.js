var Main = (function() {
    function Main() {}
    Main.odwroc = function(slowo) {
        var rozdziel = slowo.split("");
        var odwroc = rozdziel.reverse();
        return odwroc.join("");
    };
    Main.odwrocNapisyV1 = function(napis) {
        var slowa = napis.split(" ");

        for (var i = 0; i < slowa.length; i++) {
            slowa[i] = Main.odwroc(slowa[i]);
        }

        return slowa.join(" ").trim();
    };
    Main.test1 = function() {
        var napis = "Cameron Diaz";
        var oczekiwane = "noremaC zaiD";
        var wynik = Main.odwrocNapisyV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
