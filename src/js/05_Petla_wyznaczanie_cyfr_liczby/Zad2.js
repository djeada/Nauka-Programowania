   main = function(args) {
       var a = require('readline-sync').question('podaj liczbe:');
       while ((a > 0)) {
           {
               console.info(a % 10);
               console.info("\n");
               a = (a / 10 | 0);
           }
       };
   };

   main(null);