var Main = /** @class */ (function () {
    function Main() {
    }
    Main.main = function (args) {
	console.info("podaj: cene plytki, dlugosc boku plytki i wymiary podlogi");
	var rl = require('readline-sync');
	var cena = rl.question('');
	var bokPlytki = rl.question('');
	var szerokoscPodlogi = rl.question('');
	var dlugoscPodlogi = rl.question('');
	var szerokoscKonieczna = szerokoscPodlogi + bokPlytki - szerokoscPodlogi % bokPlytki;
	var dlugoscKonieczna = dlugoscPodlogi + bokPlytki - dlugoscPodlogi % bokPlytki;
	var polePlytki = Math.pow(bokPlytki, 2);
	var polePodlogi = szerokoscKonieczna * dlugoscKonieczna;
	var calkowityKoszt = cena * polePodlogi / polePlytki;
	console.info("Dla plytki o dlugosci boku " + bokPlytki + " i ceny " + cena + " calkowity koszt wylozenia podlogi o wymiarach " + szerokoscPodlogi + "x" + dlugoscPodlogi + " wynosi " + calkowityKoszt);
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
