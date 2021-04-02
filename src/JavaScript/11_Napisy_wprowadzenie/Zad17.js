var Main = (function() {
    function Main() {}
    Main.liczby = function(lista) {
        var wynik = "";
        for (var index8291 = 0; index8291 < lista.length; index8291++) {
            var liczba = lista[index8291]; {
                wynik += String(liczba).toString();
            }
        }
        return wynik;
    };
    Main.test1 = function() {
        var lista = ([2, 4, 7].slice(0));
        var wynik = "247";
        if (!(wynik === Main.liczby(lista))) {
            throw new Error("Assertion error line 16: assert wynik.equals(liczby(lista));");
        };
    };
    Main.test2 = function() {
        var lista = ([]);
        var wynik = "";
        if (!(wynik === Main.liczby(lista))) {
            throw new Error("Assertion error line 22: assert wynik.equals(liczby(lista));");
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
