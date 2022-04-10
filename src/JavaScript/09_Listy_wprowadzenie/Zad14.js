   elementBezParyV1 = function(lista) {
       var pom = ([]);
       var _loop_1 = function(i) {
           var liczba = lista[i]; {
               if ((pom.indexOf((liczba)) >= 0)) {
                   (function(a) {
                       var index = a.indexOf(liczba);
                       if (index >= 0) {
                           a.splice(index, 1);
                           return true;
                       } else {
                           return false;
                       }
                   })(pom);
               } else {
                   (pom.push(liczba) > 0);
               }
           }
       };
       for (var i = 0; i < lista.length; i++) {
           _loop_1(i);
       }
       return pom[0];
   };
   elementBezParyV2 = function(lista) {
       var wynik = 0;
       for (var i = 0; i < lista.length; i++) {
           var liczba = lista[i]; {
               wynik ^= liczba;
           }
       }
       return wynik;
   };
   test1 = function() {
       var lista = [1, 3, 1, 7, 3, 1, 1]
       var oczekiwane = 7;
       var wynik = elementBezParyV1(lista);
       if (oczekiwane !== wynik) {
           throw new Error(`Assertion error line 42: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test2 = function() {
       var lista = [1, 3, 1, 7, 3, 1, 1]
       var oczekiwane = 7;
       var wynik = elementBezParyV2(lista);
       if (oczekiwane !== wynik) {
           throw new Error(`Assertion error line 50: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);