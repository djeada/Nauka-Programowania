   mnozenie = function(a, b) {
       var wynik = 0;
       for (var i = 0; i < b; i++) {
           {
               wynik += a;
           };
       }
       return wynik;
   };
   dzielenie = function(a, b) {
       var wynik = 0;
       while ((a >= b)) {
           {
               a -= b;
               wynik++;
           }
       };
       return wynik;
   };
   test1 = function() {
       var a = 2;
       var b = 3;
       var oczekiwne = 6;
       var wynik = mnozenie(a, b);
       if (!(oczekiwne === wynik)) {
           throw new Error(`Assertion error line 28: oczekiwane: ${oczekiwne}, obliczone: ${wynik}`);
       };
   };
   test2 = function() {
       var a = 30;
       var b = 6;
       var wynik = 5;
       var oczekiwne = dzielenie(a, b);
       if (!(oczekiwne === wynik)) {
           throw new Error(`Assertion error line 37: oczekiwane: ${oczekiwne}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);