   main = function(args) {
       console.info("podaj dwie liczby:");
       var rl = require('readline-sync');
       var a = rl.question('');
       var b = rl.question('');
       if (a === b) {
           console.info("liczby sa jednakowe");
       } else {
           console.info("liczby sa rozne");
       }
   };

   main(null);