   czyPierwsza = function(n) {
       if (n <= 1) {
           return false;
       }
       if (n % 2 === 0 && n !== 2) {
           return false;
       }
       for (var i = 3; i <= Math.sqrt(n); i += 2) {
           {
               if (n % i === 0) {
                   return false;
               }
           };
       }
       return true;
   };
   test1 = function() {
       var a = 15;
       var oczekiwane = false;
       var wynik = czyPierwsza(a);
       if (wynik) {
           throw new Error(`Assertion error line 24: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test2 = function() {
       var a = 7;
       var oczekiwane = true;
       var wynik = czyPierwsza(a);
       if (!(wynik === oczekiwane)) {
           throw new Error(`Assertion error line 32: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test3 = function() {
       var a = -15;
       var oczekiwane = false;
       var wynik = czyPierwsza(a);
       if (wynik) {
           throw new Error(`Assertion error line 24: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
       test3();
   };

   main(null);