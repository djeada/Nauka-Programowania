var Main = (function() {
    function Main() {}
    Main.znajdzParyV1 = function(lista, suma) {
        var wynik = ([]);
        for (var i = 0; i < lista.length; i++) {
            {
                for (var j = i + 1; j < lista.length; j++) {
                    {
                        if (lista[i] + lista[j] === suma) {
                            var para = (new Main.Pair(lista[i], lista[j]));
                            (wynik.push(para) > 0);
                        }
                    };
                }
            };
        }
        return (wynik.slice(0));
    };
 
    Main.listyRowne = function(a1, a2) {
        if (a1 == null && a2 == null)
            return true;
        if (a1 == null || a2 == null)
            return false;
        if (a1.length != a2.length)
            return false;
        for (var i = 0; i < a1.length; i++) {
            if (!a1[i].equals(a2[i]))
                return false;
        }
        return true;
    };
    Main.test1 = function() {
        var lista = ([0, 4, 5, 6, 2, 9, 2, 3].slice(0));
        var wynik = ([]);

        (wynik.push(new Main.Pair(0, 5)) > 0);

        (wynik.push(new Main.Pair(2, 3)) > 0);

        (wynik.push(new Main.Pair(2, 3)) > 0);
        var suma = 5;

        if (!Main.listyRowne(wynik, Main.znajdzParyV1(lista, suma))) {
            throw new Error("Assertion error;");
        };
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
(function(Main) {
    var Pair = (function() {
        function Pair(firstValue, secondValue) {
            if (this.first === undefined) {
                this.first = null;
            }
            if (this.second === undefined) {
                this.second = null;
            }
            this.first = firstValue;
            this.second = secondValue;
        }

        Pair.prototype.equals = function(o) {
            return (o != null && o instanceof Main.Pair) && (this.first === o.first) && (this.second === o.second);
        };
        return Pair;
    }());
    Main.Pair = Pair;
    Pair["__class"] = "Main.Pair";
})(Main || (Main = {}));
Main.main(null);
