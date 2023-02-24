   main = function(args) {
       var a = require('readline-sync').question('podaj liczbe:');
       var suma = 0;
       while ((a > 0)) {
           {
               suma += (a % 10);
               a = (a / 10 | 0);
           }
       };
       console.info("Suma cyfr podanej liczby wynosi " + suma + "\n");
   };

   main(null);