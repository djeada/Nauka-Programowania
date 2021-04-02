var Main = /** @class */ (function() {
    function Main() {}
    Main.polaczV1 = function(listaA, listaB) {
        if ((listaA.length == 0)) {
            return listaB;
        }
        if ((listaB.length == 0)) {
            return listaA;
        }
        var wynik = ([]);
        var i = 0;
        var j = 0;
        while ((i < listaA.length && j < listaB.length)) {
            {
                if (listaA[i] < listaB[j]) {
                    (wynik.push(listaA[i]) > 0);
                    i++;
                } else {
                    (wynik.push(listaB[j]) > 0);
                    j++;
                }
            }
        };
        for (var k = i; k < listaA.length; k++) {
            {
                (wynik.push(listaA[k]) > 0);
            };
        }
        for (var k = j; k < listaB.length; k++) {
            {
                (wynik.push(listaB[k]) > 0);
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
        var listaA = ([5, 7, 11].slice(0));
        var listaB = ([1, 3, 8, 14].slice(0));
        var wynik = ([1, 3, 5, 7, 8, 11, 14].slice(0));

        if (!Main.listyRowne(wynik, Main.polaczV1(listaA, listaB))) {
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
