var Main = (function() {
    function Main() {}
    Main.policzSlowaV1 = function(slowo) {
        var spacja = true;
        var licznik = 0;

        for (const znak of slowo) {
            if (znak === " ") {
                spacja = true;
            } else if (znak.toLowerCase() != znak.toUpperCase() && spacja) {
                licznik += 1;
                spacja = false;
            }
        }

        return licznik;
    };
    Main.test1 = function() {
        var napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
        var wynik = 9;

        if (!(Main.policzSlowaV1(napis) === wynik)) {
            throw new Error("Assertion error line 25: assert policzSlowaV1(napis) == wynik;");
        };
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
