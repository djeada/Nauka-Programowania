   suma = function(listaA, listaB) {
       var wynik = (listaA.slice(0));
       var n = wynik.length < listaB.length ? wynik.length : listaB.length;
       for (var i = 0; i < n; i++) {
           {
               wynik[i] = wynik[i] + listaB[i];
           };
       }
       for (var i = n; i < listaB.length; i++) {
           {
               wynik.push(listaB[i]);
           };
       }
       return (wynik.slice(0));
   };
   test1 = function() {
       var listaA = [3, 1, 2, 5]
       var listaB = [2, 8, 6, 5]
       var oczekiwane = [5, 9, 8, 10]
       var wynik = suma(listaA, listaB);
       if (wynik.length !== oczekiwane.length) {
           throw new Error(`Assertion error line 24: ${wynik.length} != ${oczekiwane.length}`);
       }
       for (var i = 0; i < wynik.length; i++) {
           if (wynik[i] !== oczekiwane[i]) {
               throw new Error(`Assertion error line 28: ${wynik[i]} != ${oczekiwane[i]}`);
           }
       }
   };
   main = function(args) {
       test1();
   };

   main(null);