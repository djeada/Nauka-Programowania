   main = function(args) {
       var rl = require('readline-sync');
       var x = rl.question('podaj liczbe:');
       if (x > 5) {
           console.info(x);
       }
   };

   main(null);