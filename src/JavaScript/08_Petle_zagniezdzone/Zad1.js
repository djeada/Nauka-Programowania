var Main = /** @class */ (function() {
    function Main() {}
    Main.kwadrat = function(a) {
        for (var y = 0; y < a; y++) {
            {
                for (var x = 0; x < a; x++) {
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
        Main.kwadrat(a);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
