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
    Main.main = function(args) {
        var napis = "Cameron Diaz";
        var wynik = "noremaC zaiD";

        if (!(Main.odwrocNapisyV1(napis) === wynik)) {
            throw new Error("Assertion error line 21: assert odwrocNapisyV1(napis).equals(wynik);");
        };
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
