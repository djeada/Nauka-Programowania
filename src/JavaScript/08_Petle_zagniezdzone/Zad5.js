   literaX = function(n) {
       for (var y = 0; y < n; y++) {
           {
               for (var x = 0; x < n; x++) {
                   {
                       if (y === x || x === (n - 1 - y)) {
                           process.stdout.write("*");
                       } else {
                           process.stdout.write(" ");
                       }
                   };
               }
               process.stdout.write("\n");
           };
       }
   };
   main = function(args) {
       var a = 5;
       literaX(a);
   };

   main(null);