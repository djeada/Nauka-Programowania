var Main = /** @class */ (function() {
    function Main() {}
    Main.wypiszPoziomo = function(napis, k) {
        for (var i = 0; i < napis.length; i += k) {
            {
                process.stdout.write(napis.charAt(i) + ", ");

            };
        }
        console.info("\n");
    };
    Main.wypiszPionowo = function(napis, k) {
        for (var i = 0; i < napis.length; i += k) {
            {
                console.info(napis.charAt(i));
            };
        }
    };
    Main.main = function(args) {
        var napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
        var k = 3;
        Main.wypiszPoziomo(napis, k);
        Main.wypiszPionowo(napis, k);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
