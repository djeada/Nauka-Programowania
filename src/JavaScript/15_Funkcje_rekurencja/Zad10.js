/*
Rozwaz gre, w ktorej w kazdym ruchu gracz moze zdobyc 3, 5 lub 10 punktow.
Dla otrzymanej liczby N, reprezentujacej calkowita liczbe punktow,
oblicz na ile sposobow gracz moze wygrac gre.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.czyTablicaNalezyDoTablicy = function (macierz, tablica) {
        for (var i = 0; i < macierz.length; i++) {
            if (macierz[i].length == tablica.length) {
                for (var j = 0; j < macierz[i].length; j++) {
                    if (macierz[i][j] != tablica[j]) {
                        break;
                    }
                    if (j == macierz[i].length - 1) {

                        return true;
                    }
                }
            }
        }
        return false;
    }

    Main.mozliweWygrane = function (n) {
        var wynik = [];
        var mozliweWygraneWew = function (tablica) {

          var suma = 0;
          for (var i = 0; i < tablica.length; i++) {
              suma += tablica[i];
          }
          if (suma > n)
              return;
          
          if (suma === n) {
            sorted = tablica.sort(function (a, b) { return a - b; });                                               
            if (!Main.czyTablicaNalezyDoTablicy(wynik, sorted)) {         
              wynik.push(sorted.slice(0));
            }
            return;
          }
          tablica.push(3);
          mozliweWygraneWew(tablica.slice(0));
          tablica.pop();
          tablica.push(5);
          mozliweWygraneWew(tablica.slice(0));
          tablica.pop();
          tablica.push(10);
          mozliweWygraneWew(tablica.slice(0));
          tablica.pop();
      }
        mozliweWygraneWew([]);
        return wynik.length;

    }

    Main.test1 = function () {
        var n = 10;
        var oczekiwane = 2;
        if (Main.mozliweWygrane(n) !== oczekiwane) {
            throw new Error("Assertion error line 24: assert zbudujNapis(n).equals(wynik);");
        }
    }
    Main.test2 = function () {
        var n = 20;
        var oczekiwane = 4;
        if (Main.mozliweWygrane(n) !== oczekiwane) {
            throw new Error("Assertion error line 24: assert zbudujNapis(n).equals(wynik);");
        }
    }
    Main.main = function (args) {
        Main.test1();
        Main.test2();
    }
    return Main;
}
());
Main["__class"] = "Main";
Main.main(null);
