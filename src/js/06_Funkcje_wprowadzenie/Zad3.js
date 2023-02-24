   czyWieksza = function(a, b) {
       return a > b;
   };
   czySumaMniejsza = function(a, b) {
       var suma = a + b;
       return suma < 10;
   };
   czyObieNieparzyste = function(a, b) {
       return a % 2 === 1 && b % 2 === 1;
   };
   wieksza = function(a, b) {
       return a > b ? a : b;
   };
   czyWiekszaNizKwad = function(a, b) {
       return wieksza(a, b) < Math.pow(a, 2);
   };
   main = function(args) {
       console.info("Podaj dwie liczby: ");
       var rl = require('readline-sync');
       var a = rl.question('');
       var b = rl.question('');
       console.info("Pierwsza liczba jest wieksza od drugiej: ");
       console.info(czyWieksza(a, b));
       console.info("\n");
       console.info("Suma liczb jest mniejsza od 10: ");
       console.info(czySumaMniejsza(a, b));
       console.info("\n");
       console.info("Obie liczby nieparzyste: ");
       console.info(czyObieNieparzyste(a, b));
       console.info("\n");
       console.info("Wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu ");
       console.info(czyWiekszaNizKwad(a, b));
       console.info("\n");
   };

   main(null);