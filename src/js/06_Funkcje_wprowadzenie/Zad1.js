   funkcja1 = function() {
       return 3;
   };
   funkcja2 = function() {
       return "Tak";
   };
   funkcja3 = function() {
       return true;
   };
   test1 = function() {
       if (!(funkcja1() === 3)) {
           throw new Error("Assertion error line 15: assert funkcja1() == 3;");
       };
   };
   test2 = function() {
       if (!(funkcja2() === ("Tak"))) {
           throw new Error("Assertion error line 19: assert funkcja2().equals('Tak');");
       };
   };
   test3 = function() {
       if (!(funkcja3())) {
           throw new Error("Assertion error line 23: assert funkcja3();");
       };
   };
   main = function(args) {
       test1();
       test2();
       test3();
   };

   main(null);