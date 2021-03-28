var Main = /** @class */ (function() {
    function Main() {}
    Main.trojkat = function(a) {
        for (var y = 0; y < a; y++) {
            {
                for (var x = 0; x <= y; x++) {
                    {
                        process.stdout.write("x");
                    };
                }
                process.stdout.write("\n");
            };
        }
    };
    Main.main = function(args) {
        var a = 5;
        Main.trojkat(a);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
