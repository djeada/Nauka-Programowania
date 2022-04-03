var Main = /** @class */ (function() {
    function Main() {}
    Main.odleglosc = function(x1, y1, x2, y2) {
        var roznicaX = x1 - x2;
        var roznicaY = y1 - y2;
        var sumaKwadratow = Math.pow(roznicaX, 2) + Math.pow(roznicaY, 2);
        return Math.sqrt(sumaKwadratow);
    };
    Main.czyTrojkatV1 = function(wsplX, wsplY) {
        if (!(wsplX.length === wsplY.length && wsplX.length === 3)) {
            throw new Error("Assertion error line 10: assert wsplX.size() == wsplY.size() && wsplX.size() == 3;");
        };
        var odlegloscAB = Main.odleglosc(wsplX[0], wsplY[0], wsplX[1], wsplY[1]);
        var odlegloscBC = Main.odleglosc(wsplX[2], wsplY[2], wsplX[1], wsplY[1]);
        var odlegloscAC = Main.odleglosc(wsplX[0], wsplY[0], wsplX[2], wsplY[2]);
        return (odlegloscAB + odlegloscBC) > odlegloscAC && (odlegloscAB + odlegloscAC) > odlegloscBC && (odlegloscAC + odlegloscBC) > odlegloscAB;
    };
    Main.czyTrojkatV2 = function(wsplX, wsplY) {
        if (!(wsplX.length === wsplY.length && wsplX.length === 3)) {
            throw new Error("Assertion error line 18: assert wsplX.size() == wsplY.size() && wsplX.size() == 3;");
        };
        var a = wsplX[0] * (wsplY[1] - wsplY[2]) + wsplX[1] * (wsplY[2] - wsplY[0]) + wsplX[2] * (wsplY[0] - wsplY[1]);
        return a !== 0;
    };
    Main.test1 = function() {
        var wsplX = [-2, 7, 8]
        var wsplY = [4, 5, -8]
        var oczekiwane = true
        var wynik = Main.czyTrojkatV1(wsplX, wsplY)
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 31: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test2 = function() {
        var wsplX = [0, 2, 5]
        var wsplY = [0, -2, -5]
        var oczekiwane = false
        var wynik = Main.czyTrojkatV1(wsplX, wsplY)
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 40: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test3 = function() {
        var wsplX = [-2, 7, 8]
        var wsplY = [4, 5, -8]
        var oczekiwane = true
        var wynik = Main.czyTrojkatV2(wsplX, wsplY)
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 49: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.test4 = function() {
        var wsplX = [0, 2, 5]
        var wsplY = [0, -2, -5]
        var oczekiwane = false
        var wynik = Main.czyTrojkatV2(wsplX, wsplY)
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 58: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
        Main.test3();
        Main.test4();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
