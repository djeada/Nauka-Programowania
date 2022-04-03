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
    Main.test1 = function() {
        var listaA = [3, 6, 2, 7, 9]
        var listaB = [4, 2, 3, 5, 6]
        var oczekiwane = [3, 6, 2]
        var wynik = Main.czescWspolnaV1(listaA, listaB);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 33: ${wynik[i]} != ${oczekiwane[i]}`);
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
