   odwrocNapisV1 = function(slowo) {
       var rozdziel = slowo.split("");
       var odwroc = rozdziel.reverse();
       return odwroc.join("");
   };
   odwrocNapisV2 = function(slowo) {
       if (slowo === "")
           return "";
       else
           return odwrocNapisV2(slowo.substring(1)) + slowo.charAt(0);
   };
   test1 = function() {
       var napis = "adam";
       var oczekiwane = "mada";
       var wynik = odwrocNapisV1(napis);
       if (!(wynik === oczekiwane)) {
           throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
       }
   };
   test2 = function() {
       var napis = "adam";
       var oczekiwane = "mada";
       var wynik = odwrocNapisV2(napis);
       if (!(wynik === oczekiwane)) {
           throw new Error(`Assertion error line 30: ${wynik} === ${oczekiwane}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);