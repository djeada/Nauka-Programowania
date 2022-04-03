/*
Rozwaz gre, w ktorej w kazdym ruchu gracz moze zdobyc 3, 5 lub 10 punktow.
Dla otrzymanej liczby N, reprezentujacej calkowita liczbe punktow,
oblicz na ile sposobow gracz moze wygrac gre.
*/

class ArraySet extends Set {
    add(arr) {
      super.add(arr.toString());
    }
    has(arr) {
      return super.has(arr.toString());
    }
  }

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.mozliweWygrane = function (n) {
        var wynik = new ArraySet();
        var mozliweWygraneWew = function (tablica) {

          var suma = 0;
          for (var i = 0; i < tablica.length; i++) {
              suma += tablica[i];
          }
          if (suma > n)
              return;
          
          if (suma === n) {
            sorted = tablica.sort(function (a, b) { return a - b; });                                       
            wynik.add(sorted.slice(0));
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
        return wynik.size;

    }

    Main.test1 = function () {
        var n = 10;
        var oczekiwane = 2;
        var wynik = Main.mozliweWygrane(n);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 55: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
        }
    }
    Main.test2 = function () {
        var n = 20;
        var oczekiwane = 4;
        var wynik = Main.mozliweWygrane(n);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 63: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
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
