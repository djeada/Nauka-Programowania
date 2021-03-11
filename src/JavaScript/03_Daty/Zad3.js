var Main = /** @class */ (function() {
    function Main() {}
    Main.main = function(args) {
        var rok = require('readline-sync').question('Podaj rok:');
        if (rok % 4 === 0) {
            if (rok % 100 === 0) {
                if (rok % 400 === 0) {
                    console.info("rok jest przestepny");
                } else {
                    console.info("rok nie jest przestepny");
                }
            } else {
                console.info("rok jest przestepny");
            }
        } else {
            console.info("rok nie jest przestepny");
        }
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
