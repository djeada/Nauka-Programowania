var Main = (function() {
    function Main() {}
    Main.liczby = function(lista) {
        var wynik = "";
        for (var i = 0; i < lista.length; i++) {
            var liczba = lista[i]; {
                wynik += String(liczba).toString();
            }
        }
        return wynik;
    };
    Main.test1 = function() {
        var lista = ([2, 4, 7].slice(0));
        var oczekiwane = "247";
        var wynik = Main.liczby(lista);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 29: ${wynik} != ${oczekiwane}`);
        }
    };
    Main.test2 = function() {
        var lista = ([]);
        var oczekiwane = "";
        var wynik = Main.liczby(lista);
        if (wynik !== oczekiwane) {
            throw new Error(`Assertion error line 29: ${wynik} != ${oczekiwane}`);
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
