   main = function(args) {
       var a = require('readline-sync').question('podaj liczbe:');
       if (a < 0) {
           console.info("liczba jest ujemna");
       } else if (a > 0) {
           console.info("liczba jest dodatnia");
       } else {
           console.info("liczba jest zerem");
       }
   };

   main(null);