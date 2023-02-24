   main = function(args) {
       var a = require('readline-sync').question('podaj liczbe:');
       for (var i = 1; i < a; i++) {
           {
               console.info(i);
               console.info(" ");
           };
       }
       console.info("\n");
   };

   main(null);