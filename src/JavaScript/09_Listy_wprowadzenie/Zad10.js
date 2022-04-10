   odleglosc = function(x1, y1, x2, y2) {
       var roznicaX = x1 - x2;
       var roznicaY = y1 - y2;
       var sumaKwadratow = Math.pow(roznicaX, 2) + Math.pow(roznicaY, 2);
       return Math.sqrt(sumaKwadratow);
   };
   czyTrojkatV1 = function(wsplX, wsplY) {
       if (!(wsplX.length === wsplY.length && wsplX.length === 3)) {
           throw new Error("Assertion error line 10: assert wsplX.size() == wsplY.size() && wsplX.size() == 3;");
       };
       var odlegloscAB = odleglosc(wsplX[0], wsplY[0], wsplX[1], wsplY[1]);
       var odlegloscBC = odleglosc(wsplX[2], wsplY[2], wsplX[1], wsplY[1]);
       var odlegloscAC = odleglosc(wsplX[0], wsplY[0], wsplX[2], wsplY[2]);
       return (odlegloscAB + odlegloscBC) > odlegloscAC && (odlegloscAB + odlegloscAC) > odlegloscBC && (odlegloscAC + odlegloscBC) > odlegloscAB;
   };
   czyTrojkatV2 = function(wsplX, wsplY) {
       if (!(wsplX.length === wsplY.length && wsplX.length === 3)) {
           throw new Error("Assertion error line 18: assert wsplX.size() == wsplY.size() && wsplX.size() == 3;");
       };
       var a = wsplX[0] * (wsplY[1] - wsplY[2]) + wsplX[1] * (wsplY[2] - wsplY[0]) + wsplX[2] * (wsplY[0] - wsplY[1]);
       return a !== 0;
   };
   test1 = function() {
       var wsplX = [-2, 7, 8]
       var wsplY = [4, 5, -8]
       var oczekiwane = true
       var wynik = czyTrojkatV1(wsplX, wsplY)
       if (wynik !== oczekiwane) {
           throw new Error(`Assertion error line 31: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test2 = function() {
       var wsplX = [0, 2, 5]
       var wsplY = [0, -2, -5]
       var oczekiwane = false
       var wynik = czyTrojkatV1(wsplX, wsplY)
       if (wynik !== oczekiwane) {
           throw new Error(`Assertion error line 40: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test3 = function() {
       var wsplX = [-2, 7, 8]
       var wsplY = [4, 5, -8]
       var oczekiwane = true
       var wynik = czyTrojkatV2(wsplX, wsplY)
       if (wynik !== oczekiwane) {
           throw new Error(`Assertion error line 49: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test4 = function() {
       var wsplX = [0, 2, 5]
       var wsplY = [0, -2, -5]
       var oczekiwane = false
       var wynik = czyTrojkatV2(wsplX, wsplY)
       if (wynik !== oczekiwane) {
           throw new Error(`Assertion error line 58: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
       test3();
       test4();
   };

   main(null);