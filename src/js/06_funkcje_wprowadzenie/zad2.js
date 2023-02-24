   suma = function(a, b) {
       return a + b;
   };
   roznica = function(a, b) {
       return b - a;
   };
   iloczyn = function(a, b) {
       return a * b;
   };
   reszta = function(a, b) {
       return a % b;
   };
   main = function(args) {
       console.info("Podaj dwie liczby: ");
       var rl = require('readline-sync');
       var a = rl.question('');
       var b = rl.question('');
       console.info("suma liczb to: " + suma(a, b) + "\n");
       console.info("roznice drugiej i pierwszej to: " + roznica(a, b) + "\n");
       console.info("iloczyn liczb to: " + iloczyn(a, b) + "\n");
       console.info("reszte z dzielenia pierwszej przez druga to: " + reszta(a, b) + "\n");
   };

   main(null);