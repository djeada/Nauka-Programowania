var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("podaj cztery liczby:");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        var c = rl.question('');
        var d = rl.question('');
        var maksAB = a > b ? a : b;
        var maksCD = c > d ? c : d;
        var maks = maksAB > maksCD ? maksAB : maksCD;
        console.info(maks);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
