var Main = /** @class */ (function () {
    function Main() {
    }
    Main.main = function (args) {
	var rl = require('readline-sync');
	var kilogramy = rl.question('podaj wielkosc w kilogramach:\n');
	var gramy = kilogramy * 1000;
	console.info(kilogramy + " kg to " + gramy + " g.");

	var cal = rl.question('podaj wielkosc w calach:\n');
	var cm = cal / 2.54;
	console.info(cal + " cal to " + cm + " cm.");

	var sekundy = rl.question('podaj ilosc sekund:\n');
	var godziny = sekundy / 3600;
	console.info(sekundy + " sekund to " + godziny + " godzin");

	var euro = rl.question('podaj liczbe w euro:\n');
	var zloty = euro * 4.4;
	console.info(euro + " euro to " + zloty + " zlotych");

	var katStopnie = rl.question('podaj miare kata w stopniach:\n');
	var katRad = katStopnie * 0.0174532;
	console.info(katStopnie + " stopni to " + katRad + " radianow.");

	var tempF = rl.question('podaj temperature w Farenheitach:\n');
	var tempC = (tempF - 32) * 5 / 9;
	var tempK = tempC - 273;
	console.info(tempF + " F to " + tempC + " C i " + tempK + " K");        
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);

