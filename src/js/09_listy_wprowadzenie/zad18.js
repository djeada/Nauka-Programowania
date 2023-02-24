   indeksMin = function(lista) {
       var n = lista.length;
       for (var i = 0; i < n - 1; i++) {
           {
               if (lista[i] > lista[i + 1]) {
                   return i + 1;
               }
           };
       }
       return 0;
   };
   test1 = function() {
       var lista = [7, 8, -1, 4, 5]
       var oczekiwane = 2;
       var wynik = indeksMin(lista);
       if (wynik !== oczekiwane) {
           throw new Error(`Assertion error line 19: ${wynik} != ${oczekiwane}`);
       }
   };
   test2 = function() {
       var lista = [2, 3, 4, 5, 6]
       var oczekiwane = 0;
       var wynik = indeksMin(lista);
       if (wynik !== oczekiwane) {
           throw new Error(`Assertion error line 27: ${wynik} != ${oczekiwane}`);
       }
   };
   test3 = function() {
       var lista = [8, 9, 10, 11, 1]
       var oczekiwane = 4;
       var wynik = indeksMin(lista);
       if (wynik !== oczekiwane) {
           throw new Error(`Assertion error line 35: ${wynik} != ${oczekiwane}`);
       }
   };
   main = function(args) {
       test1();
       test2();
       test3();
   };

   main(null);