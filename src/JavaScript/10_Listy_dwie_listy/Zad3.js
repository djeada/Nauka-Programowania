var Main = /** @class */ (function() {
    function Main() {}
    Main.suma = function(listaA, listaB) {
        var wynik = (listaA.slice(0));
        var n = wynik.length < listaB.length ? wynik.length : listaB.length;
        for (var i = 0; i < n; i++) {
            {
                wynik[i] = wynik[i] + listaB[i];
            };
        }
        for (var i = n; i < listaB.length; i++) {
            {
                wynik.push(listaB[i]);
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
        var listaA = ([3, 1, 2, 5].slice(0));
        var listaB = ([2, 8, 6, 5].slice(0));
        var wynik = ([5, 9, 8, 10].slice(0));

        if (!Main.listyRowne(wynik, Main.suma(listaA, listaB))) {
            throw new Error("Assertion error;");
        };
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
