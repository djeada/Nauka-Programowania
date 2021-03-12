var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        console.info("Podaj dwie liczby: ");
        var rl = require('readline-sync');
        var a = rl.question('');
        var b = rl.question('');

        if (b < a) {
            var pom = a;
            a = b;
            b = pom;
        }
        for (var i = a + 1; i < b; i++) {
            {
                console.info(i + " ");
            };
        }
        console.info("\n");
        for (var i = a + 1; i < b; i++) {
            {
                if (i % 3 === 0) {
                    console.info(i + " ");
                }
            };
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
