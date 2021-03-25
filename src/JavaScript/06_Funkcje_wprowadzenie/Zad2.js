var Main = /** @class */ (function() {
    function Main() {}
    Main.suma = function(a, b) {
        return a + b;
    };
    Main.roznica = function(a, b) {
        return b - a;
    };
    Main.iloczyn = function(a, b) {
        return a * b;
    };
    Main.reszta = function(a, b) {
        return a % b;
    };
    Main.main = function(args) {
        console.info("Podaj dwie liczby: ");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        console.info("suma liczb to: " + Main.suma(a, b) + "\n");
        console.info("roznice drugiej i pierwszej to: " + Main.roznica(a, b) + "\n");
        console.info("iloczyn liczb to: " + Main.iloczyn(a, b) + "\n");
        console.info("reszte z dzielenia pierwszej przez druga to: " + Main.reszta(a, b) + "\n");
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
