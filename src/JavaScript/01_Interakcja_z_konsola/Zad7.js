var Main = /** @class */ (function () {
    function Main() {
    }
    Main.main = function (args) {
	console.info("podaj podstawe i wysokosc trojkata:");
	var rl = require('readline-sync');
	var a = rl.question('');
	var h = rl.question('');
	console.info("pole trojkata o podstawie " + a + " i wysokosci " + h + " jest rowne " + (a * h / 2));
	var a = rl.question('podaj dlugosci bokow prostokata:\n');
	var b = rl.question('');
	console.info("pole prostokata o bokach " + a + " i " + b + " jest rowne " + (a * b));
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
