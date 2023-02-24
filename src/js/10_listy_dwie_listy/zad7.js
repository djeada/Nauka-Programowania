   roznicaV1 = function(listaA, listaB) {
       var wynik = ([]);
       for (var i = 0; i < listaA.length; i++) {
           var liczba = listaA[i]; {
               if (!(listaB.indexOf((liczba)) >= 0)) {
                   (wynik.push(liczba) > 0);
               }
           }
       }
       for (var i = 0; i < listaB.length; i++) {
           var liczba = listaB[i]; {
               if (!(listaA.indexOf((liczba)) >= 0)) {
                   (wynik.push(liczba) > 0);
               }
           }
       }
       return wynik;
   };
   test1 = function() {
       var listaA = [9, 2, 5, 4]
       var listaB = [4, 2, 1]
       var oczekiwane = [9, 5, 1]
       var wynik = roznicaV1(listaA, listaB);
       if (wynik.length !== oczekiwane.length) {
           throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
       }
       for (var i = 0; i < wynik.length; i++) {
           if (wynik[i] !== oczekiwane[i]) {
               throw new Error(`Assertion error line 33: ${wynik[i]} != ${oczekiwane[i]}`);
           }
       }
   };
   main = function(args) {
       test1();
   };

   main(null);