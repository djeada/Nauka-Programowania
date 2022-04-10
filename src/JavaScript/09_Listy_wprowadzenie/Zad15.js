   elementDominujacyV1 = function(lista) {
       var n = lista.length;
       for (var i = 0; i <= (n / 2); i++) {
           {
               var licznik = 1;
               for (var j = i + 1; j < n; j++) {
                   {
                       if (lista[j] === lista[i]) {
                           licznik++;
                       }
                   };
               }
               if (licznik > (n / 2)) {
                   return lista[i];
               }
           };
       }
       return -1;
   };
   elementDominujacyV2 = function(lista) {
       // uzyj mapy do zliczania elementow
       var n = lista.length;
       var histogram = {};
       for (var i = 0; i < n; i++) {
           {
               if (histogram[lista[i]] == null) {
                   histogram[lista[i]] = 1;
               } else {
                   histogram[lista[i]]++;
               }
           };
       }
       // znajdz najczesciej wystepujacy element
       var maks = 0;
       var element = -1;
       for (var klucz in histogram) {
           {
               if (histogram[klucz] > maks) {
                   maks = histogram[klucz];
                   element = klucz;
               }
           };
       }
       // sprawdz czy element wystpuje co najmniej n/2 razy
       if (maks > (n / 2)) {
           return parseInt(element);
       }
       return -1;
   };
   test1 = function() {
       var lista = [4, 7, 4, 4, 2]
       var oczekiwane = 4;
       var wynik = elementDominujacyV1(lista);
       if (oczekiwane !== wynik) {
           throw new Error(`Assertion error line 58: ${oczekiwane} !== ${wynik}`);
       }
   };
   test2 = function() {
       var lista = [1, 2, 4, 5, 6]
       var oczekiwane = -1;
       var wynik = elementDominujacyV1(lista);
       if (oczekiwane !== wynik) {
           throw new Error(`Assertion error line 66: ${oczekiwane} !== ${wynik}`);
       }
   };
   test3 = function() {
       var lista = [4, 7, 4, 4, 2]
       var oczekiwane = 4;
       var wynik = elementDominujacyV2(lista);
       if (oczekiwane !== wynik) {
           throw new Error(`Assertion error line 74: ${oczekiwane} !== ${wynik}`);
       }
   };
   test4 = function() {
       var lista = [1, 2, 4, 5, 6]
       var oczekiwane = -1;
       var wynik = elementDominujacyV2(lista);
       if (oczekiwane !== wynik) {
           throw new Error(`Assertion error line 82: ${oczekiwane} !== ${wynik}`);
       }
   };
   main = function(args) {
       test1();
       test2();
       test3();
       test4();
   };

   main(null);