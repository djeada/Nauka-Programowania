   silnia = function(a) {
       var wynik = 1;
       while ((a > 0)) {
           {
               wynik *= a;
               a--;
           }
       };
       return wynik;
   };
   test1 = function() {
       var a = 4;
       var oczekiwane = 24;
       var wynik = silnia(a);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 33: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test2 = function() {
       var a = -5;
       var wynik = 1;
       var oczekiwane = silnia(a);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 33: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);