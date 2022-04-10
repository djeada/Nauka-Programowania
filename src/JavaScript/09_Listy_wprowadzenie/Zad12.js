   rotacjaV1 = function(lista, kierunek, liczba) {
       if (kierunek === ("prawo")) {
           for (var i = 0; i < liczba; i++) {
               {
                   lista.splice(0, 0, lista[lista.length - 1]);
                   lista.splice(lista.length - 1, 1)[0];
               };
           }
       } else {
           for (var i = 0; i < liczba; i++) {
               {
                   (lista.push(lista[0]) > 0);
                   lista.splice(0, 1)[0];
               };
           }
       }
       return lista;
   };
   test1 = function() {
       var lista = [5, 27, 6, 2, 1, 10, 8]
       var kierunek = "lewo";
       var liczba = 2;
       var oczekiwane = [6, 2, 1, 10, 8, 5, 27]
       var wynik = rotacjaV1(lista, kierunek, liczba);
       if (!(wynik.length == oczekiwane.length)) {
           throw new Error(`Assertion error line 59: ${wynik.length} != ${oczekiwane.length}`);
       }
       for (var i = 0; i < wynik.length; i++) {
           if (!(wynik[i] == oczekiwane[i])) {
               throw new Error(`Assertion error line 59: ${wynik[i]} != ${oczekiwane[i]}`);
           }
       }
   };
   test2 = function() {
       var lista = [9, 9, 42, 47, 5, 6, 19, 7]
       var liczba = 3;
       var kierunek = "prawo";
       var oczekiwane = [6, 19, 7, 9, 9, 42, 47, 5]
       var wynik = rotacjaV1(lista, kierunek, liczba);
       if (!(wynik.length == oczekiwane.length)) {
           throw new Error(`Assertion error line 69: ${wynik.length} != ${oczekiwane.length}`);
       }
       for (var i = 0; i < wynik.length; i++) {
           if (!(wynik[i] == oczekiwane[i])) {
               throw new Error(`Assertion error line 69: ${wynik[i]} != ${oczekiwane[i]}`);
           }
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);