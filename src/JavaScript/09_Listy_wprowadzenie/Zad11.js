   policzSamochodyV1 = function(lista) {
       var licznik = 0;
       for (var i = 0; i < lista.length; i++) {
           {
               if ((function(c) {
                       return c.charCodeAt == null ? c : c.charCodeAt(0);
                   })(lista[i]) == 'A'.charCodeAt(0)) {
                   for (var j = i + 1; j < lista.length; j++) {
                       {
                           if ((function(c) {
                                   return c.charCodeAt == null ? c : c.charCodeAt(0);
                               })(lista[j]) == 'B'.charCodeAt(0)) {
                               licznik++;
                           }
                       };
                   }
               } else if ((function(c) {
                       return c.charCodeAt == null ? c : c.charCodeAt(0);
                   })(lista[i]) == 'B'.charCodeAt(0)) {
                   for (var j = i - 1; j > -1; j--) {
                       {
                           if ((function(c) {
                                   return c.charCodeAt == null ? c : c.charCodeAt(0);
                               })(lista[j]) == 'A'.charCodeAt(0)) {
                               licznik++;
                           }
                       };
                   }
               }
           };
       }
       return (licznik / 2 | 0);
   };
   policzSamochodyV2 = function(lista) {
       var licznik = 0;
       var pom = 0;
       for (var index8217 = 0; index8217 < lista.length; index8217++) {
           var x = lista[index8217]; {
               if ((function(c) {
                       return c.charCodeAt == null ? c : c.charCodeAt(0);
                   })(x) == 'A'.charCodeAt(0)) {
                   pom++;
               } else if ((function(c) {
                       return c.charCodeAt == null ? c : c.charCodeAt(0);
                   })(x) == 'B'.charCodeAt(0)) {
                   licznik += pom;
               }
           }
       }
       return licznik;
   };
   test1 = function() {
       var lista = ['A', 'B', 'A', 'B', 'B']
       var oczekiwane = 5;
       var wynik = policzSamochodyV1(lista);
       if (!(wynik == oczekiwane)) {
           throw new Error(`Assertion error line 59: ${wynik} != ${oczekiwane}`);
       }
   };
   test2 = function() {
       var lista = ['A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A']
       var oczekiwane = 15;
       var wynik = policzSamochodyV1(lista);
       if (!(wynik == oczekiwane)) {
           throw new Error(`Assertion error line 67: ${wynik} != ${oczekiwane}`);
       }
   };
   test3 = function() {
       var lista = ['A', 'B', 'A', 'B', 'B']
       var oczekiwane = 5;
       var wynik = policzSamochodyV2(lista);
       if (!(wynik == oczekiwane)) {
           throw new Error(`Assertion error line 75: ${wynik} != ${oczekiwane}`);
       }
   };
   test4 = function() {
       var lista = ['A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A']
       var oczekiwane = 15;
       var wynik = policzSamochodyV2(lista);
       if (!(wynik == oczekiwane)) {
           throw new Error(`Assertion error line 83: ${wynik} != ${oczekiwane}`);
       }
   };
   main = function(args) {
       test1();
       test2();
       test3();
       test4();
   };

   main(null);