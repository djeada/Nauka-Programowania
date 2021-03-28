var Main = /** @class */ (function() {
    function Main() {}
    Main.trojkat = function(a) {
        for (var y = 0; y < a; y++) {
            {
                for (var x = 0; x <= y; x++) {
                    {
                        process.stdout.write("*");
                    };
                }
                process.stdout.write("\n");
            };
        }
    };
    Main.choinka = function(n) {
        for (var i = 1; i <= n; i++) {
            {
                Main.trojkat(i);
            };
        }
    };
    Main.main = function(args) {
        var a = 5;
        Main.choinka(a);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
