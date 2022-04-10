   nwd = function(a, b) {
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
   nww = function(a, b) {
       return (a * b / nwd(a, b) | 0);
   };
   test1 = function() {
       var a = 14;
       var b = 21;
       var oczekiwane = 42;
       var wynik = nww(a, b);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 29: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
   };

   main(null);