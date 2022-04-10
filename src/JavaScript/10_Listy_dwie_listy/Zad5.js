   sredniaWazona = function(wagi, wartosci) {
       if (!(wagi.length === wartosci.length)) {
           throw new Error("Assertion error line 3: assert wagi.size() == wartosci.size();");
       };
       var suma = 0.0;
       for (var i = 0; i < wartosci.length; i++) {
           var liczba = wartosci[i]; {
               suma += liczba;
           }
       }
       var sumaIloczynow = 0.0;
       for (var i = 0; i < wartosci.length; i++) {
           {
               sumaIloczynow += (wartosci[i] * wagi[i]);
           };
       }
       return sumaIloczynow / suma;
   };
   test1 = function() {
       var wartosci = [0.0, -23.0, -5.0, 2.0, -3.0, 4.0, 9.0]
       var wagi = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
       var oczekiwane = -1.1875;
       var wynik = sredniaWazona(wagi, wartosci);
       if (!(wynik == oczekiwane)) {
           throw new Error(`Assertion error line 27: ${wynik} != ${oczekiwane}`);
       }
   };
   test2 = function() {
       var wartosci = [2.0, 5.0, 0.0, 2.0, 1.0]
       var wagi = [0.2, 0.4, 0.1, 0.2, 0.1]
       var oczekiwane = 0.29;
       var wynik = sredniaWazona(wagi, wartosci);
       if (!(wynik == oczekiwane)) {
           throw new Error(`Assertion error line 36: ${wynik} != ${oczekiwane}`);
       }
   };
   main = function(args) {
       test1();
       test2();
   };

   main(null);