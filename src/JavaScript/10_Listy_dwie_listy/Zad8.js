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
        return wynik;
    };
    Main.test1 = function() {
        var listaA = [5, 7, 11]
        var listaB = [1, 3, 8, 14]
        var oczekiwane = [1, 3, 5, 7, 8, 11, 14]
        var wynik = Main.polaczV1(listaA, listaB);

        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 29: ${wynik[i]} != ${oczekiwane[i]}`);
            }
        }
        
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
