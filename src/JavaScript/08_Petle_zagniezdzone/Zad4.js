   tabliczkaMnozenia = function(n) {
       for (var y = 1; y <= n; y++) {
           {
               for (var x = 1; x <= n; x++) {
                   {
                       iloczyn = y * x;
                       process.stdout.write(iloczyn.toString());
                       process.stdout.write(" ");
                   };
               }
               process.stdout.write("\n");
           };
       }
   };
   main = function(args) {
       var a = 5;
       tabliczkaMnozenia(a);
   };

   main(null);