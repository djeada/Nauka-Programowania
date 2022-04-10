   dostaw = function(listaA, listaB) {
       var wynik = (listaA.slice(0));
       for (var i = 0; i < listaB.length; i++) {
           var liczba = listaB[i]; {
               (wynik.push(liczba) > 0);
           }
       }
       return (wynik.slice(0));
   };
   podmien = function(listaA, listaB) {
       var wynik = (listaA.slice(0));
       for (var i = 0; i < wynik.length; i += 2) {
           {
               (wynik[i] = listaB[i]);
           };
       }
       return (wynik.slice(0));
   };
   test1 = function() {
       var listaA = [-2, 8, 3, 6]
       var listaB = [7, 5, 0]
       var oczekiwane = [-2, 8, 3, 6, 7, 5, 0]
       var wynik = dostaw(listaA, listaB);
       if (wynik.length !== oczekiwane.length) {
           throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
       }
   };
   test2 = function() {
       var listaA = [-2, 8, 3, 6]
       var listaB = [7, 5, 0]
       var oczekiwane = [7, 8, 0, 6]
       var wynik = podmien(listaA, listaB);
       if (wynik.length !== oczekiwane.length) {
           throw new Error(`Assertion error line 38: ${wynik.length} != ${oczekiwane.length}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);