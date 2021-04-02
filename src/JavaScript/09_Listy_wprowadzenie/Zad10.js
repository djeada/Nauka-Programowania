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
        var wsplX = ([-2, 7, 8].slice(0));
        var wsplY = ([4, 5, -8].slice(0));
        if (!(Main.czyTrojkatV1(wsplX, wsplY))) {
            throw new Error("Assertion error line 26: assert czyTrojkatV1(wsplX, wsplY);");
        };
        if (!(Main.czyTrojkatV2(wsplX, wsplY))) {
            throw new Error("Assertion error line 27: assert czyTrojkatV2(wsplX, wsplY);");
        };
    };
    Main.test2 = function() {
        var wsplX = ([0, 2, 5].slice(0));
        var wsplY = ([0, -2, -5].slice(0));
        if (!(!Main.czyTrojkatV1(wsplX, wsplY))) {
            throw new Error("Assertion error line 33: assert !czyTrojkatV1(wsplX, wsplY);");
        };
        if (!(!Main.czyTrojkatV2(wsplX, wsplY))) {
            throw new Error("Assertion error line 34: assert !czyTrojkatV2(wsplX, wsplY);");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
