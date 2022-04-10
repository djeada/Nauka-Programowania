   inicjalizacjaDanych = function() {
       console.info("podaj nazwe oraz haslo do zapamietania: ");
       var rl = require('readline-sync');
       nazwa = rl.question('');
       haslo = rl.question('');
       return [nazwa, haslo];
   };
   czyDanePoprawne = function(nazwa, haslo) {
       var nowaNazwa;
       var noweHaslo;
       while ((!(nazwa === nowaNazwa) || !(haslo === noweHaslo))) {
           {
               console.info("Aby zalogowac sie do systemu: podaj nazwe oraz haslo: ");
               var rl = require('readline-sync');
               nowaNazwa = rl.question('');
               noweHaslo = rl.question('');
           }
       };
       console.info("Logowanie do systemu przebieglo pomyslnie");
       console.info("\n");
   };
   main = function(args) {
       var wynik = inicjalizacjaDanych();
       var nazwa = wynik[0];
       var haslo = wynik[1];
       czyDanePoprawne(nazwa, haslo);
   };

   main(null);