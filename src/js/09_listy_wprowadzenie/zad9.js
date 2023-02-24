   usunDuplikatyV1 = function(lista) {
       var wynik = ([]);
       for (var i = 0; i < lista.length; i++) {
           var x = lista[i];
           if (!(wynik.indexOf((x)) >= 0))
               (wynik.push(x) > 0);
       }
       return wynik;
   };
   usunDuplikatyV2 = function(lista) {
       var wynik = ([]);
       var zbior = ([]);
       for (var i = 0; i < lista.length; i++) {
           var x = lista[i];
           if ((function(s, e) {
                   if (s.indexOf(e) == -1) {
                       s.push(e);
                       return true;
                   } else {
                       return false;
                   }
               })(zbior, x))
               (wynik.push(x) > 0);
       }
       return wynik;
   };
   test1 = function(args) {
       var lista = [2, 1, 2, 2, 3, 3]
       var oczekiwane = [2, 1, 3]
       var wynik = usunDuplikatyV1(lista);
       if (oczekiwane.length !== wynik.length) {
           throw new Error(`Assertion error line 34: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
       }
       for (var i = 0; i < oczekiwane.length; i++) {
           if (oczekiwane[i] !== wynik[i]) {
               throw new Error(`Assertion error line 38: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
           }
       }
   };
   test2 = function(args) {
       var lista = [2, 1, 2, 2, 3, 3]
       var oczekiwane = [2, 1, 3]
       var wynik = usunDuplikatyV2(lista);
       if (oczekiwane.length !== wynik.length) {
           throw new Error(`Assertion error line 47: oczekiwane: ${oczekiwane.length}, obliczone: ${wynik.length}`);
       }
       for (var i = 0; i < oczekiwane.length; i++) {
           if (oczekiwane[i] !== wynik[i]) {
               throw new Error(`Assertion error line 51: oczekiwane: ${oczekiwane[i]}, obliczone: ${wynik[i]}`);
           }
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);