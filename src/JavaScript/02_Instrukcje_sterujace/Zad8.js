var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("podaj trzy liczby:");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        var c = rl.question('');
        if (a + b > c && b + c > a && a + c > b) {
            console.info("z podanych bokow mozna zbudowac trojkat");
        } else {
            console.info("z podanych bokow nie mozna zbudowac trojkata");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
