   wypiszPoziomo = function(napis, k) {
       for (var i = 0; i < napis.length; i += k) {
           {
               process.stdout.write(napis.charAt(i) + ", ");
           };
       }
       console.info("\n");
   };
   wypiszPionowo = function(napis, k) {
       for (var i = 0; i < napis.length; i += k) {
           {
               console.info(napis.charAt(i));
           };
       }
   };
   main = function(args) {
       var napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
       var k = 3;
       wypiszPoziomo(napis, k);
       wypiszPionowo(napis, k);
   };

   main(null);