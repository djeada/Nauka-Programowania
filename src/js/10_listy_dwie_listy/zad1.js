   wypisz = function(listaA, listaB) {
       var n = listaA.length < listaB.length ? listaA.length : listaB.length;
       for (var i = 0; i < n; i++) {
           {
               process.stdout.write(listaA[i] + ", ");
               process.stdout.write(listaB[i] + ", ");
           };
       }
       for (var i = n; i < listaA.length; i++) {
           {
               process.stdout.write(listaA[i] + ", ");
           };
       }
       for (var i = n; i < listaB.length; i++) {
           {
               process.stdout.write(listaB[i] + ", ");
           };
       }
   };
   main = function(args) {
       var listaA = ([5, 3, 7, 2].slice(0));
       var listaB = ([1, -2, 3].slice(0));
       wypisz(listaA, listaB);
   };

   main(null);