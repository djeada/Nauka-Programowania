var Main = (function() {
    function Main() {}
    Main.mediana = function(listaA, listaB) {
        var i = 0;
        var j = 0;
        var n = listaA.length;
        var m = listaB.length;
        var m1 = -1;
        var m2 = -1;
        for (var licznik = 0; licznik <= ((n + m) / 2 | 0); licznik++) {
            {
                if ((m + n) % 2 === 0) {
                    m2 = m1;
                }
                if (i !== n && j !== m) {
                    m1 = (listaA[i] > listaB[j]) ? listaB[j++] : listaA[i++];
                } else if (i < n) {
                    m1 = listaA[i++];
                } else {
                    m1 = listaB[j++];
                }
            };
        }
        if ((m + n) % 2 === 1) {
            return m1;
        }
        return (m1 + m2) / 2.0;
    };
    Main.test1 = function() {
        var listaA = ([2, 4, 7].slice(0));
        var listaB = ([3, 5, 9].slice(0));
        var wynik = 4.5;
        if (!(Main.mediana(listaA, listaB) === wynik)) {
            throw new Error("Assertion error line 31: assert mediana(listaA, listaB) == wynik;");
        };
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
