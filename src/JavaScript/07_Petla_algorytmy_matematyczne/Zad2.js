   potega = function(a, b) {
       var wynik = 1;
       for (var i = 0; i < Math.abs(b); i++) {
           {
               wynik *= a;
           };
       }
       if (b < 0) {
           return (1 / wynik | 0);
       }
       return wynik;
   };
   test1 = function() {
       var a = 2;
       var b = 3;
       var oczekiwane = 8.0;
       var wynik = potega(a, b);
       if (!(abs(wynik - oczekiwane) < 0.01)) {
           throw new Error(`Assertion error line 33: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       };
   };
   test2 = function() {
       var a = 10;
       var b = -5;
       var wynik = 1.0E-5;
       var oczekiwane = potega(a, b);
       if (!(abs(wynik - oczekiwane) < 0.01)) {
           throw new Error(`Assertion error line 33: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);