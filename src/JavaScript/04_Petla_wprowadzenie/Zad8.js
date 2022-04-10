   main = function(args) {
       console.info("Podaj dwie liczby: ");
       var rl = require('readline-sync');
       var glowy = rl.question('');
       var nogi = rl.question('');
       for (var i = 0; i < glowy; i++) {
           {
               var owce = glowy - i;
               if (2 * i + 4 * owce === nogi) {
                   console.info(i + " " + owce + "\n");
                   break;
               }
           };
       }
   };

   main(null);