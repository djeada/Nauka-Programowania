var Main = (function () {
    function Main() {
    }
    Main.sumaDwochV1 = function (lista, liczba) {
        var n = lista.length;
        for (var i = 0; i < n; i++) {
            {
                for (var j = i + 1; j < n; j++) {
                    {
                        if ( lista[j] +  lista[i] === liczba) {
                            return (new Main.Pair(i, j));
                        }
                    }
                    ;
                }
            }
            ;
        }
        return (new Main.Pair(-1, -1));
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
    Main.test1 = function () {
        var lista = ( [1, 3, 4, 5, 2].slice(0));
        var liczba = 5;
        var wynik = (new Main.Pair(0, 2));
        if (!Main.listyRowne(Main.sumaDwochV1(lista, liczba), wynik)) {
            throw new Error("Assertion error;");
        }
        ;
    };
    Main.test2 = function () {
        var lista = ( [2, -6, 10, 21, 8].slice(0));
        var liczba = 7;
        var wynik = (new Main.Pair(-1, -1));
        if (!Main.listyRowne(Main.sumaDwochV1(lista, liczba), wynik)) {
            throw new Error("Assertion error;");
        }
        ;
    };
    Main.main = function (args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
(function (Main) {
    var Pair = (function () {
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
        Pair.prototype.equals = function (o) {
            return (o != null && o instanceof Main.Pair) && (this.first === o.first) && (this.second === o.second);
        };
        return Pair;
    }());
    Main.Pair = Pair;
    Pair["__class"] = "Main.Pair";
})(Main || (Main = {}));
Main.main(null);
