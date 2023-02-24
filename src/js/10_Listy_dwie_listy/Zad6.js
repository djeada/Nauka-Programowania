   czescWspolnaV1 = function(listaA, listaB) {
       var wynik = ([]);
       for (var i = 0; i < listaA.length; i++) {
           var liczba = listaA[i]; {
               if ((listaB.indexOf((liczba)) >= 0)) {
                   (wynik.push(liczba) > 0);
               }
           }
       }
       return (wynik.slice(0));
   };
   test1 = function() {
       var listaA = [3, 6, 2, 7, 9]
       var listaB = [4, 2, 3, 5, 6]
       var oczekiwane = [3, 6, 2]
       var wynik = czescWspolnaV1(listaA, listaB);
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