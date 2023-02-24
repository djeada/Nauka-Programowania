   naWielkieV1 = function(slowo) {
       return slowo.toUpperCase();
   };
   test1 = function() {
       var napis = "pacZka!";
       var oczekiwane = "PACZKA!";
       var wynik = naWielkieV1(napis);
       if (!(wynik === oczekiwane)) {
           throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
       }
   };
   main = function(args) {
       test1();
   };

   main(null);