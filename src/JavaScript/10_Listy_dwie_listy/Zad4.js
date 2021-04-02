var Main = /** @class */ (function() {
    function Main() {}
    Main.mnozenieSkalarne = function(listaA, listaB) {
        if (!(listaA.length === listaB.length)) {
            throw new Error("Assertion error line 3: assert listaA.size() == listaB.size();");
        };
        var wynik = 0;
        for (var i = 0; i < listaA.length; i++) {
            {
                wynik += listaA[i] * listaB[i];
            };
        }
        return wynik;
    };
    Main.mnozenieWektorowe = function(listaA, listaB) {
        if (!(listaA.length === listaB.length && listaA.length === 3)) {
            throw new Error("Assertion error line 12: assert listaA.size() == listaB.size() && listaA.size() == 3;");
        };
        var wynik = ([]);

        (wynik.push(listaA[1] * listaB[2] - listaA[2] * listaB[1]) > 0);

        (wynik.push(listaA[2] * listaB[0] - listaA[0] * listaB[2]) > 0);

        (wynik.push(listaA[0] * listaB[1] - listaA[1] * listaB[0]) > 0);
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
        var listaA = ([3, -5, 4].slice(0));
        var listaB = ([2, 6, 5].slice(0));
        var iloczynSkalar = -4;
        if (!(Main.mnozenieSkalarne(listaA, listaB) === iloczynSkalar)) {
            throw new Error("Assertion error line 24: assert mnozenieSkalarne(listaA, listaB) == iloczynSkalar;");
        };
    };
    Main.test2 = function() {
        var listaA = ([3, -5, 4].slice(0));
        var listaB = ([2, 6, 5].slice(0));
        var iloczynWekt = ([-49, -7, 28].slice(0));

        if (!Main.listyRowne(iloczynWekt, Main.mnozenieWektorowe(listaA, listaB))) {
        throw new Error("Assertion error;");
    };

}; Main.main = function(args) {
    Main.test1();
    Main.test2();
};
return Main;
}());
Main["__class"] = "Main";
Main.main(null);
