var Main = /** @class */ (function() {
    function Main() {}
    Main.funkcja1 = function() {
        return 3;
    };
    Main.funkcja2 = function() {
        return "Tak";
    };
    Main.funkcja3 = function() {
        return true;
    };
    Main.test1 = function() {
        if (!(Main.funkcja1() === 3)) {
            throw new Error("Assertion error line 15: assert funkcja1() == 3;");
        };
    };
    Main.test2 = function() {
        if (!(Main.funkcja2() === ("Tak"))) {
            throw new Error("Assertion error line 19: assert funkcja2().equals('Tak');");
        };
    };
    Main.test3 = function() {
        if (!(Main.funkcja3())) {
            throw new Error("Assertion error line 23: assert funkcja3();");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
        Main.test3();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
