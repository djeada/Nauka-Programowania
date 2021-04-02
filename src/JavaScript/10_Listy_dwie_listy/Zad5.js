var Main = /** @class */ (function() {
    function Main() {}
    Main.sredniaWazona = function(wagi, wartosci) {
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
    Main.test1 = function() {
        var wartosci = ([0.0, -23.0, -5.0, 2.0, -3.0, 4.0, 9.0].slice(0));
        var wagi = ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0].slice(0));
        var wynik = -1.1875;
        if (!(Main.sredniaWazona(wagi, wartosci) === wynik)) {
            throw new Error("Assertion error line 22: assert sredniaWazona(wagi, wartosci) == wynik;");
        };
    };
    Main.test2 = function() {
        var wartosci = ([2.0, 5.0, 0.0, 2.0, 1.0].slice(0));
        var wagi = ([0.2, 0.4, 0.1, 0.2, 0.1].slice(0));
        var wynik = 0.29;
        if (!(Main.sredniaWazona(wagi, wartosci) === wynik)) {
            throw new Error("Assertion error line 29: assert sredniaWazona(wagi, wartosci) == wynik;");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
