   znajdzKluczV1 = function(tablica, klucz) {
       for (var i = 0; i < tablica.length; i++) {
           if (tablica[i] === klucz)
               return i;;
       }
       return -1;
   };
   znajdzKluczV2 = function(tablica, klucz) {
       return tablica.indexOf(klucz);
   };
   test1 = function() {
       var tablica = [3, 5, -7, 4, 9, -11, 2];
       var klucz = 2;
       var oczekiwane = 6;
       var wynik = znajdzKluczV1(tablica, klucz);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 20: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       };
   };
   test2 = function() {
       var tablica = [3, -2, 4, 9, -3, -40, 8, 5, -7, -1];
       var klucz = 2;
       var oczekiwane = -1;
       var wynik = znajdzKluczV1(tablica, klucz);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 29: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test3 = function() {
       var tablica = [3, 5, -7, 4, 9, -11, 2];
       var klucz = 2;
       var oczekiwane = 6;
       var wynik = znajdzKluczV2(tablica, klucz);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 38: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   test4 = function() {
       var tablica = [3, -2, 4, 9, -3, -40, 8, 5, -7, -1];
       var klucz = 2;
       var oczekiwane = -1;
       var wynik = znajdzKluczV2(tablica, klucz);
       if (!(oczekiwane === wynik)) {
           throw new Error(`Assertion error line 47: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
       test3();
       test4();
   };

   main(null);