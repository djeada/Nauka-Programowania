   nwdV1 = function(a, b) {
       if (b === 0) {
           return a;
       }
       return nwdV1(b, a % b);
   };
   nwdV2 = function(a, b) {
       var c;
       while ((b !== a % b)) {
           {
               c = b;
               b = a % b;
               a = c;
               if (b === 0) {
                   break;
               }
           }
       };
       return a;
   };
   test1 = function() {
       var a = 14;
       var b = 21;
       var oczekiwane = 7;
       var wynik = nwdV1(a, b);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 29: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test2 = function() {
       var a = 14;
       var b = 21;
       var oczekiwane = 7;
       var wynik = nwdV2(a, b);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 38: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);