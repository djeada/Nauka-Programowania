   trojkat = function(a) {
       for (var y = 0; y < a; y++) {
           {
               for (var x = 0; x <= y; x++) {
                   {
                       process.stdout.write("*");
                   };
               }
               process.stdout.write("\n");
           };
       }
   };
   choinka = function(n) {
       for (var i = 1; i <= n; i++) {
           {
               trojkat(i);
           };
       }
   };
   main = function(args) {
       var a = 5;
       choinka(a);
   };

   main(null);