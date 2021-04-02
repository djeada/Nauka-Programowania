var Main = /** @class */ (function() {
    function Main() {}
    Main.czescWspolnaV1 = function(listaA, listaB) {
        var wynik = ([]);
        for (var i = 0; i < listaA.length; i++) {
            var liczba = listaA[i]; {
                if ((listaB.indexOf((liczba)) >= 0)) {
                    (wynik.push(liczba) > 0);
                }
            }
        }
        return (wynik.slice(0));
    };
    Main.wektoryRowne = function(v1, v2) {
        v1.sort();
        v2.sort();
        return (function(a1, a2) {
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
        })(v1, v2);
    };
    Main.test1 = function() {
        var listaA = ([3, 6, 2, 7, 9].slice(0));
        var listaB = ([4, 2, 3, 5, 6].slice(0));
        var wynik = ([3, 6, 2].slice(0));
        if (!(Main.wektoryRowne(Main.czescWspolnaV1(listaA, listaB), (wynik.slice(0))))) {
            throw new Error("Assertion error line 25: assert wektoryRowne(czescWspolnaV1(listaA, listaB), new ArrayList<Integer>(wynik));");
        };
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
