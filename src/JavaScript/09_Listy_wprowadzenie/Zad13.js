   sumaCiaguArt = function(lista) {
       var minimum = Math.min.apply(Math, lista);
       var maksimum = Math.max.apply(Math, lista);
       return ((lista.length + 1) * (minimum + maksimum) / 2);
   };
   znajdzBrakujacyElement = function(lista) {
       var suma = 0;
       for (var i = 0; i < lista.length; i++) {
           var liczba = lista[i]; {
               suma += liczba;
           }
       }
       var sumaPrzedzialu = sumaCiaguArt(lista);
       return sumaPrzedzialu - suma;
   };
   test1 = function() {
       var lista = [6, 8, 4, 10, 14, 2]
       var oczekiwane = 12;
       var wynik = znajdzBrakujacyElement(lista);
       if (!(wynik == oczekiwane)) {
           throw new Error(`Assertion error line 89: ${wynik} != ${oczekiwane}`);
       }
   };
   test2 = function() {
       var lista = [1, 2, 4, 5, 6]
       var oczekiwane = 3;
       var wynik = znajdzBrakujacyElement(lista);
       if (!(wynik == oczekiwane)) {
           throw new Error(`Assertion error line 99: ${wynik} != ${oczekiwane}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);