   min2 = function(a, b) {
       return a < b ? a : b;
   };
   maks2 = function(a, b) {
       return a > b ? a : b;
   };
   min3 = function(a, b, c) {
       var minAB = a < b ? a : b;
       return minAB < c ? minAB : c;
   };
   maks3 = function(a, b, c) {
       var maksAB = a > b ? a : b;
       return maksAB > c ? maksAB : c;
   };
   main = function(args) {
       console.info("Podaj dwie liczby: ");
       var rl = require('readline-sync');
       var a = rl.question('');
       var b = rl.question('');
       console.info("mniejsza liczba to: ");
       console.info(min2(a, b));
       console.info("\n");
       console.info("wieksza liczba to: ");
       console.info(maks2(a, b));
       console.info("\n");
       console.info("Podaj trzy liczby: ");
       var rl = require('readline-sync');
       var a = rl.question('');
       var b = rl.question('');
       var c = rl.question('');
       console.info("najmniejsza liczba to: ");
       console.info(min3(a, b, c));
       console.info("\n");
       console.info("najwieksza liczba to ");
       console.info(maks3(a, b, c));
       console.info("\n");
   };

   main(null);