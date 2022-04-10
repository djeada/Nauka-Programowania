   main = function(args) {
       var n = require('readline-sync').question('podaj liczbe:');
       var suma = 0;
       for (var i = 1; i < n; i++) {
           {
               suma += i;
           };
       }
       console.info(suma);
       console.info("\n");
   };

   main(null);