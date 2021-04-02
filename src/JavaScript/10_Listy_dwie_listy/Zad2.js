var Main = /** @class */ (function() {
    function Main() {}
    Main.dostaw = function(listaA, listaB) {
        var wynik = (listaA.slice(0));
        for (var i = 0; i < listaB.length; i++) {
            var liczba = listaB[i]; {

                (wynik.push(liczba) > 0);
            }
        }
        return (wynik.slice(0));
    };
    Main.podmien = function(listaA, listaB) {
        var wynik = (listaA.slice(0));
        for (var i = 0; i < wynik.length; i += 2) {
            {

                (wynik[i] = listaB[i]);
            };
        }
        return (wynik.slice(0));
    };
    Main.listyRowne = function(a1, a2) {
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
    };
    Main.test1 = function() {
        var listaA = ([-2, 8, 3, 6].slice(0));
        var listaB = ([7, 5, 0].slice(0));
        var wynik = ([-2, 8, 3, 6, 7, 5, 0].slice(0));

        if (!Main.listyRowne(wynik, Main.dostaw(listaA, listaB))) {
            throw new Error("Assertion error;");
        };
    };
    Main.test2 = function() {
        var listaA = ([-2, 8, 3, 6].slice(0));
        var listaB = ([7, 5, 0].slice(0));
        var wynik = ([7, 8, 0, 6].slice(0));

        if (!Main.listyRowne(wynik, Main.podmien(listaA, listaB))) {
            throw new Error("Assertion error;");
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
