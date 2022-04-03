var Main = (function() {
    function Main() {}
    Main.liczby = function(n) {
        var wynik = "";
        for (var i = 1; i <= n; i++) {
            {
                wynik += String(i).toString();
            };
        }
        return wynik;
    };
    Main.test1 = function() {
        var n = 5;
        var oczekiwane = "12345";
        var wynik = Main.liczby(n);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 24: ${wynik} != ${oczekiwane}`);
        }
    };
    Main.test2 = function() {
        var n = -1;
        var oczekiwane = "";
        var wynik = Main.liczby(n);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 24: ${wynik} != ${oczekiwane}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
