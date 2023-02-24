   kwadrat = function(a) {
       for (var y = 0; y < a; y++) {
           {
               for (var x = 0; x < a; x++) {
                   {
                       process.stdout.write("x");
                   };
               }
               process.stdout.write("\n");
           };
       }
   };
   main = function(args) {
       var a = 5;
       kwadrat(a);
   };

   main(null);