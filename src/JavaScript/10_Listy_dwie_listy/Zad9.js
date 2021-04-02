var Main = (function() {
    function Main() {}
    Main.usunCzescWspolnaV1 = function(listaA, listaB) {
        for (var i = 0; i < listaA.length; i++) {
            {
                if ((listaB.indexOf((listaA[i])) >= 0)) {
                    listaA.splice(i, 1)[0];
                    i--;
                }
            };
        }
        return listaA;
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
        var listaA = ([3, 6, 2, 7, 9].slice(0));
        var listaB = ([4, 2, 3, 5, 6].slice(0));
        var wynik = ([7, 9].slice(0));

        if (!Main.listyRowne(wynik, Main.usunCzescWspolnaV1(listaA, listaB))) {
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
