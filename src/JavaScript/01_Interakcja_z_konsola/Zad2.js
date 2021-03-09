var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');
        console.info(b);
        console.info(a);

    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
