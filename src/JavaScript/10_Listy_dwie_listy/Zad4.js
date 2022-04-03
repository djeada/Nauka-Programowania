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
        return wynik;
    };
    Main.test1 = function() {
        var listaA = [3, -5, 4]
        var listaB = [2, 6, 5]
        var oczekiwane = -4;
        var wynik = Main.mnozenieSkalarne(listaA, listaB);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 34: ${wynik} != ${oczekiwane}`);
        }
    };
    Main.test2 = function() {
        var listaA = [3, -5, 4]
        var listaB = [2, 6, 5]
        var oczekiwane = [-49, -7, 28]
        var wynik = Main.mnozenieWektorowe(listaA, listaB);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 43: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 46: ${wynik[i]} != ${oczekiwane[i]}`);
            }
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
